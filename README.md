# 2026-2_T02_ELIZABETH_FRIEDMAN

Projeto final de FGA0315 Qualidade de Software 1 (UnB/FCTE, 2026/2, Turma T02): avaliação de qualidade de produto de software segundo a família SQuaRE.

GitPage: <https://fcte-qualidade-de-software-1.github.io/2026-2_T02_ELIZABETH_FRIEDMAN/>

## Rodando o site localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Acesse <http://127.0.0.1:8000>. O conteúdo fica em `docs/` e a navegação em `mkdocs.yml`.

A cada push na `main`, o GitHub Actions (`.github/workflows/pages.yml`) gera e publica o site.
