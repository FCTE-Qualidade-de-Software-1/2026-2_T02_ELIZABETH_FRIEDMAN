# Fase 4 — Executar a avaliação e resultados

<!--
Referência: ISO/IEC 25040, atividades 4 e 5.
-->

## 1. Obtenção das medidas

<!--
F4-C1 e F4-C2: coleta seguindo o plano da Fase 3; ligação DIRETA entre cada dado bruto
(arquivo, formulário, log, vídeo) e a métrica calculada.
Dados de participantes: anonimizar e descrever as condições de acesso (premissa 5).
-->

| Métrica | Data da coleta | Responsável | Dados brutos | Procedimento de cálculo |
|---------|----------------|-------------|--------------|-------------------------|
| M1.1 — Modularidade | 15/11/2026 | Kaleb | [ciclos.json](avaliacao/dados/g1/m1-1-ciclos.json), [grafo do Madge](avaliacao/dados/g1/m1-1-madge-frontend.json); pacote completo em [`formal/estatica/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/formal/estatica) | [Roteiro de M1.1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m11--ciclos-de-importação), [`ciclos.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/ciclos.py), [auditoria dos ciclos](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/formal/estatica/auditoria-ciclos.md) e [resultados](avaliacao/dados/g1/m1-1-m1-2-resultados.csv) |
| M1.2 — Analisabilidade | 15/11/2026 | Kaleb | [blocos do Radon](avaliacao/dados/g1/m1-2-radon-blocos.json), [blocos do ESLint](avaliacao/dados/g1/m1-2-eslint-blocos.json), [maiores CC por recorte](avaliacao/dados/g1/m1-2-maximos-cc.json); pacote completo em [`formal/estatica/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/formal/estatica) | [Roteiro de M1.2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m12--complexidade-ciclomática), [`coletar.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/coletar.py) e [resultados](avaliacao/dados/g1/m1-1-m1-2-resultados.csv) |
| M1.3 — Modificabilidade | 12/11/2026 | Joaquim  | [Patches de C1 e C2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/M1.3) e [verificação a posteriori](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/M1.3/verificacao-a-posteriori) (relatório e logs) | [Roteiro de M1.3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m13--mudanças-controladas) e [relatório da verificação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/M1.3/verificacao-a-posteriori/RELATORIO.md) |
| M1.4 — Testabilidade | 15/11/2026 | Kaleb | [`coverage.json`](avaliacao/dados/g1/m1-4-coverage.json), [auditoria do inventário](avaliacao/dados/g1/m1-4-auditoria-inventario.json), [ambiente](avaliacao/dados/g1/m1-4-ambiente.txt); log e demais arquivos em [`formal/M1.4/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/formal/M1.4/execucao-docker) | [Roteiro de M1.4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/README.md#m14--cobertura-de-linhas), [`cobertura.sh`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/cobertura.sh), [`resumir_cobertura.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/manutenibilidade/resumir_cobertura.py) e [resultados](avaliacao/dados/g1/m1-4-resultados.csv) |

## 2. Análise e respostas ao GQM

<!--
F4-C3: resultado de cada métrica comparado aos níveis de pontuação da Fase 2,
resposta a TODAS as questões e objetivos, com gráficos e tabelas.
-->

### 2.1 G1 — Manutenibilidade

