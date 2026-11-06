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
import unicodedata
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

import graficos_psm as g

PASTA = "docs/gestao/evidencias"
PAGINA = "docs/gestao/indicadores.md"
FUSO = ZoneInfo("America/Sao_Paulo")
PRAZO_REVISAO = timedelta(hours=48)
LABEL_RETRABALHO = "correcao"
# indicador, título do gráfico e linha de referência (só os limiares já adotados em metricas.md)
PAINEIS_EVOLUCAO = [
    ("PRs revisados no prazo", "I1 — PRs revisados no prazo", {"referencia": (100, "meta")}),
    ("PRs aprovados antes do merge", "I2 — PRs aprovados antes do merge", {"referencia": (100, "meta")}),
    ("Retrabalho (issues)", "I3 — Retrabalho (issues)", {}),
    ("Retrabalho (horas)", "I4 — Retrabalho (horas)", {}),
    ("Desvio de prazo médio", "I6 — Desvio de prazo médio (dias)", {"referencia": (0, "prazo")}),
    ("Esforço real / estimado", "I8 — Esforço real / estimado", {"faixa": (0.9, 1.1, "0,9 a 1,1")}),
    ("Issues concluídas sem horas reais", "I9 — Issues concluídas sem horas reais", {"inteiro": True}),
]
INDICADORES_EVOLUCAO = [p[0] for p in PAINEIS_EVOLUCAO]


def gh(*args):
    saida = subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout
    return json.loads(saida) if saida.strip() else []


