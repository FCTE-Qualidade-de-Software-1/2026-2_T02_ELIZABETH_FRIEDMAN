# G1 — Manutenibilidade

<!--
Percurso do objetivo G1. Os trechos com 8<-- são importados das Fases 2 e 4; para mudar o texto deles,
edite a fase. São escritos à mão aqui: o quadro de estado, a tabela da seção 1 e os textos de ligação.
-->

!!! warning "Estado: Inconclusivo"
    H1.1, H1.2 e H1.4 foram sustentadas. H1.3 está inconclusiva porque C1 e C2 não têm execução com o tempo registrado.
    Ver o [julgamento dos três objetivos](fase-4.md#31-estado-de-cada-hipotese-e-de-cada-objetivo).

## 1. Visão geral

| Questão | Limite de aceitação da hipótese | Métrica | Método | Dados | Resultado | Julgamento |
|---|---|---|---|---|---|---|
| [Q1.1](#q1-1) Modularidade | Até 10% dos arquivos em ciclos, por camada | [M1.1](#ficha-m1-1) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m11--ciclos-de-importação): pydeps e Madge | [ciclos](avaliacao/dados/g1/m1-1-ciclos.json), [resultados](avaliacao/dados/g1/m1-1-m1-2-resultados.csv) | API 4,00%; *frontend* 5,00% | H1.1 sustentada |
| [Q1.2](#q1-2) Analisabilidade | Até 20% dos blocos com CC > 10, por recorte | [M1.2](#ficha-m1-2) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m12--complexidade-ciclomática): Radon e ESLint | [Radon](avaliacao/dados/g1/m1-2-radon-blocos.json), [ESLint](avaliacao/dados/g1/m1-2-eslint-blocos.json), [resultados](avaliacao/dados/g1/m1-1-m1-2-resultados.csv) | API 0,73%; *frontend*, *scraper* e gerador 0% | H1.2 sustentada |
| [Q1.3](#q1-3) Modificabilidade | C1 e C2 em até 90 min cada, sem regressões | [M1.3](#ficha-m1-3) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m13--mudanças-controladas): mudança cronometrada | [*patches* e verificação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/M1.3) | 20 min por tarefa, autodeclarados; C2 reprova em 9 testes | H1.3 inconclusiva, sem nota |
| [Q1.4](#q1-4) Testabilidade | Ao menos 70% das linhas, por recorte | [M1.4](#ficha-m1-4) | [Roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m14--cobertura-de-linhas): coverage.py | [coverage](avaliacao/dados/g1/m1-4-coverage.json), [resultados](avaliacao/dados/g1/m1-4-resultados.csv) | API 81,88%; *scraper* 97,50%; gerador 99,29% | H1.4 sustentada |

Q1.3 também usa M1.1, M1.2 e M1.4 como contexto. Essas métricas não substituem M1.3 nem recebem uma segunda nota.

## 2. Objetivo de medição

--8<-- "fase-2.md:objetivo-g1"

## 3. Questões e hipóteses

--8<-- "fase-2.md:questoes-g1"

## 4. Métricas e critérios

As fichas são as da [Fase 2](fase-2.md#3-metricas-nivel-quantitativo). Clique para abrir.

<span id="ficha-m1-1"></span>

??? note "M1.1 — Arquivos participantes de ciclos internos"
    --8<-- "fase-2.md:ficha-m1-1"

<span id="ficha-m1-2"></span>

??? note "M1.2 — Blocos com complexidade ciclomática elevada"
    --8<-- "fase-2.md:ficha-m1-2"

<span id="ficha-m1-3"></span>

??? note "M1.3 — Tempo para concluir uma mudança validada"
    --8<-- "fase-2.md:ficha-m1-3"

<span id="ficha-m1-4"></span>

??? note "M1.4 — Cobertura de linhas executáveis da API"
    --8<-- "fase-2.md:ficha-m1-4"

**Faixas de pontuação** ([Fase 2, seção 4.1](fase-2.md#41-escala-e-faixas-por-metrica))

--8<-- "fase-2.md:faixas-g1"

A regra que transforma as notas em julgamento está na [Fase 2, seção 4.5](fase-2.md#45-julgamento-das-hipoteses-de-manutenibilidade); a justificativa dos
limites, na [seção 4.2](fase-2.md#42-justificativa-dos-limites).

## 5. Método e dados coletados

O método e os pilotos estão na [Fase 3, seção 1.2](fase-3.md#12-procedimentos-e-pilotos-de-manutenibilidade) e o ambiente, nas
[seções 2.1](fase-3.md#21-versao-avaliada-e-subida-do-ambiente) e [2.2](fase-3.md#22-requisitos-do-avaliador).
As tarefas de M1.3 estão em [C1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/tarefas/C1.md) e [C2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/tarefas/C2.md).

--8<-- "fase-4.md:dados-g1"

## 6. Resultados e respostas

--8<-- "fase-4.md:resultado-g1"

### Q1.1 — Modularidade (H1.1, M1.1) {#q1-1}

--8<-- "fase-4.md:q1-1"

### Q1.2 — Analisabilidade (H1.2, M1.2) {#q1-2}

--8<-- "fase-4.md:q1-2"

### Q1.3 — Modificabilidade (H1.3, M1.3) {#q1-3}

--8<-- "fase-4.md:q1-3"

### Q1.4 — Testabilidade (H1.4, M1.4) {#q1-4}

--8<-- "fase-4.md:q1-4"

### Resumo

--8<-- "fase-4.md:resumo-g1"

## 7. Limitações e desvios

--8<-- "fase-4.md:limites-g1"

## 8. Julgamento e decisões

--8<-- "fase-4.md:proposito-g1"

--8<-- "fase-4.md:d3"

As oportunidades de melhoria de código são as de nº 5 a 9 da
[Tabela 6](fase-4.md#41-oportunidades-de-melhoria), ligadas a D3.

A relação com os outros objetivos está na [Fase 4, seção 3.3](fase-4.md#33-relacoes-entre-as-caracteristicas) e os limites do julgamento, na
[seção 3.4](fase-4.md#34-limites-do-julgamento).
