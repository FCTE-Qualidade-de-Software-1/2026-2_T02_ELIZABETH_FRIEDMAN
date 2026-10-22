#!/usr/bin/env python3
"""Mantém horas.csv: uma linha por (issue, responsável). Nunca sobrescreve horas preenchidas."""
import csv, json, os, subprocess

CAMINHO = "docs/gestao/evidencias/horas.csv"
CAMPOS = ["issue", "titulo", "responsavel", "horas"]
PLACEHOLDER = "XX"

def pendente(h):
    return str(h).strip().upper() in ("", "X", "XX")

saida = subprocess.run(
    ["gh", "issue", "list", "--state", "all", "--limit", "500",
     "--json", "number,title,assignees"],
    capture_output=True, text=True, check=True).stdout
issues = json.loads(saida)
titulos = {i["number"]: i["title"] for i in issues}

# lê o CSV atual (aceita ',' ou ';', pois o Excel em pt-BR salva com ';')
antigas = {}
if os.path.exists(CAMINHO):
    with open(CAMINHO, newline="", encoding="utf-8-sig") as f:
        primeira = f.readline()
        f.seek(0)
        delim = ";" if primeira.count(";") > primeira.count(",") else ","
        for l in csv.DictReader(f, delimiter=delim):
            try:
                antigas[(int(l["issue"]), l["responsavel"].strip())] = l
            except (KeyError, ValueError, TypeError, AttributeError):
                continue

# uma linha por (issue, responsável atribuído)
novas = {}
for i in issues:
    for a in i["assignees"]:
        chave = (i["number"], a["login"])
        h = antigas.get(chave, {}).get("horas", PLACEHOLDER)
        novas[chave] = {"issue": i["number"], "titulo": i["title"],
                        "responsavel": a["login"],
                        "horas": PLACEHOLDER if pendente(h) else str(h).strip()}

# mantém quem saiu da issue, mas já declarou horas
for chave, l in antigas.items():
    if chave not in novas and not pendente(l.get("horas", "")):
        n, login = chave
        novas[chave] = {"issue": n, "titulo": titulos.get(n, l.get("titulo", "")),
                        "responsavel": login, "horas": str(l["horas"]).strip()}

# avisa valores que não são número
for (n, login), l in sorted(novas.items()):
    if not pendente(l["horas"]):
        try:
            float(l["horas"].replace(",", "."))
        except ValueError:
            print(f'AVISO: issue #{n} ({login}) tem horas inválidas: "{l["horas"]}"')

os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)
with open(CAMINHO, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n")
    w.writeheader()
    for chave in sorted(novas):
        w.writerow(novas[chave])

pend = sum(1 for l in novas.values() if pendente(l["horas"]))
print(f"{len(novas)} linhas, {pend} com horas pendentes ({PLACEHOLDER})")