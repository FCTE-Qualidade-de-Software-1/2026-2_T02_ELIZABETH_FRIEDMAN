# Artigo

Artigo da equipe no modelo SBC Reviews 2025 (classe `sbcreviews-2025`), em português.

## Arquivos

| Arquivo | Conteúdo |
|---------|----------|
| `main.tex` | Fonte do artigo |
| `refs.bib` | Referências em BibTeX |
| `Artigo___Qualida_Elizabeth_Friedman.pdf` | PDF compilado no Overleaf a partir dos fontes desta pasta |

## Situação das seções

| Seção | Situação | Issue |
|-------|----------|-------|
| Resumo e abstract | Versão curta; expandir após a Fase 4 (o template pede de 500 a 750 palavras) | |
| 1. Introdução | Escrita | #9 |
| 2. Referencial teórico (SQuaRE, ISO/IEC 25010:2023, ISO/IEC 25040, GQM e PSM) | Escrita | #9 |
| 3. Metodologia (Fases 1 e 2, PSM/CID e ferramentas) | Escrita; adaptação completa das Fases 1 e 2 e revisão final na #10 | #8, #10 |
| 4. Resultados | Após a Fase 4 | |
| 5. Conclusão | Após a Fase 4 | |
| Declarações | Rascunho; contribuições CRediT e declaração de IA a revisar | #10 |

Pendências que dependem da equipe estão marcadas com `% TODO` no `main.tex`.

## Como compilar

- Compila no **Overleaf** com o compilador **XeLaTeX** (Menu, Compiler). Não use pdfLaTeX.
- Os arquivos da classe (`sbcreviews-2025.cls`, `aas_macros.sty`, `apalike-sol.bst`, `sol.jpg`) ficam no projeto do Overleaf e não são versionados aqui.
- Aqui ficam só os fontes editados pela equipe (`main.tex` e `refs.bib`) e o PDF compilado.

## Como atualizar o PDF

1. Copie `main.tex` e `refs.bib` desta pasta para o projeto do Overleaf.
2. Recompile. Se as referências aparecerem como `?`, use **Recompile from scratch**.
3. Baixe o PDF e substitua `Artigo___Qualida_Elizabeth_Friedman.pdf` nesta pasta, no mesmo PR que alterou os fontes.
