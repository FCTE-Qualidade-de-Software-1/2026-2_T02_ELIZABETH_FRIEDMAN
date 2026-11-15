"""Confere o inventário de M1.4 e extrai os três recortes, sem arredondar."""

import csv
import json
import sys
from pathlib import Path


def main():
    pasta = Path(sys.argv[1])
    inventario = Path(sys.argv[2])
    for nome in ("codigo-saida.txt", "testes-codigo-saida.txt"):
        if (pasta / nome).read_text().strip() != "0":
            raise SystemExit("Execução inválida: " + nome)
    cobertura = json.loads((pasta / "coverage.json").read_text())
    esperados = {
        p.removeprefix("api/")
        for p in json.loads(inventario.read_text())["incluidos"]
        if p.startswith("api/")
    }
    arquivos = cobertura["files"]
    auditoria = {
        "inventario": str(inventario),
        "arquivos_esperados": len(esperados),
        "arquivos_reportados": len(arquivos),
        "ausentes": sorted(esperados - arquivos.keys()),
        "extras": sorted(arquivos.keys() - esperados),
        "arquivos_sem_linhas_executadas": sorted(
            p for p, dados in arquivos.items()
            if dados["summary"]["num_statements"] > 0
            and dados["summary"]["covered_lines"] == 0
        ),
        "linhas_excluidas": sum(
            len(dados["excluded_lines"]) for dados in arquivos.values()
        ),
    }
    (pasta / "auditoria-inventario.json").write_text(
        json.dumps(auditoria, ensure_ascii=False, indent=2) + "\n"
    )
    if auditoria["ausentes"] or auditoria["extras"] or auditoria["linhas_excluidas"]:
        raise SystemExit("Divergência de escopo: conferir auditoria-inventario.json")
    recortes = {
        "API": cobertura["totals"],
        "scraper": arquivos["utils/web_scraping.py"]["summary"],
        "gerador": arquivos["utils/schedule_generator.py"]["summary"],
    }
    with (pasta / "resultados.csv").open("w", newline="") as destino:
        tabela = csv.writer(destino)
        tabela.writerow(("metrica", "recorte", "linhas_cobertas", "linhas_executaveis", "percentual", "nota", "estado"))
        for nome, dados in recortes.items():
            cobertas, total = dados["covered_lines"], dados["num_statements"]
            valor = 100 * cobertas / total if total else None
            nota = sum(valor >= limite for limite in (70, 80, 90)) if total else ""
            tabela.writerow(("M1.4", nome, cobertas, total, valor, nota, "Medido" if total else "Não calculável"))
    print((pasta / "resultados.csv").read_text())


if __name__ == "__main__":
    main()
