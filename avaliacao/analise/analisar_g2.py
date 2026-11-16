#!/usr/bin/env python3
"""Análise de G2 (M2 a M5) a partir de uma rodada de coleta.

Uso:
    python3 avaliacao/analise/analisar_g2.py <pasta-da-rodada> [--saida <pasta>]

A pasta da rodada é a que o roteiro Playwright gera (`npm run coleta`) e contém um
CSV por cenário (m2-nome.csv, ..., m5-conta.csv) e o metadados.json.
Aplica as regras da Fase 2, seção 4.3, e o cálculo do P95 da Fase 3, seção 1.1.7:

  1. Cenário sem 30 tentativas medidas (aquecimento = não) -> "Não avaliado".
     Também "Não avaliado" quando alguma tentativa medida falhou na preparação
     (motivo "preparação: ..." em evidencias.jsonl): a falha ocorreu antes do
     clique, fora do intervalo medido, e é defeito do roteiro, não da aplicação.
  2. Qualquer erro ou expiração -> nota 0, com o motivo. Zero sucessos -> P95
     "não calculável" e nota 0.
  3. Com 30 sucessos, a nota é a faixa do P95 (sem arredondamento prévio).
  4. Nota da métrica = menor nota entre os cenários. Se algum cenário não foi
     avaliado, a cobertura é parcial e não há nota consolidada.
  5. H2 a H5: sustentada (todos os cenários com nota >= 1), contrariada (algum
     cenário com nota 0) ou inconclusiva (nenhum 0, mas algum não avaliado).

Saídas (em --saida, por padrão a própria pasta da rodada, subpasta `analise/`):
  resultados.csv   uma linha por cenário
  resumo.md        tabelas prontas para a Fase 4
  grafico-g2.svg   P95 de cada cenário em relação ao limite L_j
Só usa a biblioteca padrão.
"""
import argparse
import csv
import json
import math
import sys
from pathlib import Path

NIVEIS = {0: "Insatisfatório (0)", 1: "Aceitável (1)", 2: "Bom (2)", 3: "Excelente (3)"}
# Fase 2, seção 4.1: limites superiores (ms) de Excelente, Bom e Aceitável.
FAIXAS = {
    "M2": (500, 1000, 2000),
    "M3": (100, 300, 1000),
    "M4": (1000, 3000, 10000),
    "M5": (500, 1000, 2000),
}
LIMITE = {m: f[2] for m, f in FAIXAS.items()}
HIPOTESE = {"M2": ("H2", "Q2"), "M3": ("H3", "Q3"), "M4": ("H4", "Q4"), "M5": ("H5", "Q5")}
N_MEDIDAS = 30
COR = {0: "#c0392b", 1: "#e6a817", 2: "#2e86c1", 3: "#27ae60", None: "#999999"}


def nota_por_p95(metrica, p95):
    t3, t2, t1 = FAIXAS[metrica]
    if p95 <= t3:
        return 3
    if p95 <= t2:
        return 2
    if p95 <= t1:
        return 1
    return 0


