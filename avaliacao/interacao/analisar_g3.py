#!/usr/bin/env python3
"""Calcula M6 a M9 a partir do observacoes.csv, seguindo a Fase 2 (secao 4.4).

Uso:
  python3 avaliacao/interacao/analisar_g3.py OBSERVACOES.csv \
      --plano avaliacao/interacao/plano-cobertura.csv --saida PASTA

Le apenas linhas com fase_coleta=formal. So o estado_observacao=valida entra no
denominador; invalidas e nao_coletadas sao contadas a parte. Sem planejado informado,
a cobertura fica "nao informada" e nenhuma hipotese e dada como sustentada.
Nao usa dados pessoais: le somente as colunas do modelo de registro.
"""
import argparse
import csv
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

OBRIGATORIAS = ["metrica", "fase_coleta", "dispositivo", "modalidade",
                "tarefa_ponto", "estado_observacao", "resultado"]
# limites inferiores (%) das notas 1, 2 e 3; None = nao se aplica
FAIXAS = {"M6": (80, 90, 100), "M7": (90, 95, 100), "M9": (90, 95, 100)}
NOMES = {"M6": "Sucesso no primeiro uso", "M7": "Sucesso nas tarefas de controle",
         "M8": "Protecao contra perda", "M9": "Compreensao da interface"}
HIPOTESE = {"M6": "H6", "M7": "H7", "M8": "H8", "M9": "H9"}


def nota(metrica, frac):
    p = frac * 100  # razao exata, sem arredondar
    if metrica == "M8":
        return 3 if p == 100 else 0
    l1, l2, l3 = FAIXAS[metrica]
    return 3 if p >= l3 else 2 if p >= l2 else 1 if p >= l1 else 0


def chave(metrica, linha):
    d, m, t = linha["dispositivo"], linha["modalidade"], linha["tarefa_ponto"]
    if metrica == "M6":
        return (d, m, "")
    if metrica == "M8":
        return (d, m, "")
    return (d, "", t)  # M7 e M9: por tarefa/ponto e dispositivo