Medições sobre o Sua Grade UnB no commit `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`,
sem alterações rastreadas. Os valores seguem as faixas da
[Fase 2, seção 4.1](fase-2.md#41-escala-e-faixas-por-metrica) e foram classificados sem
arredondamento prévio. Os percentuais não são combinados entre recortes de denominadores
diferentes, e as notas não são calculadas em média, conforme a
[seção 4.5](fase-2.md#45-julgamento-das-hipoteses-de-manutenibilidade).

**Tabela 1 — Resultados de G1 por métrica e recorte**

| Métrica | Recorte | Numerador / denominador | Valor | Faixa da nota | Nota |
|---------|---------|-------------------------|-------|---------------|------|
| M1.1 (% de arquivos em ciclos) | API | 2 / 50 | 4,00% | >0 a 5% | 2 |
| M1.1 | Frontend | 3 / 60 | 5,00% | >0 a 5% (limite superior) | 2 |
| M1.2 (% de blocos com CC > 10) | API | 1 / 137 | 0,73% | 0 a 5% | 3 |
| M1.2 | Frontend | 0 / 213 | 0,00% | 0 a 5% | 3 |
| M1.2 | *Scraper* | 0 / 18 | 0,00% | 0 a 5% | 3 |
| M1.2 | Gerador | 0 / 15 | 0,00% | 0 a 5% | 3 |
| M1.3 (minutos até a mudança validada) | C1 | — | 20 min, autodeclarado pelo executor, com medição no próprio celular do executor; patch aprovado na suíte completa na verificação posterior | >0 a 30 min | 3  |
| M1.3 | C2 | — | 20 min, autodeclarado pelo executor, com medição no próprio celular do executor; patch reprova na suíte completa (9 falhas) | — | Não concluída; sem nota |
| M1.4 (% de linhas cobertas) | API | 1.143 / 1.396 | 81,88% | 80% a menos de 90% | 2 |
| M1.4 | *Scraper* | 156 / 160 | 97,50% | 90% ou mais | 3 |
| M1.4 | Gerador | 140 / 141 | 99,29% | 90% ou mais | 3 |

Os blocos de M1.2 do recorte da API incluem os do *scraper* e do gerador. O *frontend* não
tem testes automatizados e, por isso, fica fora de M1.4.

**Q1.1 — Modularidade (H1.1).** Sim, nas condições medidas. A API tem um componente cíclico
de dois arquivos (`api/serializers.py` e `utils/db_handler.py`, que se importam
mutuamente nas linhas 4 e 2) e o *frontend*, um de três
(`SignInSection.tsx`, `useUser.ts` e `UserContext.tsx`, em que o ciclo se fecha por uma
referência de tipo). Os dois recortes ficam abaixo de 10% e recebem nota 2, então H1.1 tem
sustentação operacional. O *frontend* está exatamente no limite superior da faixa da nota 2:
com um arquivo a mais em ciclo (4/60, 6,67%), cairia para a nota 1. A medida conta arquivos
em ciclos de importação estáticos; não mede o tamanho do ciclo nem o custo de desfazê-lo.

**Q1.2 — Analisabilidade (H1.2).** Sim. Apenas um dos 137 blocos da API tem CC acima de 10
(`GenerateSchedule.post`, em [`views.py` linha 194](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/api/views/views.py#L194), CC 15);
o *frontend* não tem nenhum entre 213. Nos componentes críticos, o maior valor do *scraper* é
7 (`make_disciplines`, `web_scraping.py` linha 200) e o do gerador é 6 (`_valid_schedule`,
linha 153, e `generate`, linha 209). Os quatro recortes ficam na nota 3 e H1.2 tem sustentação
operacional. Esses máximos são diagnóstico e não geram nota adicional (dados em
[`m1-2-maximos-cc.json`](avaliacao/dados/g1/m1-2-maximos-cc.json)). Radon (Python) e ESLint
(TypeScript) contam construções de forma própria; por isso cada recorte é comparado com a
faixa e não com os demais.

**Q1.3 — Modificabilidade (H1.3).** Inconclusivo. O integrante Joaquim entregou os
*patches* de C1 e C2 em 12/11/2026 (commit `18bd323`) e, em mensagem a Kaleb em 15/11/2026,
declarou: "Realizei C1 e C2 em 20 min cada. Cronometrado pelo meu próprio celular". O tempo é, portanto, autodeclaradoe o log de C2 arquivado na `main`
mostra apenas um erro de ambiente. Por isso ele não foi usado como medida.

Em 15/11/2026 a equipe aplicou os dois *patches* sobre o commit inicial do produto e rodou
a suíte completa da API ([relatório e logs](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/manutenibilidade/evidencias/M1.3/verificacao-a-posteriori/RELATORIO.md)). O *patch* de C1 passa
(110 testes, os dois novos incluídos). O de C2 não: dos 114 testes, 9 falham, sendo 8 nos
próprios testes novos (a mensagem de erro, que contém `[1, 3]`, é usada como expressão
regular e não casa) e 1 em teste existente, que passa isolado. Pelo critério de conclusão
da Fase 2, C2 não está concluída. A verificação foi feita fora do Docker do projeto e
não mede tempo.

Pelo item 4 da seção 4.5 da Fase 2, H1.3 fica **inconclusiva** e M1.3 não recebe nota. Se o
*patch* de C2 fosse tomado como entrega final de uma execução válida, seria insucesso e
nota 0, o que contrariaria H1.3; essa leitura não foi adotada porque a execução original não
tem registro, mas fica declarada. Os resultados de M1.1, M1.2 e M1.4 apoiam Q1.3 apenas como
contexto: *scraper* e gerador têm CC máxima baixa (7 e 6) e cobertura alta (97,50% e
99,29%), mas isso não prova que uma mudança seja rápida, correta e sem regressão. Uma
execução cronometrada, registrada e feita por um executor que não conheça as mudanças é
necessária para responder Q1.3.

**Q1.4 — Testabilidade (H1.4).** Sim. A suíte original, com 108 testes, passou (código de
saída 0) e cobre 81,88% das linhas executáveis da API (nota 2), 97,50% do *scraper* e 99,29%
do gerador (nota 3). H1.4 tem sustentação operacional. A cobertura da API está a cerca de
8 pontos percentuais da faixa seguinte (90%). Sete arquivos de produção com linhas
executáveis não executaram nenhuma linha durante a suíte e concentram 211 das 253 linhas
não cobertas: `api/management/commands/updatedb.py` (122), `utils/management/commands/updatemock.py` (36),
`api/views/get_schedules.py` (16), `api/management/commands/initadmin.py` (14),
`core/settings/prod.py` (13), `core/wsgi.py` (5) e `core/asgi.py` (5). Os 42 restantes
estão espalhados em arquivos parcialmente cobertos. A medida é de linhas, sem ramos, e não
indica se as asserções detectariam defeitos.

**G1 — Resumo por subcaracterística.** G1 não recebe nota única, porque falta a medida de
modificabilidade e as notas ordinais não são combinadas.

| Subcaracterística | Hipótese | Resultado | Categoria sintética (menor nota) |
|-------------------|----------|-----------|----------------------------------|
| Modularidade | H1.1 | Sustentada operacionalmente | 2 (API 2; *frontend* 2) |
| Analisabilidade | H1.2 | Sustentada operacionalmente | 3 (API, *frontend*, *scraper* e gerador com 3) |
| Modificabilidade | H1.3 | Inconclusiva (M1.3 não avaliada) | Não atribuída |
| Testabilidade | H1.4 | Sustentada operacionalmente | 2 (API 2; *scraper* 3; gerador 3) |

Nenhum recorte medido contraria uma hipótese. O julgamento global de G1 em relação ao
propósito do produto depende de M1.3 e será tratado na seção 3.

**Limitações.** (a) São indicadores indiretos de manutenibilidade, medidos em um único commit.
(b) Não há medida de testabilidade do *frontend*, que não possui testes. (c) A cobertura é de
linhas, sem ramos. (d) M1.1 e M1.2 foram executadas em ambiente com Python 3.13 e Node 22;
o piloto de 08/11/2026 usou Python 3.12 e Node 24 e deu os mesmos seis valores. (e) M1.4 foi
executada em contêineres `linux/amd64` emulados em um computador com Apple Silicon
(arm64), com PostgreSQL 16.16 e Redis 8.10.3; o resultado coincide com o do piloto
(1.143/1.396, 156/160 e 140/141). Detalhes de ambiente em
[`m1-4-ambiente.txt`](avaliacao/dados/g1/m1-4-ambiente.txt).

## 3. Julgamento da qualidade

<!--
F4-C4: julgamento coerente com o GQM e ligado ao propósito e uso pretendido da Fase 1.
Premissa 1: discutir as relações entre as características com evidências, limitações
e os casos em que os dados não permitem estabelecer relações.
-->

*A preencher.*

## 4. Oportunidades e ação de melhoria

<!--
F4-C5 e seção 3.2 da especificação: oportunidades de melhoria e PELO MENOS UMA ação executada
(protótipo de alta fidelidade, modificação no código, templates técnicos ou proposta de processo),
justificada por evidências da avaliação.
-->

*A preencher.*

---

Anterior: [Fase 3](fase-3.md) · Ver também: [Entregas](entregas.md).