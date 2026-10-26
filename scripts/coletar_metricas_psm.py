#!/usr/bin/env python3
"""Coleta os indicadores PSM/CID a partir das issues, milestones e pull requests do GitHub.

O histórico é recalculado inteiro a cada execução: os indicadores são calculados como
estavam no fim de cada domingo desde o início do projeto e no dia da execução.
"""
import csv
import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

PASTA = "docs/gestao/evidencias"
PAGINA = "docs/gestao/indicadores.md"
FUSO = ZoneInfo("America/Sao_Paulo")
PRAZO_REVISAO = timedelta(hours=48)
LABEL_RETRABALHO = "correcao"
INDICADORES_EVOLUCAO = ["PRs revisados no prazo", "Retrabalho (issues)",
                        "Desvio de prazo médio", "Esforço real / estimado"]


def gh(*args):
    saida = subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout
    return json.loads(saida) if saida.strip() else []


def data_hora(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(FUSO) if iso else None


def secao(corpo, titulo):
    m = re.search(rf"^###\s*{re.escape(titulo)}\s*$(.*?)(?=^###|\Z)", corpo or "", re.M | re.S)
    return m.group(1).strip() if m else ""


def numero(texto):
    m = re.search(r"\d+(?:[.,]\d+)?", texto or "")
    return float(m.group().replace(",", ".")) if m else None


REGISTRO_HORAS = re.compile(r"(\d{1,2})/(\d{1,2})\s*[—–-]\s*(.+?)\s*[—–-]\s*(\d+(?:[.,]\d+)?)\s*h", re.I)


def registros_horas(corpo, ano):
    regs = []
    for dia, mes, pessoa, h in REGISTRO_HORAS.findall(secao(corpo, "Horas reais")):
        try:
            regs.append((date(ano, int(mes), int(dia)), pessoa.strip(), float(h.replace(",", "."))))
        except ValueError:
            print(f"AVISO: data inválida em registro de horas: {dia}/{mes} — {pessoa}")
    return regs


def pct(parte, total):
    return round(100 * parte / total, 1) if total else None


def escrever_csv(nome, campos, linhas):
    with open(os.path.join(PASTA, nome), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


def coletar():
    nome_repo = gh("repo", "view", "--json", "nameWithOwner")["nameWithOwner"]
    issues = gh("issue", "list", "--state", "all", "--limit", "500", "--json",
                "number,title,body,assignees,labels,milestone,state,stateReason,createdAt,closedAt")
    milestones = gh("api", f"repos/{nome_repo}/milestones?state=all&per_page=100")
    prs = gh("pr", "list", "--state", "merged", "--limit", "500", "--json",
             "number,author,createdAt,mergedAt,reviews")
    eventos = [e for pagina in gh("api", "--paginate", "--slurp",
                                  f"repos/{nome_repo}/issues/events?per_page=100") for e in pagina]
    eventos = [e for e in eventos if "pull_request" not in e["issue"]]

    prazos = {m["title"]: date.fromisoformat(m["due_on"][:10]) for m in milestones if m.get("due_on")}

    reaberturas = defaultdict(list)
    eventos_label = defaultdict(list)
    for e in eventos:
        n, quando = e["issue"]["number"], data_hora(e["created_at"])
        if e["event"] == "reopened":
            reaberturas[n].append(quando)
        elif e["event"] in ("labeled", "unlabeled") and e["label"]["name"] == LABEL_RETRABALHO:
            eventos_label[n].append((quando, e["event"] == "labeled"))

    registros = []
    for i in sorted(issues, key=lambda i: i["number"]):
        criada = data_hora(i["createdAt"])
        ms = (i.get("milestone") or {}).get("title", "")
        tem_label = any(l["name"] == LABEL_RETRABALHO for l in i["labels"])
        registros.append({
            "numero": i["number"], "titulo": i["title"], "milestone": ms, "prazo": prazos.get(ms),
            "responsaveis": " ".join(a["login"] for a in i["assignees"]),
            "criada": criada, "fechada": data_hora(i.get("closedAt")) if i["state"] == "CLOSED" else None,
            "descartada": i["state"] == "CLOSED" and i.get("stateReason") == "NOT_PLANNED",
            "estimativa": numero(secao(i["body"], "Estimativa (horas)")),
            "horas": registros_horas(i["body"], criada.year),
            "reaberturas": reaberturas[i["number"]],
            # sem eventos (ex.: label anterior ao histórico disponível), vale a label atual desde a criação
            "label_retrabalho": sorted(eventos_label[i["number"]]) or ([(criada, True)] if tem_label else []),
        })

    linhas_prs = []
    for p in sorted(prs, key=lambda p: p["number"]):
        criado, merge = data_hora(p["createdAt"]), data_hora(p["mergedAt"])
        aprov = sorted(data_hora(r["submittedAt"]) for r in p["reviews"]
                       if r["state"] == "APPROVED" and r["author"]["login"] != p["author"]["login"])
        primeira = aprov[0] if aprov else None
        antes = bool(primeira and primeira <= merge)
        linhas_prs.append({
            "numero": p["number"], "autor": p["author"]["login"], "criado": criado, "mergeado": merge,
            "primeira_aprovacao": primeira, "antes_do_merge": antes,
            "no_prazo": antes and primeira - criado <= PRAZO_REVISAO,
        })
    return registros, linhas_prs


def concluida_ate(r, t):
    return r["fechada"] is not None and r["fechada"] <= t and not r["descartada"]


def retrabalho_ate(r, t):
    if any(q <= t for q in r["reaberturas"]):
        return True
    estado = False
    for quando, colocada in r["label_retrabalho"]:
        if quando <= t:
            estado = colocada
    return estado


def indicadores_em(t, registros, prs):
    dia = t.date().isoformat()
    ind = []

    def add(categoria, indicador, valor, unidade, detalhe):
        ind.append({"data_referencia": dia, "categoria": categoria, "indicador": indicador,
                    "valor": "" if valor is None else valor, "unidade": unidade, "detalhe": detalhe})

    mergeados = [p for p in prs if p["mergeado"] <= t]
    no_prazo = sum(p["no_prazo"] for p in mergeados)
    antes = sum(p["antes_do_merge"] for p in mergeados)
    add("Desempenho dos processos", "PRs revisados no prazo", pct(no_prazo, len(mergeados)), "%",
        f"{no_prazo} de {len(mergeados)} PRs mergeados aprovados antes do merge e em até 48 h")
    add("Desempenho dos processos", "PRs aprovados antes do merge", pct(antes, len(mergeados)), "%",
        f"{antes} de {len(mergeados)} PRs mergeados")

    concluidas = [r for r in registros if concluida_ate(r, t)]
    retrab = [r for r in concluidas if retrabalho_ate(r, t)]
    add("Desempenho dos processos", "Retrabalho (issues)", pct(len(retrab), len(concluidas)), "%",
        f"{len(retrab)} de {len(concluidas)} issues concluídas com a label {LABEL_RETRABALHO} ou reabertas")

    def horas_ate(r):
        return sum(h for d, _, h in r["horas"] if d <= t.date())

    h_retrab = sum(horas_ate(r) for r in retrab)
    h_total = sum(horas_ate(r) for r in concluidas)
    add("Desempenho dos processos", "Retrabalho (horas)", pct(h_retrab, h_total), "%",
        f"{h_retrab:g} h de {h_total:g} h reais registradas em issues concluídas")

    por_ms = defaultdict(list)
    for r in registros:
        if r["milestone"] and r["criada"] <= t and not (r["descartada"] and r["fechada"] <= t):
            por_ms[r["milestone"]].append(r)
    for ms in sorted(por_ms, key=lambda m: por_ms[m][0]["prazo"] or date.max):
        lista = por_ms[ms]
        feitas = sum(concluida_ate(r, t) for r in lista)
        prazo = lista[0]["prazo"]
        add("Calendário e progresso", f"Conclusão de issues — {ms}", pct(feitas, len(lista)), "%",
            f"{feitas} de {len(lista)} issues concluídas (prazo {prazo.strftime('%d/%m') if prazo else '-'})")

    com_prazo = [r for r in concluidas if r["prazo"]]
    if com_prazo:
        desvios = [(r["fechada"].date() - r["prazo"]).days for r in com_prazo]
        add("Calendário e progresso", "Desvio de prazo médio", round(sum(desvios) / len(desvios), 1), "dias",
            f"{sum(d > 0 for d in desvios)} de {len(desvios)} issues concluídas depois do prazo do milestone "
            "(negativo = adiantado)")

    pares = [(r["estimativa"], horas_ate(r)) for r in concluidas if r["estimativa"] and horas_ate(r)]
    est, real = sum(e for e, _ in pares), sum(h for _, h in pares)
    add("Recursos e custos", "Esforço real / estimado", round(real / est, 2) if est else None, "razão",
        f"{real:g} h reais / {est:g} h estimadas em {len(pares)} issues com os dois registros")
    add("Recursos e custos", "Issues concluídas sem horas reais", sum(not horas_ate(r) for r in concluidas),
        "issues", f"de {len(concluidas)} issues concluídas")

    por_pessoa = defaultdict(float)
    for r in registros:
        for d, pessoa, h in r["horas"]:
            if d <= t.date():
                por_pessoa[pessoa] += h
    total = sum(por_pessoa.values())
    for pessoa in sorted(por_pessoa):
        add("Recursos e custos", f"Distribuição de esforço — {pessoa}", pct(por_pessoa[pessoa], total), "%",
            f"{por_pessoa[pessoa]:g} h de {total:g} h registradas")
    return ind


def datas_de_referencia(inicio, agora):
    domingo = inicio.date() + timedelta(days=(6 - inicio.weekday()) % 7)
    datas = []
    while domingo < agora.date():
        datas.append(datetime.combine(domingo, time(23, 59, 59), FUSO))
        domingo += timedelta(days=7)
    return datas + [agora]


def main():
    agora = datetime.now(FUSO)
    os.makedirs(PASTA, exist_ok=True)
    registros, prs = coletar()

    def fmt(dt):
        return dt.isoformat(timespec="minutes") if dt else ""

    escrever_csv("issues.csv",
                 ["issue", "titulo", "milestone", "responsaveis", "situacao", "criada_em", "fechada_em",
                  "prazo_milestone", "desvio_prazo_dias", "estimativa_h", "horas_reais_h", "retrabalho"],
                 [{"issue": r["numero"], "titulo": r["titulo"], "milestone": r["milestone"],
                   "responsaveis": r["responsaveis"],
                   "situacao": "descartada" if r["descartada"] else ("concluida" if r["fechada"] else "aberta"),
                   "criada_em": fmt(r["criada"]), "fechada_em": fmt(r["fechada"]),
                   "prazo_milestone": r["prazo"].isoformat() if r["prazo"] else "",
                   "desvio_prazo_dias": (r["fechada"].date() - r["prazo"]).days
                   if concluida_ate(r, agora) and r["prazo"] else "",
                   "estimativa_h": r["estimativa"] if r["estimativa"] is not None else "",
                   "horas_reais_h": sum(h for _, _, h in r["horas"]) if r["horas"] else "",
                   "retrabalho": "sim" if retrabalho_ate(r, agora) else "nao"} for r in registros])
    escrever_csv("horas.csv", ["issue", "data", "pessoa", "horas"],
                 [{"issue": r["numero"], "data": d.isoformat(), "pessoa": p, "horas": h}
                  for r in registros for d, p, h in r["horas"]])
    escrever_csv("prs.csv",
                 ["pr", "autor", "criado_em", "mergeado_em", "primeira_aprovacao",
                  "aprovado_antes_do_merge", "revisado_no_prazo"],
                 [{"pr": p["numero"], "autor": p["autor"], "criado_em": fmt(p["criado"]),
                   "mergeado_em": fmt(p["mergeado"]), "primeira_aprovacao": fmt(p["primeira_aprovacao"]),
                   "aprovado_antes_do_merge": "sim" if p["antes_do_merge"] else "nao",
                   "revisado_no_prazo": "sim" if p["no_prazo"] else "nao"} for p in prs])

    inicio = min(r["criada"] for r in registros)
    historico = [indicadores_em(t, registros, prs) for t in datas_de_referencia(inicio, agora)]
    escrever_csv("indicadores.csv", list(historico[-1][0]), [l for ind in historico for l in ind])

    gerar_pagina(historico, agora)
    print(f"{len(registros)} issues, {len(prs)} PRs, {len(historico)} datas de referência "
          f"({historico[0][0]['data_referencia']} a {historico[-1][0]['data_referencia']})")


def formatar(valor, unidade):
    if valor == "":
        return "—"
    if unidade == "%":
        return f"{valor:.1f}%".replace(".", ",")
    if unidade == "razão":
        return f"{valor:.2f}".replace(".", ",")
    if isinstance(valor, float):
        return f"{valor:.1f} {unidade}".replace(".", ",")
    return f"{valor} {unidade}"


def gerar_pagina(historico, agora):
    atual = historico[-1]
    linhas = [
        "# Indicadores PSM/CID (coleta automática)",
        "",
        "<!-- Página gerada por scripts/coletar_metricas_psm.py. Não edite à mão. -->",
        "",
        f"Última coleta: **{agora.strftime('%d/%m/%Y')}**. Os valores são calculados a partir das issues, "
        "milestones e pull requests do repositório. A definição dos indicadores e as decisões de gestão "
        "estão em [Métricas PSM/CID](metricas.md).",
        "",
    ]
    categoria = None
    for i in atual:
        if i["categoria"] != categoria:
            categoria = i["categoria"]
            linhas += ["", f"## {categoria}", "", "| Indicador | Valor | Detalhe |", "|---|---|---|"]
        linhas.append(f"| {i['indicador']} | {formatar(i['valor'], i['unidade'])} | {i['detalhe']} |")

    linhas += ["", "## Evolução semanal", "",
               "Valores ao fim de cada domingo (23h59) e na data da última coleta.", "",
               "| Data | " + " | ".join(INDICADORES_EVOLUCAO) + " |",
               "|---|" + "---|" * len(INDICADORES_EVOLUCAO)]
    for ind in historico:
        valores = {i["indicador"]: formatar(i["valor"], i["unidade"]) for i in ind}
        dia = date.fromisoformat(ind[0]["data_referencia"]).strftime("%d/%m")
        linhas.append(f"| {dia} | " + " | ".join(valores.get(n, "—") for n in INDICADORES_EVOLUCAO) + " |")

    linhas += [
        "",
        "## Dados brutos",
        "",
        "- [issues.csv](evidencias/issues.csv): estimativa, horas reais e desvio de prazo por issue",
        "- [horas.csv](evidencias/horas.csv): registros de horas reais por pessoa",
        "- [prs.csv](evidencias/prs.csv): revisão de cada pull request",
        "- [indicadores.csv](evidencias/indicadores.csv): indicadores em cada data de referência",
        "",
    ]
    with open(PAGINA, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))


if __name__ == "__main__":
    main()
