# G2 — Eficiência de desempenho

<!--
Percurso do objetivo G2. Os trechos com 8<-- são importados das Fases 2 e 4; para mudar o texto deles,
edite a fase. São escritos à mão aqui: o quadro de estado, a tabela da seção 1 e os textos de ligação.
-->

!!! success "Estado: Atendido nas condições avaliadas"
    H2 a H5 foram sustentadas. Os sete cenários ficaram na faixa Excelente, com no máximo 7% do limite. M3 vale pela recoleta de 16/11, feita em outro ambiente.
    Ver o [julgamento dos três objetivos](fase-4.md#31-estado-de-cada-hipotese-e-de-cada-objetivo).

## 1. Visão geral

| Questão | Limite de aceitação da hipótese | Métrica | Método | Dados | Resultado | Julgamento |
|---|---|---|---|---|---|---|
| [Q2](#q2) Tempo da busca | P95 até 2.000 ms | [M2](#ficha-m2) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/e2e/tests/desempenho/m2-busca.spec.ts) Playwright | 15/11: [nome](avaliacao/dados/g2/20261115-2128/m2-nome.csv), [código](avaliacao/dados/g2/20261115-2128/m2-codigo.csv) | 30,8 ms e 31,0 ms | H2 sustentada (3) |
| [Q3](#q3) Tempo da seleção | P95 até 1.000 ms | [M3](#ficha-m3) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/e2e/tests/desempenho/m3-selecao.spec.ts) Playwright | 16/11: [sem seleção](avaliacao/dados/g2/20261116-0102/m3-sem-selecao.csv), [com seleção](avaliacao/dados/g2/20261116-0102/m3-com-selecao.csv), [ambiente](avaliacao/dados/g2/20261116-0102/AMBIENTE.md) | 38,5 ms e 33,5 ms | H3 sustentada (3) |
| [Q4](#q4) Tempo da geração | P95 até 10.000 ms | [M4](#ficha-m4) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/e2e/tests/desempenho/m4-geracao.spec.ts) Playwright | 15/11: [A](avaliacao/dados/g2/20261115-2128/m4-a.csv), [B](avaliacao/dados/g2/20261115-2128/m4-b.csv) | 649,3 ms e 700,7 ms | H4 sustentada (3) |
| [Q5](#q5) Tempo do salvamento | P95 até 2.000 ms | [M5](#ficha-m5) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/e2e/tests/desempenho/m5-salvamento.spec.ts) Playwright | 15/11: [conta](avaliacao/dados/g2/20261115-2128/m5-conta.csv) | 53,0 ms | H5 sustentada (3) |

Cada cenário tem 30 tentativas medidas, depois de 2 de aquecimento descartadas. O P95 é o 29º tempo dos 30 sucessos ordenados ([cálculo](fase-3.md#117-registro-e-calculo-do-p95)).

## 2. Objetivo de medição

--8<-- "fase-2.md:objetivo-g2"

## 3. Questões e hipóteses

--8<-- "fase-2.md:questoes-g2"

## 4. Métricas e critérios

As fichas são as da [Fase 2](fase-2.md#3-metricas-nivel-quantitativo). Clique para abrir.

<span id="ficha-m2"></span>

??? note "M2 — Tempo de resposta da busca (P95)"
    --8<-- "fase-2.md:ficha-m2"

<span id="ficha-m3"></span>

??? note "M3 — Tempo de atualização após seleção de turma (P95)"
    --8<-- "fase-2.md:ficha-m3"

<span id="ficha-m4"></span>

??? note "M4 — Tempo de geração de grades (P95)"
    --8<-- "fase-2.md:ficha-m4"

<span id="ficha-m5"></span>

??? note "M5 — Tempo de retorno do salvamento (P95)"
    --8<-- "fase-2.md:ficha-m5"

**Faixas de pontuação** ([Fase 2, seção 4.1](fase-2.md#41-escala-e-faixas-por-metrica))

--8<-- "fase-2.md:faixas-g2"

A regra que transforma as notas em julgamento está na [Fase 2, seção 4.3](fase-2.md#43-regras-de-aplicacao-e-julgamento-de-eficiencia-m2m5); a justificativa dos
limites, na [seção 4.2](fase-2.md#42-justificativa-dos-limites).

## 5. Método e dados coletados

O passo a passo está na [Fase 3, seção 1.1](fase-3.md#11-eficiencia-de-desempenho-m2-a-m5-passo-a-passo): [cenários fixos](fase-3.md#112-cenarios-fixos),
[ações e sinais de conclusão](fase-3.md#113-acoes-seletores-e-sinais-de-conclusao), [medição dos instantes](fase-3.md#115-medicao-dos-instantes-e-restauracao-do-estado) e
[cálculo do P95](fase-3.md#117-registro-e-calculo-do-p95). A massa está na [seção 2.3](fase-3.md#23-massa-de-referencia). As definições comuns a M2–M5 (P95, erros
e expirações) estão na [Fase 2, seção 3.1](fase-2.md#31-convencoes-de-medicao-de-eficiencia-de-desempenho).

--8<-- "fase-4.md:dados-g2"

## 6. Resultados e respostas

--8<-- "fase-4.md:resultado-g2"

### Q2 — Tempo da busca (H2, M2) {#q2}

--8<-- "fase-4.md:q2"

### Q3 — Tempo da seleção (H3, M3) {#q3}

--8<-- "fase-4.md:q3"

### Q4 — Tempo da geração (H4, M4) {#q4}

--8<-- "fase-4.md:q4"

### Q5 — Tempo do salvamento (H5, M5) {#q5}

--8<-- "fase-4.md:q5"

??? note "Histórico de M3: a rodada de 15/11 e a recoleta de 16/11"
    --8<-- "fase-4.md:historico-m3"

### Resumo

--8<-- "fase-4.md:resumo-g2"

## 7. Limitações e desvios

--8<-- "fase-4.md:limites-g2"

## 8. Julgamento e decisões

--8<-- "fase-4.md:proposito-g2"

G2 apoia D1 e D2. Como nenhuma hipótese foi contrariada, G2 não gerou candidato a correção
([o que não se recomenda](fase-4.md#41-oportunidades-de-melhoria)).

A relação com os outros objetivos está na [Fase 4, seção 3.3](fase-4.md#33-relacoes-entre-as-caracteristicas) e os limites do julgamento, na
[seção 3.4](fase-4.md#34-limites-do-julgamento).
