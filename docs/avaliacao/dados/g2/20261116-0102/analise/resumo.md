# Análise de G2 — rodada `20261116-0102`

## Resultado por cenário

| Métrica | Cenário | Medidas | Sucessos | Erros | Expirações | P95 (ms) | L (ms) | Classificação | Observação |
|---|---|---|---|---|---|---|---|---|---|
| M3 | m3-com-selecao | 30 | 30 | 0 | 0 | 33,5 | 1000 | Excelente (3) |  |
| M3 | m3-sem-selecao | 30 | 30 | 0 | 0 | 38,5 | 1000 | Excelente (3) |  |

## Consolidação por métrica e hipóteses

| Métrica | Nota da métrica (menor cenário) | Cobertura | Hipótese | Questão |
|---|---|---|---|---|
| M2 | sem nota consolidada | sem dados | H2 inconclusiva | Q2 |
| M3 | Excelente (3) | completa | H3 sustentada | Q3 |
| M4 | sem nota consolidada | sem dados | H4 inconclusiva | Q4 |
| M5 | sem nota consolidada | sem dados | H5 inconclusiva | Q5 |

![P95 por cenário em relação ao limite L](grafico-g2.svg)

As hipóteses valem só para as condições avaliadas (reprodução local, `commit` `3d399e7`, massa de referência). Não demonstram desempenho em produção nem são testes de significância (Fase 2, seção 4.3, regra 5).