def ler_plano(caminho):
    plano = {}
    if not caminho:
        return plano
    with open(caminho, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("planejado", "").strip():
                continue
            m = r["metrica"].strip()
            k = (m, r["dispositivo"].strip(),
                 r.get("modalidade", "").strip() if m in ("M6", "M8") else "",
                 r.get("tarefa_ponto", "").strip() if m in ("M7", "M9") else "")
            plano[k] = int(r["planejado"])
    return plano


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("observacoes")
    ap.add_argument("--plano")
    ap.add_argument("--saida", default=".")
    a = ap.parse_args()

    with open(a.observacoes, encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f)
        faltam = [c for c in OBRIGATORIAS if c not in (leitor.fieldnames or [])]
        if faltam:
            sys.exit(f"Colunas ausentes: {faltam}")
        linhas = [r for r in leitor if r["fase_coleta"].strip() == "formal"]

    avisos = []
    dados = defaultdict(lambda: {"valida": 0, "sucesso": 0, "invalida": 0, "nao_coletada": 0})
    for i, r in enumerate(linhas, start=2):
        m = r["metrica"].strip()
        if m not in NOMES:
            avisos.append(f"linha {i}: metrica desconhecida '{m}'")
            continue
        est, res = r["estado_observacao"].strip(), r["resultado"].strip()
        d = dados[(m,) + chave(m, r)]
        if est == "valida":
            if res not in ("sucesso", "insucesso"):
                avisos.append(f"linha {i}: valida sem resultado sucesso/insucesso")
                continue
            if m == "M9" and res == "sucesso" and not (
                    r.get("estado_correto", "").strip() == "sim" and r.get("acao_correta", "").strip() == "sim"):
                avisos.append(f"linha {i}: M9 'sucesso' sem estado_correto e acao_correta = sim")
            d["valida"] += 1
            d["sucesso"] += res == "sucesso"
        elif est in ("invalida", "nao_coletada"):
            d[est] += 1
            if not r.get("motivo", "").strip():
                avisos.append(f"linha {i}: {est} sem motivo")
        else:
            avisos.append(f"linha {i}: estado_observacao invalido '{est}'")

    plano = ler_plano(a.plano)
    for k in plano:  # recortes planejados sem nenhuma linha tambem aparecem
        dados[k]
    res = []
    for k in sorted(dados):
        m, disp, mod, tp = k
        d = dados[k]
        pl = plano.get(k)
        n, s = d["valida"], d["sucesso"]
        if n == 0:
            pct, nt, estado = "", "", "Nao avaliado"
        else:
            fr = Fraction(s, n)
            pct, nt, estado = f"{float(fr * 100):.2f}", nota(m, fr), "Medido"
        cob = "nao informada" if pl is None else ("completa" if n >= pl else "parcial")
        res.append({"metrica": m, "dispositivo": disp, "modalidade": mod, "tarefa_ponto": tp,
                    "sucessos": s, "validas": n, "percentual": pct, "nota": nt,
                    "invalidas": d["invalida"], "nao_coletadas": d["nao_coletada"],
                    "planejado": "" if pl is None else pl, "cobertura": cob, "estado": estado})

    out = Path(a.saida)
    out.mkdir(parents=True, exist_ok=True)
    cab = list(res[0].keys()) if res else OBRIGATORIAS
    with open(out / "resultados-g3.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cab)
        w.writeheader()
        w.writerows(res)

    # julgamento operacional das hipoteses (Fase 2, 4.4, item 5)
    julg = []
    for m in ("M6", "M7", "M8", "M9"):
        rs = [r for r in res if r["metrica"] == m]
        medidos = [r for r in rs if r["estado"] == "Medido"]
        if not medidos:
            st = "Nao avaliada (sem observacoes validas)"
        elif any(r["nota"] == 0 for r in medidos):
            st = "Contrariada nas condicoes avaliadas (ha recorte com nota 0)"
        elif any(r["cobertura"] != "completa" for r in rs) or len(medidos) != len(rs):
            st = "Inconclusiva (cobertura parcial ou planejado nao informado)"
        elif m == "M8" and all(r["nota"] == 3 for r in medidos):
            st = "Sustentada operacionalmente (100% de protecao em todos os conjuntos)"
        elif m != "M8" and all(r["nota"] >= 1 for r in medidos):
            st = "Sustentada operacionalmente (todos os recortes com nota >= 1)"
        else:
            st = "Inconclusiva"
        julg.append((HIPOTESE[m], m, st))

    md = ["| Metrica | Dispositivo | Modalidade | Tarefa/ponto | Sucessos/validas | % | Nota | Cobertura (planejado) | Invalidas | Nao coletadas |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        pct = r["percentual"].replace(".", ",") + "%" if r["percentual"] else "-"
        nt = r["nota"] if r["nota"] != "" else "Nao avaliado"
        cob = r["cobertura"] + ("" if r["planejado"] == "" else f" ({r['planejado']})")
        md.append(f"| {r['metrica']} | {r['dispositivo']} | {r['modalidade'] or '-'} | {r['tarefa_ponto'] or '-'} | "
                  f"{r['sucessos']}/{r['validas']} | {pct} | {nt} | {cob} | {r['invalidas']} | {r['nao_coletadas']} |")
    md += ["", "| Hipotese | Metrica | Estado |", "|---|---|---|"]
    md += [f"| {h} | {m} | {s} |" for h, m, s in julg]
    (out / "resumo-g3.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    if avisos:
        print("\nAVISOS (corrigir a ficha antes de usar):")
        print("\n".join("- " + x for x in avisos))
    print(f"\nGravado em {out}/resultados-g3.csv e {out}/resumo-g3.md")


if __name__ == "__main__":
    main()