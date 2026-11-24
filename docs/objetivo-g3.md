# G3 — Capacidade de interação

<!--
Percurso do objetivo G3. Os trechos com 8<-- são importados das Fases 2 e 4; para mudar o texto deles,
edite a fase. São escritos à mão aqui: o quadro de estado, a tabela da seção 1 e os textos de ligação.
-->

!!! failure "Estado: Não atendido"
    H6, H7, H8 e H9 foram contrariadas: cada uma tem ao menos um recorte com nota 0. M7 e M9 têm recortes sem cobertura completa, que não mudam essa conclusão.
    Ver o [julgamento dos três objetivos](fase-4.md#31-estado-de-cada-hipotese-e-de-cada-objetivo).

## 1. Visão geral

| Questão | Limite de aceitação da hipótese | Métrica | Método | Dados | Resultado | Julgamento |
|---|---|---|---|---|---|---|
| [Q6](#q6) Aprendizagem | Ao menos 80%, por dispositivo | [M6](#ficha-m6) | [Protocolo, 3](avaliacao-interacao/protocolo.md#3-m6-primeiro-uso) | [sessões](avaliacao/dados/g3/m6-m9-sessoes.csv), [resultados](avaliacao/dados/g3/m6-m9-resultados.csv) | Computador 0/2; celular 1/2 | H6 contrariada |
| [Q7](#q7) Operabilidade | Ao menos 90%, por tarefa e dispositivo | [M7](#ficha-m7) | [Protocolo, 4](avaliacao-interacao/protocolo.md#4-m7-controle-da-grade) | [sessões](avaliacao/dados/g3/m6-m9-sessoes.csv), [resultados](avaliacao/dados/g3/m6-m9-resultados.csv) | Computador: seleção 2/2, troca 1/2, remoção 2/2. Celular: seleção 1/2; troca e remoção 1/1, sem nota | H7 contrariada |
| [Q8](#q8) Proteção contra erros | 100%, por dispositivo e modalidade | [M8](#ficha-m8) | [Protocolo, 5](avaliacao-interacao/protocolo.md#5-m8-e-m9) e [inventário](avaliacao-interacao/instrumentos.md#1-inventario-m8) | [observações](avaliacao/dados/g3/m8-observacoes.csv), [capturas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/docs/avaliacao/dados/g3/m8-capturas) | Navegador 5/6 nos dois dispositivos (R04 sem proteção); conta 1/1 | H8 contrariada |
| [Q9](#q9) Autodescrição | Ao menos 90%, por ponto e dispositivo | [M9](#ficha-m9) | [Protocolo, 5](avaliacao-interacao/protocolo.md#5-m8-e-m9) e [gabarito](avaliacao-interacao/instrumentos.md#2-gabarito-m9) | [sessões](avaliacao/dados/g3/m6-m9-sessoes.csv), [resultados](avaliacao/dados/g3/m6-m9-resultados.csv) | V01 e V03: computador 2/2, celular 1/2. V02 e V04 não avaliados | H9 contrariada |

Q6 também usa M7 e M9, e Q7 usa M9, como apoio. Essas ligações não criam uma segunda nota.

## 2. Objetivo de medição

--8<-- "fase-2.md:objetivo-g3"

## 3. Questões e hipóteses

--8<-- "fase-2.md:questoes-g3"

## 4. Métricas e critérios

As fichas são as da [Fase 2](fase-2.md#3-metricas-nivel-quantitativo). Clique para abrir.

<span id="ficha-m6"></span>

??? note "M6 — Sucesso no primeiro uso"
    --8<-- "fase-2.md:ficha-m6"

<span id="ficha-m7"></span>

??? note "M7 — Sucesso independente nas tarefas de controle"
    --8<-- "fase-2.md:ficha-m7"

<span id="ficha-m8"></span>

??? note "M8 — Cobertura de proteção contra perda involuntária"
    --8<-- "fase-2.md:ficha-m8"

<span id="ficha-m9"></span>

??? note "M9 — Compreensão dos estados e ações"
    --8<-- "fase-2.md:ficha-m9"

**Faixas de pontuação** ([Fase 2, seção 4.1](fase-2.md#41-escala-e-faixas-por-metrica))

--8<-- "fase-2.md:faixas-g3"

A regra que transforma as notas em julgamento está na [Fase 2, seção 4.4](fase-2.md#44-regras-de-aplicacao-e-julgamento-de-interacao-m6m9); a justificativa dos
limites, na [seção 4.2](fase-2.md#42-justificativa-dos-limites).

## 5. Método e dados coletados

M6, M7 e M9 seguem o [protocolo 0.3](avaliacao-interacao/protocolo.md), com participantes; M8 é uma inspeção feita pela equipe. O
[inventário de M8 e o gabarito de M9](avaliacao-interacao/instrumentos.md) e o [perfil dos participantes](fase-3.md#25-participantes-e-sessoes-m6-a-m9) completam o método.
Os desvios entre o protocolo e a execução estão nas [limitações](#7-limitacoes-e-desvios).

--8<-- "fase-4.md:dados-g3"

## 6. Resultados e respostas

--8<-- "fase-4.md:resultado-g3"

### Q6 — Aprendizagem (H6, M6) {#q6}

--8<-- "fase-4.md:q6"

### Q7 — Operabilidade (H7, M7) {#q7}

--8<-- "fase-4.md:q7"

### Q8 — Proteção contra erros (H8, M8) {#q8}

--8<-- "fase-4.md:q8"

### Q9 — Autodescrição (H9, M9) {#q9}

--8<-- "fase-4.md:q9"

### Resumo

--8<-- "fase-4.md:resumo-g3"

## 7. Limitações e desvios

--8<-- "fase-4.md:limites-g3"

## 8. Julgamento e decisões

--8<-- "fase-4.md:proposito-g3"

--8<-- "fase-4.md:d1"

**D2 (ação executada).** A equipe corrigiu a perda da seleção na recarga (R04) e verificou a correção:
[ação de melhoria](fase-4.md#42-acao-de-melhoria-executada) e [relatório](avaliacao/dados/acao-r04/RELATORIO.md). A verificação não altera os 5/6 de M8, que
são da versão avaliada.

A relação com os outros objetivos está na [Fase 4, seção 3.3](fase-4.md#33-relacoes-entre-as-caracteristicas) e os limites do julgamento, na
[seção 3.4](fase-4.md#34-limites-do-julgamento).
