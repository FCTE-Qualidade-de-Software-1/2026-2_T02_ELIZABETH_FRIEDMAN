# Artigo

Artigo da equipe no modelo de artigos da SBC (coluna única, pacote `sbc-template`), em português. Limite total de 15 páginas.

## Arquivos

| Arquivo | Conteúdo |
|---------|----------|
| `main.tex` | Fonte do artigo |
| `refs.bib` | Referências em BibTeX |
| `Artigo___Qualida_Elizabeth_Friedman.pdf` | PDF compilado no Overleaf a partir dos fontes desta pasta |

## Situação das seções

| Seção | Situação | Issue |
|-------|----------|-------|
| Resumo e abstract | Versão curta; revisar após a Fase 4 (o modelo limita a 10 linhas) | |
| 1. Introdução | Escrita e reduzida | #9, #24 |
| 2. Referencial teórico (SQuaRE, ISO/IEC 25010:2023, ISO/IEC 25040, GQM e PSM) | Escrito e reduzido | #9, #24 |
| 3. Metodologia (Fases 1 e 2, PSM/CID e ferramentas) | Escrita e reduzida; Fases 3 e 4 após a Fase 3 | #8, #10, #24 |
| 4. Resultados | Após a Fase 4 | |
| 5. Conclusão | Após a Fase 4 | |
| Contribuições e uso de IA | Rascunho; contribuições CRediT e declaração de IA a revisar | #10 |

As seções das Entregas 1 e 2 (até a Metodologia) ocupam cerca de 7 páginas, o que deixa cerca de 8 páginas para as Fases 3 e 4, os resultados e a conclusão.

Pendências que dependem da equipe estão marcadas com `% TODO` no `main.tex`.

## Como compilar

- Compila no **Overleaf** com o compilador **pdfLaTeX** (Menu, Compiler).
- Os arquivos do modelo da SBC (`sbc-template.sty` e `sbc.bst`, do pacote de modelos para publicação de artigos da SBC) ficam no projeto do Overleaf e não são versionados aqui. Os arquivos do modelo antigo (`sbcreviews-2025.cls`, `aas_macros.sty`, `apalike-sol.bst`, `sol.jpg`) podem ser removidos do projeto.
- Aqui ficam só os fontes editados pela equipe (`main.tex` e `refs.bib`) e o PDF compilado.

## Como atualizar o PDF

1. Copie `main.tex` e `refs.bib` desta pasta para o projeto do Overleaf.
2. Recompile. Se as referências aparecerem como `?`, use **Recompile from scratch**.
3. Baixe o PDF e substitua `Artigo___Qualida_Elizabeth_Friedman.pdf` nesta pasta, no mesmo PR que alterou os fontes.