def data_hora(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(FUSO) if iso else None


def secao(corpo, titulo):
    m = re.search(rf"^###\s*{re.escape(titulo)}\s*$(.*?)(?=^###|\Z)", corpo or "", re.M | re.S)
    return m.group(1).strip() if m else ""


TRACO = r"\s*(?:—|–|−|-{1,2})\s*"
DURACAO = r"(\d+(?:[.,]\d+)?)\s*(?:(?:horas?|hrs?|hs|h)(?:\s*(\d{1,2})\s*(?:min)?)?|(min(?:utos)?))"
REGISTRO_HORAS = re.compile(rf"(\d{{1,2}})/(\d{{1,2}})(?:/(\d{{4}}|\d{{2}}))?{TRACO}(.+?){TRACO}{DURACAO}(?![\wà-ú])",
                            re.I)
ESTIMATIVA = re.compile(r"(\d+(?:[.,]\d+)?)\s*h?", re.I)
avisos = []


def horas(numero, minutos, so_minutos):
    valor = float(numero.replace(",", "."))
    return round(valor / 60 if so_minutos else valor + int(minutos or 0) / 60, 2)


def linhas_uteis(texto):
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    return [l.strip().lstrip("-*• ").strip() for l in texto.splitlines() if l.strip().lstrip("-*• ").strip()]


def estimativa(corpo, n):
    texto = " ".join(linhas_uteis(secao(corpo, "Estimativa (horas)")))
    if not texto:
        return None
    m = ESTIMATIVA.fullmatch(texto)
    if m:
        return float(m.group(1).replace(",", "."))
    avisos.append(f"#{n}: estimativa não reconhecida (use só o total, ex.: 5 ou 5 h): {texto}")
    return None


def registros_horas(corpo, criada, n):
    regs = []
    for linha in linhas_uteis(secao(corpo, "Horas reais")):
        m = REGISTRO_HORAS.search(linha)
        if not m:
            avisos.append(f"#{n}: linha de horas reais não reconhecida: {linha}")
            continue
        dia, mes, ano, pessoa = m.groups()[:4]
        try:
            if ano:
                d = date(int(ano) + (2000 if len(ano) == 2 else 0), int(mes), int(dia))
            else:
                d = date(criada.year, int(mes), int(dia))
                if d < criada.date() - timedelta(days=60):
                    d = d.replace(year=d.year + 1)
        except ValueError:
            avisos.append(f"#{n}: data inválida em horas reais: {linha}")
            continue
        regs.append((d, " ".join(pessoa.split()), horas(*m.groups()[4:])))
    return regs


def chave_pessoa(nome):
    sem_acento = "".join(c for c in unicodedata.normalize("NFKD", nome) if not unicodedata.combining(c))
    return " ".join(sem_acento.casefold().split())


def unificar_nomes(registros):
    grafias = defaultdict(Counter)
    for r in registros:
        for _, pessoa, _ in r["horas"]:
            grafias[chave_pessoa(pessoa)][pessoa] += 1
    nome = {k: c.most_common(1)[0][0] for k, c in grafias.items()}
    for r in registros:
        r["horas"] = [(d, nome[chave_pessoa(p)], h) for d, p, h in r["horas"]]


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
    estados = defaultdict(list)
    eventos_label = defaultdict(list)
    for e in eventos:
        n, quando = e["issue"]["number"], data_hora(e["created_at"])
        if e["event"] == "reopened":
            reaberturas[n].append(quando)
            estados[n].append((quando, "aberta"))
        elif e["event"] == "closed":
            estados[n].append((quando, situacao_fechada(e.get("state_reason"))))
        elif e["event"] in ("labeled", "unlabeled") and e["label"]["name"] == LABEL_RETRABALHO:
            eventos_label[n].append((quando, e["event"] == "labeled"))

    registros = []
    for i in sorted(issues, key=lambda i: i["number"]):
        criada = data_hora(i["createdAt"])
        ms = (i.get("milestone") or {}).get("title", "")
        tem_label = any(l["name"] == LABEL_RETRABALHO for l in i["labels"])
        n = i["number"]
        # sem eventos (histórico indisponível), vale o estado e a label atuais
        fechamento = [(data_hora(i["closedAt"]), situacao_fechada(i.get("stateReason")))] \
            if i["state"] == "CLOSED" and i.get("closedAt") else []
        registros.append({
            "numero": n, "titulo": i["title"], "milestone": ms, "prazo": prazos.get(ms),
            "responsaveis": " ".join(a["login"] for a in i["assignees"]),
            "criada": criada, "estados": sorted(estados[n]) or fechamento,
            "estimativa": estimativa(i["body"], n),
            "horas": registros_horas(i["body"], criada, n),
            "reaberturas": reaberturas[n],
            "label_retrabalho": sorted(eventos_label[n]) or ([(criada, True)] if tem_label else []),
        })
    unificar_nomes(registros)

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


def situacao_fechada(motivo):
    return "descartada" if (motivo or "").lower() in ("not_planned", "duplicate") else "concluida"


def situacao_em(r, t):
    situacao, quando = "aberta", None
    for q, s in r["estados"]:
        if q > t:
            break
        situacao, quando = s, q
    return situacao, quando


def concluida_ate(r, t):
    return situacao_em(r, t)[0] == "concluida"


def fechamento_ate(r, t):
    situacao, quando = situacao_em(r, t)
    return quando if situacao == "concluida" else None


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
        if r["milestone"] and r["criada"] <= t and situacao_em(r, t)[0] != "descartada":
            por_ms[r["milestone"]].append(r)
    for ms in sorted(por_ms, key=lambda m: por_ms[m][0]["prazo"] or date.max):
        lista = por_ms[ms]
        feitas = sum(concluida_ate(r, t) for r in lista)
        prazo = lista[0]["prazo"]
        add("Calendário e progresso", f"Conclusão de issues — {ms}", pct(feitas, len(lista)), "%",
            f"{feitas} de {len(lista)} issues concluídas (prazo {prazo.strftime('%d/%m') if prazo else '-'})")

    com_prazo = [r for r in concluidas if r["prazo"]]
    if com_prazo:
        desvios = [(fechamento_ate(r, t).date() - r["prazo"]).days for r in com_prazo]
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

    linhas_issues = []
    for r in registros:
        situacao, fechada = situacao_em(r, agora)
        linhas_issues.append({
            "issue": r["numero"], "titulo": r["titulo"], "milestone": r["milestone"],
            "responsaveis": r["responsaveis"], "situacao": situacao,
            "criada_em": fmt(r["criada"]), "fechada_em": fmt(fechada), "reaberturas": len(r["reaberturas"]),
            "prazo_milestone": r["prazo"].isoformat() if r["prazo"] else "",
            "desvio_prazo_dias": (fechada.date() - r["prazo"]).days
            if situacao == "concluida" and r["prazo"] else "",
            "estimativa_h": r["estimativa"] if r["estimativa"] is not None else "",
            "horas_reais_h": round(sum(h for _, _, h in r["horas"]), 2) if r["horas"] else "",
            "retrabalho": "sim" if retrabalho_ate(r, agora) else "nao"})
    escrever_csv("issues.csv", list(linhas_issues[0]), linhas_issues)
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

    gerar_pagina(historico, agora, montar_graficos(registros, prs, agora))
    for aviso in avisos:
        print(f"AVISO: {aviso}")
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


def plural(n, palavra):
    return f"{n} {palavra}" + ("" if n == 1 else "s")


def montar_graficos(registros, prs, agora):
    """Gráficos por item medido (PR, issue ou integrante), como decidido na ata 04."""
    def dh(dt):
        return dt.strftime("%d/%m %H:%M")

    graficos = defaultdict(list)

    itens = []
    for p in prs:
        aprovacao = p["primeira_aprovacao"]
        if aprovacao:
            espera = (aprovacao - p["criado"]).total_seconds() / 3600
            if p["no_prazo"]:
                classe, situacao = "g-azul", "Aprovado antes do merge, em até 48 h"
            elif p["antes_do_merge"]:
                classe, situacao = "g-verde", "Aprovado antes do merge, depois de 48 h"
            else:
                classe, situacao = "g-laranja", "Aprovado só depois do merge"
            texto_aprovacao = f"1ª aprovação: {dh(aprovacao)} ({g.num(espera)} h após a abertura)"
        else:
            espera, classe, situacao = None, "g-laranja", "Sem aprovação de outra pessoa"
            texto_aprovacao = "1ª aprovação: nenhuma"
        itens.append({"rotulo": f"#{p['numero']}", "valor": espera, "classe": classe,
                      "dica": f"PR #{p['numero']} — {p['autor']}\nAberto: {dh(p['criado'])}\n"
                              f"Mergeado: {dh(p['mergeado'])}\n{texto_aprovacao}\n{situacao}"})
    if itens:
        graficos["Desempenho dos processos"].append((
            "I1 e I2 — Tempo até a aprovação de cada PR",
            g.colunas(itens, "horas entre a abertura e a 1ª aprovação",
                      "Horas até a primeira aprovação de cada PR mergeado",
                      "Cada coluna é um PR mergeado. A altura é o tempo entre a abertura e a primeira aprovação "
                      "de outra pessoa. I1 conta só as colunas azuis, e I2 conta as azuis e as verdes. "
                      "Passe o mouse sobre a coluna para ver as datas.",
                      [("g-azul", "aprovado antes do merge, em até 48 h"),
                       ("g-verde", "aprovado antes do merge, depois de 48 h"),
                       ("g-laranja", "aprovado só depois do merge (× = sem aprovação)")],
                      referencia=(PRAZO_REVISAO.total_seconds() / 3600, "limite de 48 h"))))

    concluidas = []
    for r in registros:
        situacao, fechada = situacao_em(r, agora)
        if situacao == "concluida":
            concluidas.append((r, fechada))

    itens = []
    for r, _ in concluidas:
        h = round(sum(x for _, _, x in r["horas"]), 2)
        retrabalho = retrabalho_ate(r, agora)
        motivo = "reaberta" if r["reaberturas"] else f"label {LABEL_RETRABALHO}"
        itens.append({"rotulo": f"#{r['numero']}", "valor": h or None,
                      "classe": "g-laranja" if retrabalho else "g-cinza",
                      "dica": f"#{r['numero']} {r['titulo']}\n"
                              + (f"{g.num(h)} h reais" if h else "Sem horas reais registradas")
                              + (f"\nRetrabalho ({motivo})" if retrabalho else "")})
    if itens:
        graficos["Desempenho dos processos"].append((
            "I3 e I4 — Horas de cada issue concluída e retrabalho",
            g.colunas(itens, "horas reais", "Horas reais de cada issue concluída, com o retrabalho em destaque",
                      "Cada coluna é uma issue concluída, com as horas reais registradas. I3 é a fração de colunas "
                      "laranja, e I4 é a fração das horas que elas somam.",
                      [("g-laranja", f"retrabalho (label {LABEL_RETRABALHO} ou reaberta)"),
                       ("g-cinza", "demais issues concluídas (× = sem horas reais)")])))

    por_ms = defaultdict(list)
    for r in registros:
        if r["milestone"] and situacao_em(r, agora)[0] != "descartada":
            por_ms[r["milestone"]].append(r)
    grupos = []
    for ms in sorted(por_ms, key=lambda m: por_ms[m][0]["prazo"] or date.max):
        lista, prazo, feitas, issues = por_ms[ms], por_ms[ms][0]["prazo"], 0, []
        for r in lista:
            situacao, fechada = situacao_em(r, agora)
            concluida = situacao == "concluida"
            feitas += concluida
            estado = f"Concluída em {fechada.strftime('%d/%m')}" if concluida else "Aberta"
            issues.append((r["numero"], concluida, f"#{r['numero']} {r['titulo']}\n{estado}"))
        grupos.append({"titulo": ms, "subtitulo": f"prazo {prazo.strftime('%d/%m')}" if prazo else "sem prazo",
                       "resumo": f"{feitas} de {len(lista)} · {g.num(pct(feitas, len(lista)))}%", "issues": issues})
    if grupos:
        graficos["Calendário e progresso"].append((
            "I5 — Issues de cada milestone",
            g.grade_issues(grupos, "Issues de cada milestone, concluídas e abertas",
                           "Cada quadrado é uma issue do milestone, com o número dela. As descartadas ficam de fora. "
                           "I5 é a fração de quadrados cheios.",
                           [("g-azul", "concluída"), ("g-aberta", "aberta")])))

    pontos = []
    for r, fechada in concluidas:
        if not r["prazo"]:
            continue
        desvio = (fechada.date() - r["prazo"]).days
        if desvio < 0:
            classe, quando = "g-azul", f"{plural(-desvio, 'dia')} antes do prazo"
        elif desvio == 0:
            classe, quando = "g-cinza", "no dia do prazo"
        else:
            classe, quando = "g-laranja", f"{plural(desvio, 'dia')} depois do prazo"
        pontos.append({"valor": desvio, "classe": classe,
                       "dica": f"#{r['numero']} {r['titulo']}\n{r['milestone']}, prazo {r['prazo'].strftime('%d/%m')}"
                               f"\nFechada em {fechada.strftime('%d/%m')}, {quando}"})
    if pontos:
        graficos["Calendário e progresso"].append((
            "I6 — Desvio de prazo de cada issue concluída",
            g.pontos_empilhados(pontos, "dias entre o fechamento da issue e o prazo do milestone",
                                "Desvio de prazo de cada issue concluída, em dias",
                                "Cada ponto é uma issue concluída. Issues com o mesmo desvio ficam empilhadas. "
                                "I6 é a média desses valores, e a média não mostra quantas issues fecharam no "
                                "próprio dia do prazo.",
                                [("g-azul", "antes do prazo"), ("g-cinza", "no dia do prazo"),
                                 ("g-laranja", "depois do prazo")])))

    por_pessoa = defaultdict(lambda: [0.0, 0])
    for r in registros:
        for _, pessoa, h in r["horas"]:
            por_pessoa[pessoa][0] += h
            por_pessoa[pessoa][1] += 1
    total = sum(h for h, _ in por_pessoa.values())
    if total:
        media = total / len(por_pessoa)
        itens = [{"rotulo": pessoa, "valor": h, "texto_valor": f"{g.num(h)} h · {g.num(pct(h, total))}%",
                  "dica": f"{pessoa}: {g.num(h)} h em {plural(n, 'registro')}, {g.num(pct(h, total))}% do total"}
                 for pessoa, (h, n) in sorted(por_pessoa.items(), key=lambda kv: (-kv[1][0], kv[0]))]
        graficos["Recursos e custos"].append((
            "I7 — Horas reais de cada integrante",
            g.barras_horizontais(itens, "Horas reais registradas por integrante",
                                 "Cada barra é a soma das horas reais que o integrante registrou nas issues, com a "
                                 "participação no total. A linha tracejada é a média do grupo.",
                                 (media, f"média {g.num(media)} h"))))

    pontos = []
    for r, _ in concluidas:
        real = round(sum(h for _, _, h in r["horas"]), 2)
        if r["estimativa"] and real:
            pontos.append({"x": r["estimativa"], "y": real,
                           "dica": f"#{r['numero']} {r['titulo']}: {g.num(r['estimativa'])} h estimadas, "
                                   f"{g.num(real)} h reais"})
    if pontos:
        graficos["Recursos e custos"].append((
            "I8 — Horas estimadas e reais de cada issue concluída",
            g.dispersao(pontos, "horas estimadas", "horas reais", "Horas estimadas e reais de cada issue concluída",
                        "Cada ponto é uma issue concluída com estimativa e horas reais (×n = n issues com os "
                        "mesmos valores). Na linha tracejada a estimativa foi exata. I8 divide a soma das horas "
                        "reais pela soma das estimadas, então as issues maiores pesam mais.")))
    return graficos


def valor_curto(valor, unidade):
    if unidade == "%":
        return f"{g.num(valor)}%"
    if unidade == "razão":
        return f"{valor:.2f}".replace(".", ",")
    return g.num(valor)


def graficos_evolucao(historico):
    paineis = []
    for indicador, titulo, opcoes in PAINEIS_EVOLUCAO:
        pontos, unidade = [], ""
        for ind in historico:
            dia = date.fromisoformat(ind[0]["data_referencia"]).strftime("%d/%m")
            item = next((i for i in ind if i["indicador"] == indicador), None)
            if item is None or item["valor"] == "":
                pontos.append((dia, None, f"{dia}: sem valor"))
                continue
            unidade = item["unidade"]
            pontos.append((dia, item["valor"], f"{dia}: {formatar(item['valor'], unidade)}\n{item['detalhe']}"))
        valores = [v for _, v, _ in pontos if v is not None]
        if not valores:
            continue
        if unidade == "%":
            dominio = (0, 100)
        elif unidade == "razão":
            dominio = (min(valores + [0.8]), max(valores + [1.2]))
        else:
            dominio = (min(valores + [0]), max(valores + [1]))
        paineis.append(g.painel_linha(titulo, pontos, lambda v, u=unidade: valor_curto(v, u), dominio, **opcoes))
    return g.paineis(paineis, "Valor de cada indicador ao fim de cada domingo e na data da última coleta. A linha "
                              "tracejada marca a meta adotada (I1 e I2) ou o prazo (I6), e a faixa em I8 é o intervalo "
                              "de 0,90 a 1,10 do critério de decisão. I9 tem meta 0. I3, I4 e I6 ainda não têm limiar "
                              "definido pela equipe.")


def gerar_pagina(historico, agora, graficos):
    atual = historico[-1]
    linhas = [
        "# Indicadores PSM/CID (coleta automática)",
        "",
        "<!-- Página gerada por scripts/coletar_metricas_psm.py. Não edite à mão. -->",
        "",
        f"Última coleta: **{agora.strftime('%d/%m/%Y')}**. Os valores são calculados a partir das issues, "
        "milestones e pull requests do repositório. A definição dos indicadores e as decisões de gestão "
        "estão em [Métricas PSM/CID](metricas.md). Cada tabela vem acompanhada de gráficos que mostram os itens "
        "medidos um a um (PR, issue ou integrante). Passe o mouse sobre um item para ver os dados dele.",
        "",
    ]
    categorias = defaultdict(list)
    for i in atual:
        categorias[i["categoria"]].append(i)
    for categoria, itens in categorias.items():
        linhas += ["", f"## {categoria}", "", "| Indicador | Valor | Detalhe |", "|---|---|---|"]
        linhas += [f"| {i['indicador']} | {formatar(i['valor'], i['unidade'])} | {i['detalhe']} |" for i in itens]
        for titulo, html in graficos.get(categoria, []):
            linhas += ["", f"### {titulo}", "", html]

    linhas += ["", "## Evolução semanal", "",
               "Valores ao fim de cada domingo (23h59) e na data da última coleta.", "",
               graficos_evolucao(historico), "",
               "| Data | " + " | ".join(INDICADORES_EVOLUCAO) + " |",
               "|---|" + "---|" * len(INDICADORES_EVOLUCAO)]
    for ind in historico:
        valores = {i["indicador"]: formatar(i["valor"], i["unidade"]) for i in ind}
        dia = date.fromisoformat(ind[0]["data_referencia"]).strftime("%d/%m")
        linhas.append(f"| {dia} | " + " | ".join(valores.get(n, "—") for n in INDICADORES_EVOLUCAO) + " |")

    if avisos:
        linhas += ["", "## Registros a corrigir", "",
                   "Registros fora do formato esperado. Linhas não reconhecidas ficam fora dos indicadores.", ""]
        linhas += [f"- {a}" for a in avisos]

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
