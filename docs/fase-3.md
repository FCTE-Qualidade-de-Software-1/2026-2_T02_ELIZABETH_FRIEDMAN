# Fase 3 — Projetar a avaliação

<!--
Referência: ISO/IEC 25040, atividade 3.
F3-C8: para cada métrica da Fase 2, indicar explicitamente o método e os recursos que a medem.
-->

## 1. Método de avaliação

<!--
F3-C1: método justificado e instruções passo a passo para o avaliador,
garantindo repetibilidade e reprodutibilidade.
-->

Os níveis resumem a [escala da Fase 2, seção 4.1](fase-2.md#41-escala-e-faixas-por-metrica) (0 Insatisfatório, 1 Aceitável, 2 Bom, 3 Excelente); em caso de divergência, vale a Fase 2. A coluna **Card** indica onde o passo a passo é detalhado: #38 (M1.1 a M1.4), #39 (M2 a M5) e #40 (M6 a M9). O passo a passo de M2 a M5 está na [seção 1.1](#11-eficiencia-de-desempenho-m2-a-m5-passo-a-passo); o das demais métricas fica **a detalhar** enquanto os cards #38 e #40 não fecham.

| Métrica (Fase 2) | Método / técnica | Recurso | Ambiente | Nível de pontuação | Card (instruções) |
|---|---|---|---|---|---|
| [M1.1](fase-2.md#m11-arquivos-participantes-de-ciclos-internos) | Análise estática do grafo de importações, por camada; ciclos = componentes fortemente conexos; auditoria manual dos *imports* dos ciclos | pydeps (Python), Madge (TS/TSX), inventário do Git; CSV de registro mínimo | Máquina de avaliação ([2.2](#22-requisitos-do-avaliador)), *commit* `3d399e7` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); sem subir os serviços | Por camada (%): 0 = >10; 1 = >5 a 10; 2 = >0 a 5; 3 = 0 | #38 |
| [M1.2](fase-2.md#m12-blocos-com-complexidade-ciclomatica-elevada) | Análise estática da complexidade ciclomática (CC > 10), por camada e nos componentes críticos; revisão manual do *scraper* e do gerador | Radon (Python); ESLint, regra `complexity`, com *parser* TypeScript; inventário de blocos | Máquina de avaliação ([2.2](#22-requisitos-do-avaliador)), *commit* `3d399e7` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); sem subir os serviços | Por recorte (%): 0 = >20; 1 = >10 a 20; 2 = >5 a 10; 3 = ≤5 | #38 |
| [M1.3](fase-2.md#m13-tempo-para-concluir-uma-mudanca-validada) | Mudança controlada e cronometrada (tarefas C1 e C2), uma execução por tarefa, em cópias independentes do mesmo *commit*; revisor confere o *patch* | Git, cronômetro, fichas de C1 e C2, lista de aceitação, suíte Django, `api/utils/mock/sigaa.html`; executor que não conheça as alterações | Cópias do *commit* `3d399e7`; `db`, `redis` e `api` de pé, sem acesso ao SIGAA ([2.1](#21-versao-avaliada-e-subida-do-ambiente)) | Por tarefa (min): 0 = insucesso, regressão ou >90; 1 = >60 a 90; 2 = >30 a 60; 3 = ≤30 | #38 |
| [M1.4](fase-2.md#m14-cobertura-de-linhas-executaveis-da-api) | Execução da suíte completa da API com cobertura de linhas, total e nos dois componentes críticos | coverage.py 7.3.2 com configuração própria (`source` explícito, sem `pragma: no cover`), relatórios JSON e HTML | Cópia limpa do *commit*, PostgreSQL e Redis locais, *fixtures* existentes, sem SIGAA ([2.1](#21-versao-avaliada-e-subida-do-ambiente)) | Por recorte (%): 0 = <70; 1 = 70 a <80; 2 = 80 a <90; 3 = ≥90 | #38 |
| [M2](fase-2.md#m2-tempo-de-resposta-da-busca-de-disciplinas-p95) | Roteiro automatizado: 2 tentativas de aquecimento + 30 medidas por cenário (busca por nome e por código); P95 pelo posto mais próximo ([Fase 2, 3.1](fase-2.md#31-convencoes-de-medicao-de-eficiencia-de-desempenho)); tempo máximo de espera **10000 ms** | Playwright 1.62.1, Chromium 151.0.7922.34, `Event.timeStamp`/`performance.now()`, CSV; roteiro `m2-busca.spec.ts`; termos de [2.3](#23-massa-de-referencia) | Reprodução local: `db`, `redis`, `api` e `web` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); massa de [2.3](#23-massa-de-referencia); Playwright e Chromium de [2.4](#24-playwright-e-chromium); `workers: 1`, `retries: 0` | P95 (ms): 0 = >2000; 1 = >1000 a 2000; 2 = >500 a 1000; 3 = ≤500 | #39 |
| [M3](fase-2.md#m3-tempo-de-atualizacao-apos-selecao-de-turma-p95) | Mesmo protocolo de M2, com seleção de turma e restauração das seleções entre tentativas; tempo máximo de espera **5000 ms** | Playwright, Chromium, CSV; roteiro `m3-selecao.spec.ts`; turma identificada por código da disciplina e número da turma | Reprodução local: `db`, `redis`, `api` e `web` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); massa de [2.3](#23-massa-de-referencia); Playwright e Chromium de [2.4](#24-playwright-e-chromium); `workers: 1`, `retries: 0` | P95 (ms): 0 = >1000; 1 = >300 a 1000; 2 = >100 a 300; 3 = ≤100 | #39 |
| [M4](fase-2.md#m4-tempo-de-geracao-de-grades-p95) | Mesmo protocolo de M2, com conjuntos fixos de disciplinas e turmas e combinações esperadas conferidas pelo gerador do produto; tempo máximo de espera **30000 ms** | Playwright, Chromium, CSV; roteiro `m4-geracao.spec.ts`; conjuntos M4-A e M4-B da massa de [2.3](#23-massa-de-referencia); `avaliacao/massa/m4_combinacoes.py` | Reprodução local: `db`, `redis`, `api` e `web` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); massa de [2.3](#23-massa-de-referencia); Playwright e Chromium de [2.4](#24-playwright-e-chromium); `workers: 1`, `retries: 0` | P95 (ms): 0 = >10000; 1 = >3000 a 10000; 2 = >1000 a 3000; 3 = ≤1000 | #39 |
| [M5](fase-2.md#m5-tempo-de-retorno-do-salvamento-de-grade-p95) | Mesmo protocolo de M2, separado por modalidade; depois da medição, recarregar a página e recuperar a grade para validar a persistência; tempo máximo de espera **10000 ms**. Conta: coletada. Navegador: **não avaliada** ([4.1](#41-o-que-mudou-em-relacao-a-fase-2-e-por-que), linha 5) | Playwright, Chromium, CSV; roteiro `m5-salvamento.spec.ts`; sessão da conta de teste pelo fluxo do *frontend* com o *token* simulado ([1.1.6](#116-sessao-da-conta-de-teste-m5)) | Reprodução local: `db`, `redis`, `api` e `web` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)); massa de [2.3](#23-massa-de-referencia); Playwright e Chromium de [2.4](#24-playwright-e-chromium); `workers: 1`, `retries: 0` | P95 (ms): 0 = >2000; 1 = >1000 a 2000; 2 = >500 a 1000; 3 = ≤500 | #39 |
| [M6](fase-2.md#m6-sucesso-no-primeiro-uso-apos-exploracao-inicial) | Sessão de primeiro uso, com exploração livre limitada e tarefa padronizada; distribuição entre computador e celular em participantes distintos | Cronômetro, questionário de experiência prévia, ficha CSV, capturas, termo de consentimento; estudantes sem uso prévio | Aplicação em versão fixa com a massa de [2.3](#23-massa-de-referencia); computador e celular reais; Chrome manual ([2.2](#22-requisitos-do-avaliador)); como o celular acessa a instância local é definido no card #40 | Percentual: 0 = <80; 1 = 80 a <90; 2 = 90 a <100; 3 = 100 | #40 |
| [M7](fase-2.md#m7-sucesso-independente-nas-tarefas-de-controle-da-grade) | Tarefas de selecionar, remover e alterar escolhas, com estado inicial restaurado; conferência do estado final | Ficha de observação CSV, capturas antes e depois; Playwright apenas para restaurar o estado | Aplicação em versão fixa com a massa de [2.3](#23-massa-de-referencia); computador e celular reais; Chrome manual ([2.2](#22-requisitos-do-avaliador)); como o celular acessa a instância local é definido no card #40 | Percentual: 0 = <90; 1 = 90 a <95; 2 = 95 a <100; 3 = 100 | #40 |
| [M8](fase-2.md#m8-cobertura-de-protecao-contra-perda-involuntaria-da-grade) | Inspeção pelo avaliador de cada cenário do inventário de ações de risco, com grade de referência restaurada | Inventário de riscos, roteiro de inspeção, CSV, capturas; grades descartáveis | Aplicação em versão fixa com a massa de [2.3](#23-massa-de-referencia); computador e celular reais; Chrome manual ([2.2](#22-requisitos-do-avaliador)); como o celular acessa a instância local é definido no card #40 | Binária: 0 = <100%; 3 = 100% (níveis 1 e 2 não se aplicam) | #40 |
| [M9](fase-2.md#m9-compreensao-dos-estados-e-acoes-da-interface) | Perguntas neutras em pontos de verificação (seleção, geração em andamento e concluída, resultado do salvamento), confrontadas com o gabarito | Gabarito de estados e ações, ficha CSV, capturas da interface no instante da pergunta | Aplicação em versão fixa com a massa de [2.3](#23-massa-de-referencia); computador e celular reais; Chrome manual ([2.2](#22-requisitos-do-avaliador)); como o celular acessa a instância local é definido no card #40 | Percentual: 0 = <90; 1 = 90 a <95; 2 = 95 a <100; 3 = 100 | #40 |

### 1.1 Eficiência de desempenho (M2 a M5): passo a passo

Esta seção detalha o método de M2 a M5 (card #39). Ela segue a
[Fase 2, seção 3.1](fase-2.md#31-convencoes-de-medicao-de-eficiencia-de-desempenho) e não
altera métricas, fórmulas, faixas nem limites $L_j$. Os roteiros ficam em
[`avaliacao/e2e/tests/desempenho/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/e2e/tests/desempenho).
Há um arquivo por métrica (`m2-busca`, `m3-selecao`, `m4-geracao`, `m5-salvamento`) e um
*helper* comum (`medicao.ts`). As citações do código do produto apontam para o *commit*
`3d399e7`.

**Por que este método:** a Fase 2 pede o intervalo entre a ação do usuário e o resultado
visível, medido no navegador com um único relógio monotônico. Um roteiro Playwright faz o
mesmo clique em todas as tentativas, mede os dois instantes dentro da página e grava cada
tentativa no CSV. Por isso o procedimento pode ser repetido por outro avaliador sem
depender de cronômetro manual. O tempo de uma requisição HTTP isolada não é usado.

#### 1.1.1 Pré-condições e comandos

| # | Passo | Comando / verificação |
|---|-------|-----------------------|
| 1 | Subir `db`, `redis`, `api` e `web` no *commit* `3d399e7` ([2.1](#21-versao-avaliada-e-subida-do-ambiente)) | `curl -s http://localhost:8000/courses/year-period/` devolve o JSON; `curl -s -o /dev/null -w '%{http_code}' http://localhost:3000` devolve `200` |
| 2 | Carregar a massa de referência ([2.3](#23-massa-de-referencia)) | `docker exec -i django-api python3 manage.py shell < …/avaliacao/massa/seed_referencia.py` → `massa carregada: … 14 disciplinas, 43 turmas` |
| 3 | Conferir as combinações de M4 com o gerador do produto ([1.1.2](#112-cenarios-fixos)) | `docker exec -i django-api python3 manage.py shell < …/avaliacao/massa/m4_combinacoes.py` → `m4-a: … 1 válidas`; `m4-b: … 128 candidatas, 76 válidas, exibidas pela API: 5` |
| 4 | Instalar o Playwright fixado ([2.4](#24-playwright-e-chromium)) | `cd avaliacao/e2e && npm ci` |
| 5 | Somente na coleta formal: parar contêineres de outros projetos e registrar a máquina ([2.2](#22-requisitos-do-avaliador)) | `docker ps`, `free -h` (o roteiro também grava ambos em `metadados.json`) |
| 6 | Piloto (verificação do método, fora da amostra) | `npm run piloto` (todos) ou `npm run piloto -- m2-busca` (um roteiro) |
| 7 | Coleta formal (issue #43) | `npm run coleta` |

`npx playwright test` sem variáveis roda **só o *smoke***. O projeto `piloto` existe apenas
com `PILOTO=1`, e o `coleta` apenas com `COLETA=1`; os *scripts* dos passos 6 e 7 definem
essas variáveis (`playwright.config.ts`). O roteiro de M5 lê o `GOOGLE_OAUTH2_MOCK_TOKEN` de
`api/.env` do produto. O roteiro espera o clone do produto ([2.1](#21-versao-avaliada-e-subida-do-ambiente))
como pasta irmã deste repositório; outro local pode ser indicado em `PRODUTO_DIR`.

| Item | Piloto (`npm run piloto`) | Coleta (`npm run coleta`) |
|------|---------------------------|---------------------------|
| Tentativas por cenário | 1 de aquecimento + 3 medidas (`PILOTO_MEDIDAS` altera as medidas) | 2 de aquecimento + 30 medidas |
| Tempo máximo de espera | Tabela da [1.1.4](#114-tempo-maximo-de-espera); `TMAX_MS` pode reduzi-lo para forçar expiração | Tabela da [1.1.4](#114-tempo-maximo-de-espera); `TMAX_MS` é recusado |
| Pasta de saída | `avaliacao/resultados/desempenho/piloto/<rodada>/` | `avaliacao/resultados/desempenho/coleta/<rodada>/` (fora do Git até a análise da #43) |
| Execução | Sequencial (`workers: 1`), `retries: 0`, sem *trace*, vídeo nem captura automática | Igual |

A `<rodada>` é a data e hora do início (`AAAAMMDD-HHMM`) ou o valor de `RODADA`. Uma rodada
com `TMAX_MS` recebe o sufixo `-tmax<valor>`.

#### 1.1.2 Cenários fixos

Os resultados esperados vêm da API local com a massa de [2.3](#23-massa-de-referencia), ano
e período correntes (2026/2 em 12/11/2026). As turmas são identificadas por **código da
disciplina e número da turma**. O roteiro consulta `GET /courses/?search=<código>`, acha a
posição da turma pelo campo `_class` (o *frontend* exibe as turmas nessa ordem,
[DisciplineFragment.tsx#L42](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/AsideSchedulePopUp/DisciplineFragment.tsx#L42))
e confere se o horário exibido na linha é o horário da turma. O `id` nunca é fixado, porque
muda a cada carga.

| Cenário | Métrica | Preparação (fora do intervalo) | Ação medida | Resultado esperado |
|---------|---------|--------------------------------|-------------|--------------------|
| `m2-nome` | M2 | Painel "Buscar matéria" aberto, período corrente, termo `seminario` digitado | Clique em pesquisar | 3 disciplinas: `PPGPS0156`, `PPGPS0157`, `PPGPS2989` |
| `m2-codigo` | M2 | Idem, termo `PPGPS2475` | Clique em pesquisar | 1 disciplina: `PPGPS2475` |
| `m3-sem-selecao` | M3 | Nenhuma seleção; `PPGPS2475` buscada e expandida | Adicionar `PPGPS2475/01` | Turma marcada, 1 cartão "Código:", "Gerar Grade" habilitado |
| `m3-com-selecao` | M3 | `PPGPS0156/02` já selecionada; `PPGPS0156` expandida | Adicionar `PPGPS0156/04` | Turma marcada, 2 cartões "Código:", "Gerar Grade" habilitado |
| `m4-a` | M4 | 2 disciplinas, 2 turmas: `PPGPS2475/01`, `PPGPS2939/01`; modal de preferências aberto (1/1/1) | Clique em "Gerar" | 1 combinação candidata, 1 válida, **1 grade exibida** |
| `m4-b` | M4 | 6 disciplinas, 16 turmas: `PPGPS0156/02,03,04,05`, `PPGPS0161/01,02,03,04`, `PPGPS0163/01,02`, `PPGPS0165/01,02,03,05`, `PPGPS2475/01`, `PPGPS2939/01`; preferências 1/1/1 | Clique em "Gerar" | 128 candidatas, **76 válidas** pelo `ScheduleGenerator`, **5 grades exibidas** |
| `m5-conta` | M5 | Conta de teste autenticada, nenhuma grade na nuvem, uma grade local fixa (`PPGPS2475/01` + `PPGPS2939/01`, gerada pela API) | Clique em "ícone de upload" | Toast "Grade salva com sucesso!"; depois de recarregar, "Grades nuvem" com 1 grade |
| `m5-navegador` | M5 | n/a | n/a | **Não avaliada** ([4.1](#41-o-que-mudou-em-relacao-a-fase-2-e-por-que), linha 5) |

**Limitação de M4-B.** As 76 combinações válidas foram contadas pelo gerador do próprio
produto (`m4_combinacoes.py`, executado em 12/11/2026 com a massa recarregada). A API,
porém, devolve no máximo **5** grades
([views.py#L27](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/api/views/views.py#L27),
[#L245](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/api/views/views.py#L245)).
Assim, M4-B mede o processamento de 128 candidatas, mas a apresentação é sempre de 5 grades.
A comparação entre M4-A e M4-B diz pouco sobre a sensibilidade ao volume: o que cresce é o
trabalho do gerador, não o que a interface mostra. O tamanho do conjunto também é limitado
pelo produto (até 4 turmas por disciplina e 11 disciplinas,
[schedule_generator.py#L7-L10](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/utils/schedule_generator.py#L7-L10)).

#### 1.1.3 Ações, seletores e sinais de conclusão

Todos os seletores vêm do código abaixo e foram conferidos na página em execução em
12/11/2026.

| Métrica | Elemento clicado (início) | Sinal de conclusão (fim) | Erro | Fonte no produto |
|---------|---------------------------|--------------------------|------|------------------|
| M2 | Botão de envio com a imagem `alt="ícone de pesquisa"`. Não há busca automática nem *debounce*: digitar só altera o estado; a busca roda no `submit` | Os botões `"<nome> - <código>"` da lista de resultados estão visíveis e habilitados, com **exatamente** os códigos esperados. A lista é substituída num único `setState`, então não há resultado parcial | Qualquer *toast* (ex.: "Nenhuma disciplina encontrada") ou um conjunto diferente do esperado | [InputForm.tsx#L24-L48](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/AsideSchedulePopUp/Form/InputForm.tsx#L24-L48), [DisciplineFragment.tsx#L28-L38](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/AsideSchedulePopUp/DisciplineFragment.tsx#L28-L38), [searchDiscipline.ts#L38-L46](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/utils/api/searchDiscipline.ts#L38-L46) |
| M3 | Botão com a imagem `alt="ícone adicionar matéria"` na linha da turma | As três condições juntas: (a) a imagem da mesma linha passa a `alt="ícone remover matéria"`; (b) a página tem o número esperado de cartões "Código:"; (c) "Gerar Grade" está habilitado | *Toast* (ex.: limite de turmas) ou cartões a mais | [ClassInfoBox.tsx#L20-L49](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/AsideSchedulePopUp/ClassInfoBox.tsx#L20-L49), [DisciplineBox.tsx#L38](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/DisciplineBox.tsx#L38), [GenerateScheduleButton.tsx#L105](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/home/components/GenerateScheduleButton.tsx#L105) |
| M4 | Botão "Gerar" do modal "Período de preferência" | Em `/schedules/mygrades`, sem a tela de carregamento, com o título "Grades locais" e o número esperado de grades (também no `localStorage`). Inclui a espera fixa de **500 ms** que o produto impõe antes de esconder o carregamento | *Toast* (ex.: "Não há horários disponíveis…") ou um número de grades diferente | [GenerateScheduleButton.tsx#L46-L75](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/home/components/GenerateScheduleButton.tsx#L46-L75), [layout.tsx#L108-L112](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/layout.tsx#L108-L112), [mygrades/page.tsx#L7-L22](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/mygrades/page.tsx#L7-L22) |
| M5 (conta) | Botão com a imagem `alt="ícone de upload"` da grade local; só aparece para usuário autenticado | *Toast* "Grade salva com sucesso!", emitido depois do `201` da API | Qualquer outro *toast*; ou a grade ausente em "Grades nuvem" depois de recarregar (verificação de persistência, fora do intervalo) | [SchedulePreview.tsx#L112](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/SchedulePreview/SchedulePreview.tsx#L112), [#L134-L163](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/SchedulePreview/SchedulePreview.tsx#L134-L163) |

#### 1.1.4 Tempo máximo de espera

| Operação | $L_j$ (Fase 2, 4.1) | Tempo máximo de espera | Critério |
|----------|---------------------|------------------------|----------|
| M2 (busca) | 2000 ms | **10000 ms** | 5 × $L_2$ |
| M3 (seleção) | 1000 ms | **5000 ms** | 5 × $L_3$ |
| M4 (geração) | 10000 ms | **30000 ms** | 3 × $L_4$ |
| M5 (salvamento) | 2000 ms | **10000 ms** | 5 × $L_5$ |

Os valores são uma escolha operacional da equipe, fixada antes da coleta, e não um requisito
normativo. Todos são estritamente maiores que $L_j$, como exige a Fase 2, seção 3.1. Pela
regra 2 da [Fase 2, seção 4.3](fase-2.md#43-regras-de-aplicacao-e-julgamento-de-eficiencia-m2m5),
uma expiração já leva o cenário a **Insatisfatório (0)**. Por isso o prazo é folgado: uma
operação lenta, mas concluída, entra como **sucesso** com o tempo real e não vira expiração,
o que mantém lentidão e falha separadas. Para M4 o múltiplo é menor porque
$L_4 = 10000$ ms já corresponde ao limite de atenção de Nielsen.

#### 1.1.5 Medição dos instantes e restauração do estado

**Instantes** (`medicao.ts`):

- **Inicial:** `Event.timeStamp` do clique **confiável** (`isTrusted`) no elemento da
  [1.1.3](#113-acoes-seletores-e-sinais-de-conclusao), capturado por um *listener* na
  própria página. Esse valor usa a mesma origem e o mesmo relógio de `performance.now()`.
- **Final:** `performance.now()` no primeiro quadro (`requestAnimationFrame`) em que o sinal
  de conclusão está completo. A espera (`page.waitForFunction`, `polling: 'raf'`) é armada
  **antes** do clique e só aceita o sinal depois que o instante inicial existe.
- **Duração:** instante final − instante inicial, gravada só para tentativas com sucesso.
- **Expiração:** detectada no mesmo relógio, quando `performance.now() − início` passa do
  tempo máximo de espera. Uma guarda externa do Playwright (tempo máximo + 5 s) cobre o caso
  de a página parar de responder.

**Estado limpo antes do clique.** Antes de cada clique medido, o roteiro confere que não há
sinal de uma tentativa anterior. M2: nenhum resultado e nenhum *toast*. M3: o número esperado
de cartões e de turmas marcadas. M4: nenhuma grade no `localStorage` e a página inicial
aberta. M5: nenhum *toast*, nenhuma grade na nuvem e uma única grade local. Se algo estiver
fora do esperado, a tentativa é registrada como **erro** de preparação, sem instante inicial,
e a série segue. O sinal de fim também é recusado se não for posterior ao instante inicial.

**Limitações de precisão:**

- O fim é marcado no início do quadro em que o estado já está no DOM, pouco antes da pintura.
  O erro é de até cerca de 1 quadro.
- O intervalo entre quadros foi medido pelo roteiro em todas as séries do piloto: mediana
  **16,7 ms** (≈ 60 Hz), registrada em `metadados.json`.
- Os instantes são gravados com 0,1 ms. A resolução real do relógio no Chromium sem
  isolamento de origem não foi verificada (**a confirmar**), mas fica bem abaixo da
  granularidade do quadro.
- Essa granularidade é pequena perante os cortes da Fase 2 (o menor é 100 ms, em M3), mas
  tempos de 1 a 2 quadros, como os do piloto de M2 e M3, não podem ser separados com
  resolução melhor que cerca de 17 ms.
- As medidas valem para o Chromium *headless* e o *frontend* em modo de desenvolvimento
  (`npm run dev`), como descrito em [2.1](#21-versao-avaliada-e-subida-do-ambiente).

**Restauração entre tentativas** (fora do intervalo medido). Um contexto de navegador por
cenário, o que mantém a mesma política de *cache* em todas as tentativas depois do
aquecimento. Em cada tentativa:

| Métrica | Restauração |
|---------|-------------|
| M2 | Recarregar `/schedules/home`; a lista de resultados e os *toasts* somem |
| M3 | Recarregar `/schedules/home`; as seleções só existem no estado do React ([SelectedClassesContext.tsx#L44](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/contexts/SelectedClassesContext/SelectedClassesContext.tsx#L44)); refazer as seleções anteriores do cenário |
| M4 | Remover `localStorage['schedules']` e recarregar, porque a geração **soma** grades às já existentes ([SchedulesContext.tsx#L52-L63](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/contexts/SchedulesContext.tsx#L52-L63)); refazer as seleções do conjunto |
| M5 | Apagar as grades da conta (`DELETE /courses/schedules/<id>/`; a API limita 10 por conta, [save_schedule.py#L15](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/api/views/save_schedule.py#L15)), gravar a grade local fixa e recarregar |

A massa de disciplinas e turmas só é lida por M2, M3 e M4. Ela é recarregada pelo
`seed_referencia.py` antes de cada rodada (passo 2).

#### 1.1.6 Sessão da conta de teste (M5)

O *frontend* usa `POST /users/register/google/`: ele lê o `access_token` do fragmento da
URL, que normalmente é o retorno do Google, e o envia à API
([retrieveAccessToken.ts#L4-L15](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/utils/retrieveAccessToken.ts#L4-L15),
[SignInSection.tsx#L29-L49](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/components/SignInSection.tsx#L29-L49)).

- A API grava o cookie `refresh` (`HttpOnly; Secure; SameSite=Lax`,
  [decorators.py#L14-L20](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/api/users/simplejwt/decorators.py#L14-L20)).
- A cada carga de página, o `UserContext` obtém o `access` por `POST /users/login/`
  ([UserContext.tsx#L44-L59](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/contexts/UserContext.tsx#L44-L59)).
  O `access` fica só na memória.

O roteiro abre `http://localhost:3000/#access_token=<GOOGLE_OAUTH2_MOCK_TOKEN>` uma vez, antes
da série. A partir daí o login segue o fluxo do próprio *frontend*, sem cookie injetado por
fora. **Confirmado no piloto de 12/11/2026:** `register/google` respondeu `200`, o Chromium
aceitou o cookie `refresh` em `http://localhost` (`secure=true, httpOnly=true,
sameSite=Lax`) e o `/users/login/` funcionou depois de recarregar. O caminho alternativo
(`context.addCookies`) não foi necessário.

O *token* simulado nunca é gravado. Ele é lido de `api/.env` em tempo de execução, e o
roteiro o remove de qualquer texto que grava ou imprime. Os projetos de desempenho não usam
*trace*, e as capturas mostram só a área da página, sem a URL. O piloto foi conferido: o
*token* não aparece em nenhum arquivo da rodada.

#### 1.1.7 Registro e cálculo do P95

Cada cenário gera um CSV (`<cenário>.csv`) com as colunas da Fase 2, seção 3.1, nesta ordem:
`métrica, cenário, ambiente, versão do sistema, data, número da tentativa, aquecimento,
instante inicial, instante final, duração (ms), estado, referência à evidência`.

- **Instantes:** em ms, com uma casa decimal, no relógio da página. A origem muda a cada
  recarga, então só a diferença dentro de uma linha tem significado.
- **Estado:** `sucesso`, `erro` ou `expiração`.
- **Erro e expiração:** a duração fica **vazia**, nunca zero. O instante final registra o
  momento em que a falha foi detectada.
- **Aquecimento:** `sim` ou `não`. A numeração das tentativas recomeça em 1 nas medidas.
- **Referência à evidência:** aponta para a linha da tentativa em `evidencias.jsonl` (estado,
  motivo e o que foi observado, como os códigos exibidos ou o número de grades). Há também
  uma captura (`evidencias/<cenário>-<n>.png`) da 1ª medida e de toda tentativa sem sucesso.
  Em M5, a captura é feita depois da verificação de persistência.

O `metadados.json` da rodada registra:

- *commit* do produto e ausência de alterações rastreadas;
- versões do Playwright e do Chromium, modo *headless* e dispositivo;
- ano/período da massa (`/courses/year-period/`);
- saída de `docker ps` e `free -h`;
- tempo máximo de espera e $L_j$ por cenário, intervalo entre quadros e esperados de cada cenário.

**P95 pelo posto mais próximo** (Fase 2, seção 3.1): usar só as linhas com `aquecimento =
não`, contar sucessos, erros e expirações, ordenar as durações dos sucessos e tomar a posição
$\lceil 0{,}95\,n \rceil$ (com 30 sucessos, a 29ª). Sem sucessos, o P95 é **não calculável**.
O julgamento segue a [Fase 2, seção 4.3](fase-2.md#43-regras-de-aplicacao-e-julgamento-de-eficiencia-m2m5).

```bash
python3 - avaliacao/resultados/desempenho/coleta/<rodada>/m2-nome.csv <<'FIM'
import csv, math, sys
linhas = [l for l in csv.DictReader(open(sys.argv[1], encoding='utf-8')) if l['aquecimento'] == 'não']
estados = {e: sum(l['estado'] == e for l in linhas) for e in ('sucesso', 'erro', 'expiração')}
t = sorted(float(l['duração (ms)']) for l in linhas if l['estado'] == 'sucesso')
p95 = t[math.ceil(0.95 * len(t)) - 1] if t else 'não calculável'
print(len(linhas), 'medidas', estados, 'P95 =', p95)
FIM
```

#### 1.1.8 Piloto (12/11/2026)

O piloto verifica o método e **não integra** as 30 tentativas da coleta formal (Fase 2,
seção 3.2, pendência 4). Os valores abaixo não são resultados de M2 a M5: são poucas
tentativas e não há P95.

- **Rodada:** `20261112-piloto`.
- **Condições:** todos os cenários com 1 aquecimento e 3 medidas; massa recarregada pelo
  *seed* antes da rodada (2026/2).
- **Máquina:** os contêineres `n8n` e `instancia_postgres`, de outros projetos, estavam em
  execução e foram registrados em `metadados.json`; para o piloto não foram parados.
- **Arquivos:**
  [`avaliacao/resultados/desempenho/piloto/20261112-piloto/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/resultados/desempenho/piloto/20261112-piloto).

| Cenário | Aquecimento | Medidas | Estados (medidas) | Durações das medidas (ms) | CSV |
|---------|-------------|---------|-------------------|---------------------------|-----|
| `m2-nome` | 1 (sucesso) | 3 | 3 sucessos | 30,2; 30,7; 31,7 | `m2-nome.csv` |
| `m2-codigo` | 1 (sucesso) | 3 | 3 sucessos | 30,0; 31,1; 47,5 | `m2-codigo.csv` |
| `m3-sem-selecao` | 1 (sucesso) | 3 | 3 sucessos | 31,0; 30,4; 31,2 | `m3-sem-selecao.csv` |
| `m3-com-selecao` | 1 (sucesso) | 3 | 3 sucessos | 29,7; 30,7; 30,9 | `m3-com-selecao.csv` |
| `m4-a` | 1 (sucesso) | 3 | 3 sucessos | 617,4; 623,1; 636,6 | `m4-a.csv` |
| `m4-b` | 1 (sucesso) | 3 | 3 sucessos | 671,7; 732,9; 676,1 | `m4-b.csv` |
| `m5-conta` | 1 (sucesso) | 3 | 3 sucessos; persistência verificada nas 4 tentativas | 48,1; 33,4; 49,6 | `m5-conta.csv` |
| `m5-navegador` | n/a | n/a | não avaliada | n/a | n/a |

**Conferências feitas no piloto:**

- Os 7 CSVs têm exatamente o cabeçalho da Fase 2.
- Todas as linhas com sucesso têm duração > 0 e instante final maior que o inicial.
- As linhas de aquecimento estão marcadas com `sim`.
- O *token* não aparece em nenhum arquivo da rodada.
- **Expiração forçada:** rodada `20261112-piloto-tmax5`, só `m2-nome`, com `TMAX_MS=5`. As 4
  tentativas viraram linhas `expiração`, com duração vazia e evidência, e a série foi até o
  fim sem nova tentativa.
- Com `COLETA=1`, o mesmo `TMAX_MS` é recusado antes de qualquer gravação.

Em M4, cerca de 500 ms de cada duração vêm da espera fixa do produto
([GenerateScheduleButton.tsx#L66-L68](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/home/components/GenerateScheduleButton.tsx#L66-L68)),
que faz parte do que o estudante espera.

## 2. Recursos e ambiente de avaliação

<!--
F3-C2: hardware e software necessários, massa de dados (dados-exemplo) quando pertinente,
perfil exigido dos avaliadores/usuários (conhecimento em informática e no domínio).
-->

Esta seção descreve o ambiente local usado nas métricas que dependem da reprodução do
produto (M1.3, M1.4 e M2–M5, ver [Fase 2](fase-2.md)). Cada versão traz a fonte de onde
foi lida: um arquivo do repositório do produto ou a saída de um comando executado na
máquina de avaliação em 03/11/2026. O que ainda não foi confirmado está marcado como
**a confirmar**.

### 2.1 Versão avaliada e subida do ambiente

**Produto:** [unb-mds/2023-2-SuaGradeUnB](https://github.com/unb-mds/2023-2-SuaGradeUnB),
branch `main`.

| Campo | Valor | Fonte |
|-------|-------|-------|
| *Commit* (curto) | `3d399e7` | `git log -1 --format=%h 3d399e7` |
| *Commit* (completo) | `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360` | `git log -1 --format=%H 3d399e7` |
| Data | 15/02/2026 10:44:50 -0300 | `git log -1 --format=%ci 3d399e7` |
| Autor | Caio Felipe | `git log -1 --format=%an 3d399e7` |
| Mensagem | `Merge pull request #250 from Marcosatc147/main` | `git log -1 --format=%s 3d399e7` |

**Fixar a versão:**

```bash
git clone https://github.com/unb-mds/2023-2-SuaGradeUnB.git
cd 2023-2-SuaGradeUnB
git checkout 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
git log -1 --format='%H %ci'   # deve mostrar 3d399e7… 2026-02-15 10:44:50 -0300
```

**Serviços** (fonte: `docker-compose.yml`, `docker/Dockerfile`, `docker/Dockerfile.web`):

| Serviço (`compose`) | Contêiner | Imagem / base | Porta no host | Papel |
|---------------------|-----------|---------------|---------------|-------|
| `db` | `postgresql` | `postgres:16` | não publicada | PostgreSQL; volume `postgres_data` |
| `redis` | `rediscache` | `redis:alpine` | não publicada | *Cache* e sessões |
| `api` | `django-api` | `python:3.11.6-alpine3.18` (build) | `8000` | API Django (`runserver 0.0.0.0:8000`) |
| `web` | `nextjs-web` | `node:20.9.0-alpine3.18` (build) | `3000` | *Frontend* Next.js (`npm run dev`) |

As tags `postgres:16` e `redis:alpine` não são fixas e podem mudar entre as execuções. Por
isso, o digest de cada imagem deve ser registrado depois do primeiro `pull`:
`docker image inspect --format '{{index .RepoDigests 0}}' postgres:16 redis:alpine`.
Versões registradas na máquina de avaliação em 03/11/2026:

| Componente | Versão em execução | Fonte |
|------------|--------------------|-------|
| PostgreSQL | 16.11, `postgres@sha256:d4c3314b2dd74ff23cd6cd07e4d7e737cb6ef791c22a7cbd744cfbfb4815df72` | `docker exec postgresql postgres --version`; `docker image inspect` |
| Redis | 8.10.3, `redis@sha256:21090af93f8324db2f0f0f4f38a7c60369d47d917e000c3423d89d2ae2883537` | `docker exec rediscache redis-server --version`; `docker image inspect` |
| Python (API) | 3.11.6; Django 5.1.5 | `docker exec django-api python3 --version`; log do `runserver` |
| Node / npm (*frontend*) | v20.9.0 / 10.1.0; Next.js 14.2.21 | `docker exec nextjs-web node --version`, `npm --version`, `node -p "require('next/package.json').version"` |

**Variáveis de ambiente.** O alvo `make config` (fonte: `Makefile`) copia
`api/.env.example` → `api/.env` e `web/.env.example` → `web/.env.local`. Em seguida, gera
valores aleatórios para `DJANGO_SECRET_KEY` (`scripts/env.sh`) e `GOOGLE_OAUTH2_MOCK_TOKEN`
(`scripts/config.sh`). Os outros valores ficam como no exemplo:

| Arquivo | Variável | Valor do `.env.example` | Uso |
|---------|----------|-------------------------|-----|
| `api/.env` | `DJANGO_SECRET_KEY` | `your_secret_key` → aleatório | Chave do Django |
| `api/.env` | `SETTINGS_FILE_PATH` | `core.settings.dev` | `DEBUG=True`, CORS liberado |
| `api/.env` | `DB_ENGINE`, `DB_NAME`, `DB_USERNAME`, `DB_PASSWORD`, `DB_HOSTNAME`, `DB_PORT` | `django.db.backends.postgresql`, `postgres`, `suagradeunb`, `suagradeunb`, `db`, `5432` | Conexão da API |
| `api/.env` | `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | `postgres`, `suagradeunb`, `suagradeunb` | Inicialização do contêiner `db` |
| `api/.env` | `REDIS_CACHE_LOCATION` | `redis://redis:6379/1` | *Cache* |
| `api/.env` | `ADMIN_NAME`, `ADMIN_PASS`, `ADMIN_EMAIL` | `admin`, `admin`, `admin@gmail.com` | Superusuário criado por `initadmin` |
| `api/.env` | `GOOGLE_OAUTH2_MOCK_TOKEN` | `your_google_oauth2_mock_token` → aleatório | Login simulado na API (ver 2.3) |
| `web/.env.local` | `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Endereço da API usado pelo navegador |
| `web/.env.local` | `NEXT_PUBLIC_GOOGLE_OAUTH_URL` | `https://accounts.google.com/o/oauth2/v2/auth` | Login Google |
| `web/.env.local` | `NEXT_PUBLIC_GOOGLE_OAUTH_CLIENT_ID` | `your_client_id` | Mantido sem valor real; o login Google fica fora do escopo ([Fase 1, Tabela 12](fase-1.md#62-o-que-fica-fora-do-escopo)) |

**Passo a passo:**

```bash
# 1. Configurar o ambiente (cria api/.env e web/.env.local)
make config

# 2. Construir e subir os quatro serviços em segundo plano
docker compose up --build -d

# 3. Acompanhar a inicialização da API
docker compose logs -f api
```

**Ordem de inicialização.** O `depends_on` do compose sobe `db` e `redis` antes de `api`, e
`api` antes de `web`. O `api/config/entrypoint.sh` espera a porta do PostgreSQL responder
(`nc -z $DB_HOSTNAME $DB_PORT`). Depois executa `python3 manage.py migrate` e
`python3 manage.py initadmin`, e só então inicia o servidor. A API está pronta quando o log
mostra `PostgreSQL iniciado`, `Migrando banco de dados...` e a linha de escuta do
`runserver`.

**Verificação de cada serviço:**

| Serviço | Comando | Resultado esperado |
|---------|---------|--------------------|
| Todos | `docker compose ps` | Quatro contêineres com estado `running` |
| PostgreSQL | `docker exec postgresql pg_isready -U suagradeunb` | `accepting connections` |
| Redis | `docker exec rediscache redis-cli ping` | `PONG` |
| API | `curl -s http://localhost:8000/courses/year-period/` | JSON `{"year/period": [...]}` com o período atual e o seguinte (rota em `api/api/urls.py`) |
| *Frontend* | `curl -s -o /dev/null -w '%{http_code}\n' http://localhost:3000` | `200` |

Para encerrar sem apagar dados, use `docker compose stop` ou `docker compose down`. **Não**
use `docker compose down -v` (alvo `make stop-v`), porque esse comando apaga o volume do
banco.

**Execução nesta máquina (03/11/2026):** depois de `make config`, o
`docker compose up --build -d` construiu as imagens `2023-2-suagradeunb-api` e
`2023-2-suagradeunb-web`, criou o volume `2023-2-suagradeunb_postgres_data` e iniciou os
quatro contêineres em cerca de 3 min (`time`). Antes da subida, as portas `3000` e `8000` do
host estavam livres (`ss -ltn`). As portas `5432` e `6379` estão em uso por outros serviços
da máquina, mas isso não causa conflito porque o compose não publica essas portas.
Resultados das verificações:

| Verificação | Saída obtida |
|-------------|--------------|
| `docker compose ps` | `api`, `web`, `db` e `redis` em `running`; `0.0.0.0:8000->8000/tcp` e `0.0.0.0:3000->3000/tcp` |
| `docker compose logs api` | `PostgreSQL iniciado`, todas as migrações `OK`, `Conta do usuário admin será criada!`, `System check identified no issues (0 silenced).`, `Starting development server at http://0.0.0.0:8000/` |
| `pg_isready` | `/var/run/postgresql:5432 - accepting connections` |
| `redis-cli ping` | `PONG` |
| `/courses/year-period/` | `{"year/period":["2026/2","2027/1"]}` |
| `http://localhost:3000` | `200` |

Uma reprodução anterior, de 17/10/2026, está na
[Fase 1, Seção 3.6](fase-1.md#36-reproducao-local-e-implicacoes-para-a-avaliacao).

### 2.2 Requisitos do avaliador

O projeto declara os pré-requisitos em `docs/executing.md`. Os dados da máquina de
avaliação foram coletados em 03/11/2026.

| Item | Mínimo exigido pelo projeto (fonte) | Máquina usada na avaliação (comando) |
|------|-------------------------------------|--------------------------------------|
| Sistema operacional | Não declarado | Ubuntu 24.04.2 LTS (`lsb_release -a`); *kernel* Linux 7.0.0-38-generic x86_64 (`uname -a`) |
| Equipamento | Não declarado | Modelo `550XDA` (`/sys/devices/virtual/dmi/id/product_name`) |
| CPU | Não declarado | Intel Core i5-1135G7 @ 2.40 GHz, 4 núcleos / 8 *threads* (`lscpu`) |
| Memória | Não declarado | 7,5 GiB de RAM + 4,0 GiB de *swap* (`free -h`) |
| Disco | Não declarado | 233 GB, 73 GB livres (`df -h ~`) |
| Docker Engine | v24.0.6 ou superior (`docs/executing.md`) | 29.1.2 (`docker --version`) |
| Docker Compose | v2.21.0 ou superior (`docs/executing.md`) | v2.40.3 (`docker compose version`) |
| GNU Make | 4.3 ou superior (`docs/executing.md`) | 4.3 (`make --version`) |
| Python (host) | 3.11.6 (`docs/executing.md`, `api/runtime.txt`) | 3.12.3 (`python3 --version`); a API roda no contêiner `python:3.11.6-alpine3.18` |
| Node / npm (host) | Node 20.9.0 / npm 10.1.0 (`docs/executing.md`) | Node v22.22.3 / npm 11.16.0 (`node --version`, `npm --version`); o *frontend* roda no contêiner `node:20.9.0-alpine3.18` |
| Git | Não declarado | 2.43.0 (`git --version`) |
| Navegador (automação) | Não declarado | Chromium do Playwright, ver 2.4 |
| Navegador (manual) | Não declarado | Google Chrome 153.0.8010.36 (`google-chrome --version`) |

**Observações sobre a máquina:**

- Python e Node do host diferem do mínimo declarado, mas isso não afeta a execução: API e
  *frontend* rodam nos contêineres com as versões fixadas nos Dockerfiles. As versões do host
  só importam para `make config` (usa `python3`) e para o Playwright (usa Node).
- No momento da coleta havia outros contêineres em execução na máquina (de outros
  projetos), e a memória disponível era de 795 MiB (`free -h`). Para as métricas de
  eficiência de desempenho, esses contêineres devem ser parados antes da medição, e o
  `docker ps` e o `free -h` devem ser registrados junto com cada coleta.

**Perfil do avaliador:** saber usar terminal Linux, Git e Docker Compose, e conhecer o
básico de Playwright/TypeScript para rodar e ler os roteiros. Para as tarefas não é preciso
conhecer o domínio (matrícula na UnB) além do descrito na [Fase 1](fase-1.md).

### 2.3 Massa de referência

**O que o repositório oferece:**

- Não há *fixtures* nem *seed* de disciplinas e turmas. O comando
  `python3 manage.py updatedb` (`api/api/management/commands/updatedb.py`; alvos
  `make updatedb-all` e `make deletedb-all`) baixa os dados do SIGAA em produção. Com isso o
  resultado muda a cada execução e depende de um serviço externo, o que não serve como massa
  fixa.
- O próprio projeto guarda uma página do SIGAA usada nos testes, em
  `api/utils/mock/sigaa.html` (departamento `1499`, 2023/2, conforme
  `api/utils/mock/infos.json`), com SHA-256
  `17ae00b1edcc0348c3dff66ef7709be26f8f3f2f5efc244ee65d54a198dead65` (`sha256sum`).
  O *parser* do próprio produto (`DisciplineWebScraper.make_web_scraping_of_disciplines`)
  extrai desse arquivo, sem acesso à rede, **14 disciplinas e 43 turmas** do Programa de
  Pós-Graduação em Política Social (códigos `PPGPS*`).
- `initadmin` cria o superusuário `admin` / `admin` (valores do `.env.example`).
- Usuário de teste: um `POST /users/register/google/` com
  `{"access_token": "<GOOGLE_OAUTH2_MOCK_TOKEN>"}` cria ou autentica o usuário
  `user@email.com` sem chamar o Google (`api/users/backends/google.py`). Correção feita no
  card #39: o *frontend* **usa** essa rota. Ele envia o `access_token` recebido no fragmento
  da URL, que normalmente vem do Google. Assim, o roteiro de M5 autentica a conta pelo
  próprio fluxo do *frontend*, como descrito na
  [seção 1.1.6](#116-sessao-da-conta-de-teste-m5), confirmada no piloto de 12/11/2026.

**Massa adotada:** as 14 disciplinas e 43 turmas do mock acima, carregadas no
departamento `1499`, no **ano e período correntes** devolvidos por
`/courses/year-period/`. O *frontend* só oferece o período atual e o seguinte
(`api/utils/sessions.py`). O conteúdo da massa não muda, mas o ano/período em que ela é
gravada acompanha a data da execução, e esse valor deve ser registrado em cada coleta.

**Carga e restauração:** o *script*
[`avaliacao/massa/seed_referencia.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/massa/seed_referencia.py)
confere o SHA-256 do mock e o lê com o *parser* do produto, sem acessar a rede. Em seguida,
apaga e recria o departamento `1499` do período corrente em uma transação. Assim, rodar o
*script* de novo restaura o estado inicial das disciplinas e turmas. Ele deve ser executado
a partir do diretório do produto, com os serviços de pé:

```bash
docker exec -i django-api python3 manage.py shell \
  < ../2026-2_T02_ELIZABETH_FRIEDMAN/avaliacao/massa/seed_referencia.py
# massa carregada: 2026/2 depto 1499 14 disciplinas, 43 turmas, mock 17ae00b1edcc
```

O *script* foi executado duas vezes seguidas em 03/11/2026. Depois disso, o banco tinha
1 departamento, 14 disciplinas e 43 turmas, o que confirma que repetir a carga não duplica
os dados. Grades salvas no navegador são descartadas porque cada execução do Playwright usa
um contexto novo.

**Resultados de referência** (API local, ano 2026, período 2, 03/11/2026):

| Operação | Entrada | Resultado esperado |
|----------|---------|--------------------|
| Busca por nome | `GET /courses/?search=seminario&year=2026&period=2` | 3 disciplinas: `PPGPS0156` (4 turmas), `PPGPS0157` (1), `PPGPS2989` (16) |
| Busca por nome | `search=politica` | 6 disciplinas: `PPGPS0032`, `PPGPS0156`, `PPGPS0157`, `PPGPS2475`, `PPGPS2991`, `PPGPS0030` |
| Busca por código | `search=PPGPS2475` | 1 disciplina (`ESTADO E POLÍTICA SOCIAL NO BRASIL`, 1 turma) |
| Geração | `POST /courses/schedules/generate/` com as turmas `PPGPS2475/01` (5T2345) e `PPGPS2939/01` (4M1234) | `Horários gerados com sucesso.`, 1 grade com as duas turmas |

Os `id` das turmas mudam a cada carga, porque são gerados pelo banco. Por isso, os roteiros
devem identificar a turma por código da disciplina e número da turma, nunca pelo `id`.

### 2.4 Playwright e Chromium

O produto não usa Playwright (`web/package.json` não tem a dependência e o *frontend* não
tem testes). A automação fica no projeto `avaliacao/e2e/` deste repositório, com execução
sequencial (`workers: 1`) e sem novas tentativas (`retries: 0`), definidas em
`playwright.config.ts`.

| Item | Versão | Fonte |
|------|--------|-------|
| `@playwright/test` | `1.62.1` (exata, sem `^`) | `avaliacao/e2e/package.json` e `package-lock.json` (`@playwright/test`, `playwright` e `playwright-core` em `1.62.1`); `npx playwright --version` → `Version 1.62.1` |
| Chromium | Chrome for Testing `151.0.7922.34` (revisão `1234`) | `npx playwright install --dry-run chromium`; `~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome --version` |
| Chromium *headless shell* | `151.0.7922.34` (revisão `1234`) | `npx playwright install --dry-run chromium` |

É a mesma versão usada no teste de inicialização da [Fase 2](fase-2.md).

**Instalação fixada:**

```bash
cd avaliacao/e2e
npm ci                             # instala exatamente o package-lock.json
npx playwright --version           # esperado: Version 1.62.1
npx playwright install chromium    # baixa a revisão 1234 se ainda não estiver no cache
```

Na máquina de avaliação, as revisões `chromium-1234` e `chromium_headless_shell-1234` já
estavam no cache (`--dry-run`), então nada foi baixado.

**Demonstração de inicialização (03/11/2026)**, com os serviços da 2.1 de pé:

```text
$ npx playwright test --list
  [chromium] › smoke.spec.ts:6:5 › API responde o período letivo
  [chromium] › smoke.spec.ts:12:5 › frontend abre a tela inicial
Total: 2 tests in 1 file

$ npx playwright test
Running 2 tests using 1 worker
  ✓  1 [chromium] › tests/smoke.spec.ts:6:5 › API responde o período letivo (89ms)
  ✓  2 [chromium] › tests/smoke.spec.ts:12:5 › frontend abre a tela inicial (4.1s)
  2 passed (5.4s)
```

O *smoke* só confirma que o Chromium inicia, que a API responde e que a tela inicial
(`Continuar como anônimo`) é exibida. Não é coleta de M2–M5.

## 3. Cronograma da avaliação

<!--
F3-C3: cronograma realista com atividades distribuídas e alinhadas à execução da Fase 4.
-->

Cada linha corresponde a uma issue do repositório. **Início** e **Fim** são as datas reais das atividades
concluídas e a previsão da equipe para as demais, e cada atividade começa depois do fim das que aparecem
em **Depende de**. A coluna **Situação** vale para 10/11/2026. Todas as atividades terminam até **22/11/2026**.

| Issue | Atividade | Responsável | Início | Fim | Métricas | Depende de | Situação |
|------|-----------|-------------|--------|-----|----------|------------|----------|
| #37 | Ambiente de avaliação e massa de referência | Júlia | 02/11 | 05/11 | M1.3, M1.4, M2–M5 | n/a | Concluída |
| #38 | Método e roteiros de Manutenibilidade, com piloto | Lucas | 02/11 | 12/11 | M1.1–M1.4 | #37 | Em andamento |
| #39 | Método e roteiros de Eficiência de desempenho, com piloto | Júlia | 02/11 | 12/11 | M2–M5 | #37 | Em andamento |
| #40 | Protocolo com participantes de Capacidade de interação, com piloto | Lucas, Kaleb | 02/11 | 12/11 | M6–M9 | n/a | Em andamento |
| #41 | Cronograma e consistência com a Fase 2 | Joaquim | 02/11 | 09/11 | M1.1–M9 | n/a | PR #59 em revisão |
| #50 | Gestão PSM/CID, atas e decisões da E2 | Joaquim | 02/11 | 21/11 | n/a | contínuo | Contínua |
| #52 | Apresentação da gestão PSM/CID | Todos | 03/11 | 08/11 | n/a | n/a | Concluída |
| #54 | Ata da reunião de 03/11 | Eduardo | 04/11 | 04/11 | n/a | n/a | Concluída |
| #55 | Gráficos dos indicadores PSM/CID | Eduardo, Joaquim | 04/11 | 06/11 | n/a | n/a | Concluída |
| #49 | Correções do PC1 e largura do site | Eduardo | 10/11 | 10/11 | n/a | n/a | PR #60 em revisão |
| #36 | Material do PC2 (apresentação em 16/11 ou 18/11) | Todos | 13/11 | 18/11 | n/a | #38–#41 | A iniciar |
| #42 | Fase 4: coleta e análise de Manutenibilidade (G1) | Kaleb | 13/11 | 17/11 | M1.1–M1.4 | #38 | A iniciar |
| #43 | Fase 4: coleta e análise de Eficiência de desempenho (G2) | Júlia | 13/11 | 17/11 | M2–M5 | #39 | A iniciar |
| #44 | Fase 4: sessões e análise de Capacidade de interação (G3) | Kaleb, João | 13/11 | 17/11 | M6–M9 | #40 | A iniciar |
| #45 | Fase 4: julgamento, relações entre características e recomendações | Kaleb, Joaquim | 18/11 | 19/11 | M1.1–M9 | #42–#44 | A iniciar |
| #46 | Fase 4: ação de melhoria | Lucas | 20/11 | 20/11 | n/a | #45 | A iniciar |
| #47 | Artigo: metodologia, resultados e conclusão | João | 20/11 | 20/11 | n/a | #41–#46 | A iniciar |
| #48 | Artigo: revisão final da 2ª versão | João | 21/11 | 21/11 | n/a | #47 | A iniciar |
| #51 | Fechamento da E2: GitPage, contribuição e *release* v2.0 | Eduardo | 22/11 | 22/11 | n/a | #48, #50 | A iniciar |

---

## 4. Consistência com a Fase 2

<!--
F3-C8: para cada métrica da Fase 2, indicar explicitamente o método e os recursos que a medem.
Esta seção registra o que a Fase 3 fixou, o que mudou em relação à Fase 2 e o que ainda está pendente.
-->

A Fase 3 não altera nenhuma métrica, fórmula nem faixa de pontuação da [Fase 2](fase-2.md).
A tabela da seção 1 cobre M1.1 a M1.4 e M2 a M9, com a mesma numeração.

### 4.1 O que mudou em relação à Fase 2 e por quê

| # | Tema | Na Fase 2 | Na Fase 3 | Por quê e efeito |
|---|------|-----------|-----------|------------------|
| 1 | Máquina e Docker | Docker indisponível na distribuição WSL inspecionada em 18/10 ([3.2](fase-2.md#32-verificacao-de-viabilidade-da-coleta)); Node 24.19.0, npm 11.17.0 | Ubuntu 24.04.2 LTS, Docker 29.1.2, Compose v2.40.3; quatro serviços de pé em 03/11 ([2.1](#21-versao-avaliada-e-subida-do-ambiente), [2.2](#22-requisitos-do-avaliador)); Node v22.22.3, npm 11.16.0 | A coleta passou para outra máquina. A pendência 1 da Fase 2 está atendida. As ferramentas de análise estática de M1.1 e M1.2 devem registrar de novo as versões do host, pois as execuções de 18/10 foram só verificação inicial |
| 2 | Massa de M2–M5 | Conjuntos fixos a definir na Fase 3, sem acionar o SIGAA | Mock do projeto (`api/utils/mock/sigaa.html`): departamento 1499, 14 disciplinas e 43 turmas, todas de Pós-Graduação em Política Social ([2.3](#23-massa-de-referencia)) | É o único conjunto fixo e reproduzível sem rede. Os resultados valem para essa massa, não para o volume de uma matrícula real; a Fase 2 já limita as conclusões nesse sentido |
| 3 | Sessão na conta (M5) | Conta de teste com autenticação funcional por OAuth local | O login Google fica fora do escopo ([Fase 1, Tabela 12](fase-1.md#62-o-que-fica-fora-do-escopo)). A API aceita um *token* simulado, e o roteiro o entrega ao próprio fluxo do *frontend* pelo fragmento `#access_token`, sem credencial real ([1.1.6](#116-sessao-da-conta-de-teste-m5)); confirmado no piloto de 12/11/2026 | Evita depender de credenciais reais. A modalidade conta é coletada. O *token* simulado nunca é gravado nos resultados |
| 4 | Período da massa | Não especificado | A massa é gravada no ano e período correntes (`/courses/year-period/`), e o valor é registrado em cada coleta ([2.3](#23-massa-de-referencia)) | O *frontend* só oferece o período atual e o seguinte |
| 5 | M5 no navegador | Modalidade navegador de M5 prevista, com sinal visual de conclusão a confirmar ([3.2](fase-2.md#32-verificacao-de-viabilidade-da-coleta)) | **Não avaliada.** Na versão `3d399e7` não existe uma ação de salvar no navegador nem um sinal de conclusão desse salvamento. As grades vão para `localStorage['schedules']` como efeito colateral da geração ([GenerateScheduleButton.tsx#L64](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/schedules/home/components/GenerateScheduleButton.tsx#L64) → [SchedulesContext.tsx#L52-L63](https://github.com/unb-mds/2023-2-SuaGradeUnB/blob/3d399e745383b05e8e3b1a7c97ac0fdbf93a0360/web/app/contexts/SchedulesContext.tsx#L52-L63)), e o fim visível dessa gravação é o próprio fim de M4 | A Fase 2, seção 3.2, prevê revisar M5 quando o sinal não existe. A Fase 2 não foi alterada: pela regra 4 da [seção 4.3](fase-2.md#43-regras-de-aplicacao-e-julgamento-de-eficiencia-m2m5), M5 fica com **cobertura parcial** (só a conta) e sem nota consolidada completa. A revisão de M5 está pendente na [4.2](#42-decisoes-que-a-fase-2-deixou-para-a-fase-3) |

### 4.2 Decisões que a Fase 2 deixou para a Fase 3

| Decisão pendente na Fase 2 | Situação | Issue |
|----------------------------|----------|------|
| Fixar versões de Playwright e Chromium; execução sequencial sem nova tentativa | Fixadas: 1.62.1 e 151.0.7922.34; `workers: 1`, `retries: 0` ([2.4](#24-playwright-e-chromium)) | #37, concluído |
| Reprodução local e massa de referência | Feitas em 03/11 ([2.1](#21-versao-avaliada-e-subida-do-ambiente), [2.3](#23-massa-de-referencia)) | #37, concluído |
| Tempo máximo de espera por operação (maior que $L_j$) | Resolvida: 10000, 5000, 30000 e 10000 ms para M2 a M5 ([1.1.4](#114-tempo-maximo-de-espera)) | #39 |
| Seletores e sinais de conclusão visual de M2–M5 | Resolvida para M2, M3, M4 e M5 conta ([1.1.3](#113-acoes-seletores-e-sinais-de-conclusao)); M5 navegador não tem sinal (linha seguinte) | #39 |
| Sessão da conta de teste em M5 | Resolvida: fluxo do *frontend* com o *token* simulado no fragmento; cookie aceito no piloto ([1.1.6](#116-sessao-da-conta-de-teste-m5)) | #39 |
| Revisão de M5 para a modalidade navegador (sem ação de salvar nem sinal de conclusão) | **Pendente, decisão da equipe.** Até lá, a modalidade fica não avaliada e M5 com cobertura parcial ([4.1](#41-o-que-mudou-em-relacao-a-fase-2-e-por-que), linha 5) | Equipe |
| Configuração própria do `coverage` (`source` explícito, sem `pragma: no cover`) | Pendente; conferir no piloto | #38 |
| Executor de C1 e C2 e fichas das mudanças | Pendente | #38 |
| Número e perfil dos participantes, limites $E$ e $T$ de M6, consentimento | Pendente | #40 |
| Inventário de riscos de M8 e gabarito de M9 | Pendente | #40 |
| Pilotos de todas as métricas | M2 a M5: piloto feito em 12/11/2026 ([1.1.8](#118-piloto-12112026)). M1.1 a M1.4 e M6 a M9: pendentes | #38, #39 (concluído), #40 |

---

Anterior: [Fase 2](fase-2.md) · Próxima: [Fase 4 — Execução e resultados](fase-4.md).