def motivos_preparacao(rodada):
    """Ids de tentativas medidas que falharam antes do clique (defeito do roteiro)."""
    ev = rodada / "evidencias.jsonl"
    falhas = {}
    if not ev.exists():
        return falhas
    for l in open(ev, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        if (not d.get("aquecimento") and d.get("estado") != "sucesso"
                and str(d.get("motivo") or "").startswith("preparação:")):
            falhas.setdefault(d["cenario"], []).append(d["motivo"])
    return falhas


def analisar_cenario(caminho, meta, prep):
    linhas = list(csv.DictReader(open(caminho, encoding="utf-8")))
    if not linhas:
        raise ValueError(f"{caminho.name}: CSV vazio")
    metrica = linhas[0]["métrica"]
    cenario = linhas[0]["cenário"]
    medidas = [l for l in linhas if l["aquecimento"] == "não"]
    cont = {e: sum(l["estado"] == e for l in medidas) for e in ("sucesso", "erro", "expiração")}
    tempos = sorted(float(l["duração (ms)"]) for l in medidas if l["estado"] == "sucesso")
    p95 = tempos[math.ceil(0.95 * len(tempos)) - 1] if tempos else None
    limite = meta.get("cenarios", {}).get(cenario, {}).get("L_ms", LIMITE[metrica])
    r = {"metrica": metrica, "cenario": cenario, "medidas": len(medidas), **cont,
         "p95_ms": p95, "limite_ms": limite, "nota": None, "classificacao": "", "motivo": ""}
    falhas_prep = prep.get(cenario, [])
    if len(medidas) != N_MEDIDAS:
        r["classificacao"] = "Não avaliado"
        r["motivo"] = f"{len(medidas)} tentativas medidas em vez de {N_MEDIDAS} (regra 1)"
    elif falhas_prep:
        r["classificacao"] = "Não avaliado"
        tipos = sorted(set(falhas_prep))
        r["motivo"] = (f"{len(falhas_prep)} tentativa(s) falharam na preparação, antes do clique "
                       f"(defeito do roteiro, regra 1): {'; '.join(tipos)}")
    elif cont["erro"] or cont["expiração"]:
        r["nota"] = 0
        r["motivo"] = (f"{cont['erro']} erro(s) e {cont['expiração']} expiração(ões) (regra 2)"
                       + ("" if p95 is not None else "; P95 não calculável"))
    else:
        r["nota"] = nota_por_p95(metrica, p95)
    if r["nota"] is not None:
        r["classificacao"] = NIVEIS[r["nota"]]
    return r


def fmt(v):
    return "não calculável" if v is None else f"{v:.1f}".replace(".", ",")


def consolidar(res):
    out = {}
    for m in FAIXAS:
        cs = [r for r in res if r["metrica"] == m]
        if not cs:
            out[m] = {"cenarios": [], "nota": None, "cobertura": "sem dados", "hipotese": "inconclusiva"}
            continue
        sem = [r for r in cs if r["nota"] is None]
        notas = [r["nota"] for r in cs if r["nota"] is not None]
        if sem:
            nota, cob = None, "parcial"
        else:
            nota, cob = min(notas), "completa"
        if any(n == 0 for n in notas):
            h = "contrariada"
        elif sem:
            h = "inconclusiva"
        else:
            h = "sustentada"
        out[m] = {"cenarios": cs, "nota": nota, "cobertura": cob, "hipotese": h}
    return out


def grafico(res, destino):
    """Barras horizontais do P95 indexado ao limite L do cenário (100% = L).

    Eixo linear de 0 a 100% de L, com grade a cada 25%. A cor segue a classificação e o
    texto ao lado repete valor e classificação, para não depender só da cor. Cada barra
    tem <title> (dica ao passar o mouse). Cenários sem nota não têm barra, só o motivo.
    """
    larg, lin, esq, dir_ = 760, 34, 130, 250
    topo = 48
    alt = topo + lin * len(res) + 56
    razoes = [r["p95_ms"] / r["limite_ms"] for r in res if r["p95_ms"] is not None and r["nota"] is not None]
    teto = max([1.0] + razoes)
    esc = (larg - esq - dir_) / teto
    base = topo + lin * len(res)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {larg} {alt}" font-family="sans-serif" font-size="12" role="img" aria-labelledby="t d">',
         '<title id="t">P95 de cada cenário de G2 em relação ao limite de aceitação L</title>',
         '<desc id="d">' + "; ".join(
             f'{r["cenario"]}: ' + (f'P95 {fmt(r["p95_ms"])} ms, L {r["limite_ms"]} ms, {r["classificacao"]}'
                                    if r["nota"] is not None else r["classificacao"]) for r in res) + '</desc>',
         '<rect width="100%" height="100%" fill="#ffffff"/>',
         f'<text x="{esq}" y="18" font-weight="bold" fill="#1a1a1a">P95 de cada cenário em % do limite de aceitação L do cenário</text>',
         f'<text x="{esq}" y="34" fill="#555" font-size="11">Menor é melhor. Barra até a linha tracejada = P95 igual a L.</text>']
    for k in range(0, 101, 25):
        x = esq + k / 100 * esc
        tracejado = ' stroke-dasharray="4 3"' if k == 100 else ''
        cor = "#333" if k == 100 else "#e3e3e3"
        s.append(f'<line x1="{x:.1f}" y1="{topo - 6}" x2="{x:.1f}" y2="{base}" stroke="{cor}"{tracejado}/>')
        s.append(f'<text x="{x:.1f}" y="{base + 14}" text-anchor="middle" fill="#555" font-size="11">{k}%{" (L)" if k == 100 else ""}</text>')
    for i, r in enumerate(res):
        y = topo + i * lin
        s.append(f'<text x="{esq - 8}" y="{y + 14}" text-anchor="end" fill="#1a1a1a">{r["cenario"]}</text>')
        if r["nota"] is None:
            s.append(f'<text x="{esq + 6}" y="{y + 14}" fill="#555" font-style="italic">'
                     f'{r["classificacao"]}: sem nota (ver motivo na tabela)</text>')
            continue
        frac = r["p95_ms"] / r["limite_ms"]
        w = max(frac * esc, 2)
        dica = f'{r["cenario"]}: P95 {fmt(r["p95_ms"])} ms de L = {r["limite_ms"]} ms ({fmt(frac * 100)}%), {r["classificacao"]}'
        s.append(f'<g><title>{dica}</title><rect x="{esq}" y="{y}" width="{w:.1f}" height="20" rx="2" fill="{COR[r["nota"]]}"/>'
                 f'<rect x="{esq}" y="{y - 4}" width="{max(w, 12):.1f}" height="28" fill="transparent"/></g>')
        rot = f'{fmt(r["p95_ms"])} ms · {fmt(frac * 100)}% de L · {r["classificacao"]}'
        s.append(f'<text x="{esq + w + 6:.1f}" y="{y + 14}" fill="#1a1a1a">{rot}</text>')
    leg = [(3, "Excelente"), (2, "Bom"), (1, "Aceitável"), (0, "Insatisfatório")]
    x = esq
    for n, t in leg:
        s.append(f'<rect x="{x}" y="{alt - 20}" width="10" height="10" fill="{COR[n]}"/>')
        s.append(f'<text x="{x + 14}" y="{alt - 11}" font-size="11" fill="#1a1a1a">{t}</text>')
        x += 100
    s.append("</svg>")
    destino.write_text("\n".join(s), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rodada", type=Path)
    ap.add_argument("--saida", type=Path)
    a = ap.parse_args()
    saida = a.saida or a.rodada / "analise"
    saida.mkdir(parents=True, exist_ok=True)
    mpath = a.rodada / "metadados.json"
    meta = json.load(open(mpath, encoding="utf-8")) if mpath.exists() else {}
    if not meta:
        print("AVISO: metadados.json ausente; usando os limites L_j da Fase 2.", file=sys.stderr)
    csvs = sorted(p for p in a.rodada.glob("m[2-5]-*.csv"))
    if not csvs:
        sys.exit(f"Nenhum CSV de M2 a M5 em {a.rodada}")
    prep = motivos_preparacao(a.rodada)
    res = sorted((analisar_cenario(p, meta, prep) for p in csvs), key=lambda r: (r["metrica"], r["cenario"]))
    cons = consolidar(res)

    with open(saida / "resultados.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["métrica", "cenário", "medidas", "sucessos", "erros", "expirações",
                    "P95 (ms)", "limite L (ms)", "classificação", "motivo"])
        for r in res:
            w.writerow([r["metrica"], r["cenario"], r["medidas"], r["sucesso"], r["erro"], r["expiração"],
                        "" if r["p95_ms"] is None else r["p95_ms"], r["limite_ms"], r["classificacao"], r["motivo"]])
    grafico(res, saida / "grafico-g2.svg")

    md = [f"# Análise de G2 — rodada `{a.rodada.name}`", "",
          "## Resultado por cenário", "",
          "| Métrica | Cenário | Medidas | Sucessos | Erros | Expirações | P95 (ms) | L (ms) | Classificação | Observação |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        md.append(f"| {r['metrica']} | {r['cenario']} | {r['medidas']} | {r['sucesso']} | {r['erro']} | "
                  f"{r['expiração']} | {fmt(r['p95_ms'])} | {r['limite_ms']} | {r['classificacao']} | {r['motivo']} |")
    md += ["", "## Consolidação por métrica e hipóteses", "",
           "| Métrica | Nota da métrica (menor cenário) | Cobertura | Hipótese | Questão |", "|---|---|---|---|---|"]
    for m, c in cons.items():
        nota = "sem nota consolidada" if c["nota"] is None else NIVEIS[c["nota"]]
        md.append(f"| {m} | {nota} | {c['cobertura']} | {HIPOTESE[m][0]} {c['hipotese']} | {HIPOTESE[m][1]} |")
    md += ["", "![P95 por cenário em relação ao limite L](grafico-g2.svg)", "",
           "As hipóteses valem só para as condições avaliadas (reprodução local, `commit` `3d399e7`, massa de referência)."
           " Não demonstram desempenho em produção nem são testes de significância (Fase 2, seção 4.3, regra 5).", ""]
    (saida / "resumo.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))
    print(f"\nSaídas em {saida}", file=sys.stderr)


if __name__ == "__main__":
    main()
