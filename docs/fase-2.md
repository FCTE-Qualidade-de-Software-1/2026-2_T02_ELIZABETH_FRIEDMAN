# Fase 2 — Especificar a avaliação

<!--
Referência: ISO/IEC 25040, atividade 2; método GQM (Basili).
F2-C11: deixar EXPLÍCITO como cada objetivo deriva das características e stakeholders da Fase 1.
-->

Os objetivos de medição abaixo derivam do propósito, das decisões apoiadas e das
necessidades das partes interessadas documentados na [Fase 1](fase-1.md).

A seleção e a priorização das características na [Seção 5 da Fase 1](fase-1.md#5-selecao-e-priorizacao-das-caracteristicas)
ainda estão em elaboração. Estes objetivos são iniciais e deverão ser revisados após
a consolidação dessa seção. A menção a usabilidade na Seção 2.2 da Fase 1 também
precisa ser conciliada com a orientação registrada na Seção 5 de não incluir essa
característica; não foi definido um objetivo para ela nesta etapa.

## 1. Objetivos de medição (nível conceitual)

<!--
F2-C1: usar o template GQM completo para cada objetivo.
-->

### G1 — Manutenibilidade

| Elemento | Descrição |
|----------|-----------|
| Analisar | O código-fonte do Sua Grade UnB, com foco nos componentes de coleta de dados do SIGAA e de busca de disciplinas, seleção de turmas, geração e salvamento de grades. |
| Com o propósito de | Avaliar a facilidade de manutenção e identificar os componentes que devem receber melhorias prioritárias para viabilizar correções e contribuições de voluntários. |
| Com respeito a | Manutenibilidade, com foco em analisabilidade, modificabilidade e testabilidade. |
| Do ponto de vista de | Mantenedores e contribuidores externos do Sua Grade UnB. |
| No contexto de | Uma avaliação acadêmica independente conduzida pela equipe Elizabeth Friedman, em cerca de seis semanas, de uma aplicação web em operação e mantida por voluntários, utilizando o repositório público e a reprodução local, sem acesso a logs ou ao banco de dados de produção e sem coletas repetidas no SIGAA. |

**Origem na Fase 1:** a [Seção 1.1](fase-1.md#11-contexto) registra a manutenção
por voluntários e a necessidade de adaptar a coleta de dados após mudanças no SIGAA.
O [propósito da avaliação](fase-1.md#12-proposito) inclui a continuidade da manutenção.
Na [Seção 2.2, Tabela 3](fase-1.md#22-mapa-de-partes-interessadas), as necessidades dos
mantenedores e dos contribuidores externos motivam explicitamente a manutenibilidade
e o foco em analisabilidade, modificabilidade e testabilidade. O objetivo apoia as
decisões **D1** (priorizar correções), **D2** (escolher a melhoria da Fase 4) e **D3**
(identificar por onde começar a contribuir), definidas na [Seção 1.3](fase-1.md#13-uso-pretendido-decisoes-apoiadas).

### G2 — Eficiência de desempenho

| Elemento | Descrição |
|----------|-----------|
| Analisar | O desempenho do Sua Grade UnB no fluxo de buscar disciplinas, selecionar turmas, gerar e salvar grades. |
| Com o propósito de | Avaliar o desempenho do fluxo principal e identificar operações cuja lentidão possa prejudicar o uso e deva ser priorizada nas melhorias. |
| Com respeito a | Eficiência de desempenho, com foco no comportamento temporal das operações do fluxo principal. |
| Do ponto de vista de | Estudantes da UnB que utilizam o sistema para montar a grade no período de matrícula. |
| No contexto de | Uma avaliação acadêmica independente conduzida pela equipe Elizabeth Friedman, em cerca de seis semanas, por observações no site público e medições em reprodução local sob condições documentadas, sem acesso a logs ou ao banco de dados de produção e sem gerar carga sobre o SIGAA. Os resultados ficam limitados às condições avaliadas e não demonstram, por si só, o desempenho em picos reais de matrícula. |

**Origem na Fase 1:** a [Seção 1.1](fase-1.md#11-contexto) identifica o uso recorrente
e concentrado no período de matrícula. O [propósito da avaliação](fase-1.md#12-proposito)
prevê identificar problemas que afetam os estudantes nesse período. Na
[Seção 2.2, Tabela 3](fase-1.md#22-mapa-de-partes-interessadas), os estudantes motivam
explicitamente a característica de eficiência e a avaliação dos tempos de resposta
no fluxo principal. A mesma tabela estabelece a restrição de não gerar carga sobre
o SIGAA. O objetivo apoia as decisões **D1** (priorizar correções) e **D2** (escolher a
melhoria da Fase 4), definidas na [Seção 1.3](fase-1.md#13-uso-pretendido-decisoes-apoiadas).

## 2. Questões e hipóteses (nível operacional)

<!--
F2-C2: questões que cobrem os atributos do foco de qualidade (não métricas disfarçadas de pergunta).
F2-C3: uma hipótese clara para CADA questão.
-->

### 2.1 Manutenibilidade — G1

| ID | Questão | Hipótese | Objetivo |
|----|---------|----------|----------|
| Q1 | | H1: | G1 |

### 2.2 Eficiência de desempenho — G2

As questões abaixo cobrem **comportamento temporal**, a subcaracterística selecionada
no [objetivo G2](#g2-eficiencia-de-desempenho), nas quatro operações do fluxo principal
identificadas na [Seção 2.2 da Fase 1](fase-1.md#22-mapa-de-partes-interessadas).
Utilização de recursos e capacidade não integram o recorte atual de G2.

As hipóteses são expectativas a verificar, não resultados da avaliação. Os limites
de tempo aceitáveis por operação e a regra para confirmar ou refutar cada hipótese
deverão ser definidos nas Seções 3 e 4, antes da coleta. As condições de execução,
os dados utilizados e a repetição das tarefas serão especificados no plano da
[Fase 3](fase-3.md), permitindo comparar os resultados sob condições documentadas.

| ID | Subcaracterística | Questão | Hipótese | Objetivo |
|----|-------------------|---------|----------|----------|
| Q2 | Comportamento temporal | A busca de disciplinas apresenta os resultados em tempo aceitável para o estudante dar continuidade à montagem da grade? | H2: O tempo entre solicitar uma busca por nome ou código e visualizar seus resultados atende ao limite de aceitação definido para a busca, nas condições avaliadas. | G2 |
| Q3 | Comportamento temporal | A seleção de turmas atualiza a interface em tempo aceitável para o estudante continuar selecionando as opções desejadas? | H3: O tempo entre selecionar uma turma e visualizar a atualização correspondente na interface atende ao limite de aceitação definido para a seleção, nas condições avaliadas. | G2 |
| Q4 | Comportamento temporal | A geração de combinações de turmas sem conflito apresenta as grades em tempo aceitável nos cenários de montagem avaliados? | H4: O tempo entre solicitar a geração e visualizar as combinações de grades atende ao limite de aceitação definido para a geração em cada cenário avaliado. | G2 |
| Q5 | Comportamento temporal | O salvamento de uma grade fornece retorno em tempo aceitável para o estudante concluir a tarefa? | H5: O tempo entre solicitar o salvamento e visualizar sua confirmação atende ao limite de aceitação definido para o salvamento, nas modalidades avaliadas de conta do usuário e armazenamento no navegador. | G2 |

## 3. Métricas (nível quantitativo)

<!--
F2-C4 e premissa 2: para cada métrica documentar definição, procedimento de cálculo (fórmula),
fonte dos dados, procedimento de coleta e critérios de interpretação.
Fórmulas em LaTeX: $ X = \frac{A}{B} $ em linha, ou $$ ... $$ em bloco.
-->

### 3.1 Convenções de medição de eficiência de desempenho

As métricas **M2 a M5** respondem, respectivamente, às questões **Q2 a Q5** do
objetivo **G2**, cobrindo comportamento temporal. A métrica M1 permanece reservada
à questão de manutenibilidade, ainda em elaboração.

Para cada operação e cenário, executar duas tentativas de aquecimento, registradas
e excluídas do cálculo, seguidas de **30 tentativas medidas**, sequenciais e sem
concorrência. Esse tamanho de amostra é uma escolha operacional inicial da equipe;
não representa uma garantia estatística sobre o uso em produção. Restaurar o estado
inicial antes de cada tentativa e manter os mesmos dados, navegador, equipamento,
rede e política de cache dentro de cada cenário. Documentar essas condições na
Fase 3. Separar os resultados por cenário e ambiente, sem misturar medições locais
com observações do site público. A coleta repetida será realizada em reprodução
local com dados previamente disponíveis, sem acionar a coleta do SIGAA.

Medir o intervalo entre a ação do usuário e o resultado visível na interface,
incluindo processamento, comunicação e atualização visual. Usar um mesmo relógio
monotônico no navegador e registrar os eventos em um roteiro automatizado ou em
uma instrumentação local reproduzível. Tempos de requisições de rede isoladas não
substituem esse intervalo. Os seletores e sinais de conclusão serão confirmados
na preparação do roteiro na Fase 3, conforme o comportamento real da aplicação.

Para cada tentativa concluída com sucesso:

$$
t_i = t_{\mathrm{fim},i} - t_{\mathrm{início},i}
$$

Os tempos são expressos em **milissegundos (ms)**. Ordenando os tempos válidos de
forma crescente, calcular o percentil 95 pelo método do posto mais próximo:

$$
P_{95}(t) = t_{(\lceil 0{,}95n \rceil)}
$$

Nessa fórmula, $n$ é o número de tentativas medidas concluídas com sucesso e
$t_{(k)}$ é o tempo na posição $k$ da série ordenada. Com 30 sucessos, utiliza-se
o 29º tempo. Com nenhum sucesso, o percentil é **não calculável**.

Registrar as 30 tentativas, incluindo erros e expiração do tempo de espera, sem
substituí-los por novas tentativas ou tratá-los como tempos iguais a zero. O tempo
máximo de espera por operação será fixado na Fase 3, antes da coleta, e deverá ser
superior ao respectivo limite de aceitação. Publicar o número de sucessos, erros e
expirações junto ao percentil; este descreve apenas as tentativas bem-sucedidas.
Ocorrências de falha impedem confirmar a hipótese apenas com base em um percentil
baixo e devem ser consideradas na regra de julgamento da Seção 4.

Guardar os dados brutos em CSV com: métrica, cenário, ambiente, versão do sistema,
data, número da tentativa, indicação de aquecimento, instante inicial, instante
final, duração, estado (sucesso, erro ou expiração) e referência à evidência.
Registrar a configuração do ambiente e a massa de dados junto ao arquivo.

Para cada métrica, **menor é melhor**. O resultado atende ao requisito temporal
quando $M_j \leq L_j$, em que $L_j$ é o limite de aceitação da operação e do
cenário, em ms. Os valores de $L_2$ a $L_5$, sua justificativa e os níveis de
pontuação serão definidos na Seção 4 **antes da coleta**. Até essa definição, as
métricas permitem descrever os tempos, mas não confirmar as hipóteses de aceitação.

### M1 — Manutenibilidade (a definir)

| Campo | Descrição |
|-------|-----------|
| Questão respondida | Q1 |
| Definição | |
| Fórmula | $ X = \frac{A}{B} $ |
| Fonte dos dados | |
| Procedimento de coleta | |
| Interpretação | |

### M2 — Tempo de resposta da busca de disciplinas (P95)

| Campo | Descrição |
|-------|-----------|
| Questão respondida | Q2 — hipótese H2; objetivo G2. |
| Definição | Percentil 95 do tempo entre a ação que solicita a busca e a exibição dos resultados correspondentes ao termo informado, com a interface pronta para interação. |
| Fórmula | $M_2 = P_{95}(t_{\mathrm{busca}})$, em ms, conforme a Seção 3.1. |
| Fonte dos dados | Registros de eventos do navegador na reprodução local, arquivo CSV das tentativas e evidências da atualização dos resultados. |
| Procedimento de coleta | Preparar cenários separados para busca por nome e por código, com termos e resultados esperados fixos. Iniciar a marcação na ação que dispara a busca; se houver busca automática, usar o último evento de entrada do termo, incluindo eventual espera programada pela aplicação. Encerrar quando os resultados correspondentes estiverem visíveis e utilizáveis, sem confundir resultados anteriores com os da nova busca. Executar o protocolo da Seção 3.1 para cada cenário. |
| Interpretação | Comparar cada cenário com $L_2$. Um resultado acima do limite indica demora na busca sob as condições medidas. Interpretar junto aos erros e expirações; o resultado não demonstra desempenho em picos de matrícula. |

### M3 — Tempo de atualização após seleção de turma (P95)

| Campo | Descrição |
|-------|-----------|
| Questão respondida | Q3 — hipótese H3; objetivo G2. |
| Definição | Percentil 95 do tempo entre selecionar uma turma e visualizar a atualização completa do estado de seleção na interface. |
| Fórmula | $M_3 = P_{95}(t_{\mathrm{seleção}})$, em ms, conforme a Seção 3.1. |
| Fonte dos dados | Registros de eventos de seleção e atualização visual do navegador na reprodução local, arquivo CSV e evidências do estado selecionado. |
| Procedimento de coleta | Fixar a disciplina, a turma e as seleções anteriores de cada cenário. Iniciar a marcação na ação de selecionar a turma e encerrar quando os indicadores visuais correspondentes refletirem o novo estado e a interface permitir continuar a tarefa. Restaurar as seleções iniciais entre tentativas, fora do intervalo medido. Executar o protocolo da Seção 3.1. |
| Interpretação | Comparar cada cenário com $L_3$. Um resultado acima do limite indica atraso na atualização após a seleção, nas condições medidas. Uma atualização ausente ou incorreta é registrada como erro, não como resposta rápida. |

### M4 — Tempo de geração de grades (P95)

| Campo | Descrição |
|-------|-----------|
| Questão respondida | Q4 — hipótese H4; objetivo G2. |
| Definição | Percentil 95 do tempo entre solicitar a geração e concluir a apresentação das combinações de grades previstas pelo fluxo da aplicação para o conjunto selecionado. |
| Fórmula | $M_4 = P_{95}(t_{\mathrm{geração}})$, em ms, conforme a Seção 3.1. |
| Fonte dos dados | Registros de acionamento e conclusão da geração no navegador da reprodução local, massa de dados de disciplinas e turmas, arquivo CSV e evidências das grades apresentadas. |
| Procedimento de coleta | Preparar conjuntos fixos de disciplinas e turmas com combinações válidas conhecidas. Documentar por cenário as quantidades de disciplinas, turmas candidatas e combinações válidas esperadas. Iniciar a marcação na solicitação de geração e encerrar quando o processamento e a apresentação previstos pelo fluxo estiverem concluídos e o estudante puder consultar as grades. Não encerrar apenas ao aparecer um indicador de carregamento ou um resultado parcial. Executar o protocolo da Seção 3.1 e calcular o percentil separadamente para cada conjunto. |
| Interpretação | Comparar cada cenário com $L_4$. Tempos acima do limite indicam demora na geração para aquele conjunto. Comparações entre conjuntos ajudam a identificar sensibilidade ao volume de combinações, mas não estabelecem a capacidade máxima do sistema. Resultados incompatíveis com a massa de referência são registrados como erro. |

### M5 — Tempo de retorno do salvamento de grade (P95)

| Campo | Descrição |
|-------|-----------|
| Questão respondida | Q5 — hipótese H5; objetivo G2. |
| Definição | Percentil 95 do tempo entre solicitar o salvamento de uma grade e visualizar o sinal de conclusão bem-sucedida fornecido pela interface. |
| Fórmula | $M_5 = P_{95}(t_{\mathrm{salvamento}})$, em ms, conforme a Seção 3.1. |
| Fonte dos dados | Registros de eventos de salvamento e de sua confirmação no navegador da reprodução local, arquivo CSV e evidências da recuperação da grade salva. |
| Procedimento de coleta | Preparar uma grade fixa e cenários separados para salvamento na conta de teste e no navegador, conforme as modalidades disponíveis. Concluir autenticação e preparação antes da marcação. Iniciar ao solicitar o salvamento e encerrar na confirmação visual. Depois do intervalo medido, verificar se a grade pode ser recuperada; uma confirmação sem persistência verificada conta como erro. Restaurar o estado inicial entre tentativas e executar o protocolo da Seção 3.1. Se uma modalidade não puder ser reproduzida, registrar a limitação e não lhe atribuir resultado. |
| Interpretação | Comparar separadamente cada modalidade com $L_5$. Tempos acima do limite indicam demora no retorno do salvamento. Um retorno rápido sem persistência não confirma H5. O tempo de autenticação e o de recuperação usado na verificação não integram esta métrica. |

### 3.2 Verificação de viabilidade da coleta

Esta verificação distingue **viabilidade documental** (há uma ferramenta e um caminho
de acesso identificados) de **coleta validada** (o roteiro foi executado no ambiente
da avaliação e produziu dados e evidências). A consulta ao repositório e a inspeção
do ambiente foram feitas em **18/10/2026**. Nenhuma das métricas abaixo teve ainda
sua coleta validada por execução ponta a ponta.

O [README do Sua Grade UnB](https://github.com/unb-mds/2023-2-SuaGradeUnB#readme)
documenta instalação, execução por Docker Compose, frontend em `localhost:3000`,
backend em `localhost:8000` e configuração de Google OAuth para login. Isso fornece
um caminho de reprodução, mas não comprova que a aplicação esteja operacional no
ambiente da equipe. O procedimento de atualização do banco descrito no README
aciona o SIGAA e não será usado na coleta; a massa local deverá ser preparada e
validada previamente, sem essa dependência.

| Métrica | Ferramenta e evidência prevista | Acesso necessário | Ambiente e dependências | Situação e condição para validar |
|---------|--------------------------------|-------------------|-------------------------|----------------------------------|
| M1 — Manutenibilidade | A definir após a formulação de Q1 e da métrica. | O código é público, mas a fonte específica depende da definição da métrica. | A definir. | **Não verificável no estado atual:** falta especificar a métrica; não presumir que ferramentas de análise estática sejam suficientes. |
| M2 — Busca | Playwright com Chromium, marcações temporais no navegador, CSV e captura dos resultados. | Código público e API local com disciplinas e turmas de referência; confirmar no piloto se o fluxo exige autenticação. | Frontend, backend e banco locais populados; cenários fixos de nome e código. | **Viável sob condições:** executar uma busca de cada tipo, verificar o resultado esperado e demonstrar a captura dos dois instantes e do CSV. |
| M3 — Seleção | Playwright com Chromium, marcações temporais e captura da atualização visual. | Acesso ao fluxo de disciplinas e turmas; confirmar no piloto os requisitos de sessão. | Mesma aplicação local de M2, com turma conhecida e estado inicial restaurável. | **Viável sob condições:** demonstrar que uma seleção produz o estado esperado e que o roteiro distingue a atualização completa de um estado anterior. |
| M4 — Geração | Playwright com Chromium, marcações temporais, CSV e evidência das combinações geradas. | Acesso ao gerador e a uma massa local com combinações válidas previamente conferidas. | Aplicação local e conjuntos fixos de disciplinas e turmas, com resultados de referência. | **Viável sob condições:** gerar um conjunto conhecido e verificar que o sinal de término representa a conclusão prevista em M4, incluindo a conferência dos resultados. |
| M5 — Salvamento no navegador | Playwright com Chromium, marcações temporais, CSV e evidência de recuperação da grade. | Acesso à modalidade de armazenamento no navegador, cuja disponibilidade precisa ser confirmada na versão avaliada. | Aplicação local, contexto de navegador preservado durante a verificação e grade fixa. | **Viável sob condições:** confirmar a modalidade, identificar seu sinal visual de conclusão e recuperar a grade após recarregar a página. Se o sinal não existir, revisar M5 antes da coleta. |
| M5 — Salvamento na conta | Playwright com Chromium, sessão de teste autenticada, marcações temporais, CSV e evidência de recuperação. | Conta de teste e configuração local de OAuth conforme o projeto; sem credenciais ou banco de produção. | Frontend, backend e banco locais, autenticação funcional e persistência configurada. | **Viável sob condições adicionais:** concluir login antes da medição, salvar e recuperar a grade após recarregar. Sem autenticação funcional, registrar esta modalidade como não coletada; não generalizar o resultado do navegador para a conta. |

A escolha do Playwright se apoia em sua [documentação de automação de navegadores](https://playwright.dev/docs/intro).
Para as marcações, usar `performance.now()` no mesmo contexto de página, cujo
[relógio monotônico é documentado pela MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now).
Os sinais de conclusão visual precisam ser implementados e conferidos no piloto;
observar somente uma alteração no DOM ou uma resposta HTTP não comprova que a
operação terminou e está visível. Registrar o mecanismo adotado e sua limitação
de precisão na Fase 3.

**Resultado da inspeção do ambiente de trabalho:** Node `24.19.0`, npm `11.17.0`,
Python `3.12.3` e GNU Make `4.3` responderam aos comandos de versão. Foram localizados
arquivos de instalação do Playwright e binários do Chromium no cache do usuário;
sua presença não comprova inicialização nem compatibilidade com o roteiro.
`docker compose version` e `docker ps` falharam informando que o Docker não está
disponível nesta distribuição WSL. A reprodução local, a massa de dados e o login
de teste ainda não foram demonstrados neste ambiente. Esses resultados descrevem
a máquina inspecionada, não todas as máquinas da equipe.

**Pendências para confirmar a coleta na Fase 3:**

1. Disponibilizar Docker Engine/Compose com integração ao WSL ou outro ambiente
   de execução compatível, fixar o commit avaliado e iniciar os serviços locais.
2. Preparar a massa de referência sem executar a coleta do SIGAA e conferir os
   resultados esperados de busca, seleção e geração.
3. Fixar as versões do Playwright e do Chromium, demonstrar sua inicialização e
   configurar execução sequencial, sem repetição automática de tentativas com erro.
4. Executar o piloto de cada linha da matriz, guardando roteiro, configuração,
   CSV com duração válida e evidência do resultado. O piloto é uma verificação
   do método e não integra as 30 tentativas da coleta formal.
5. Validar a restauração de estado e o registro de erros e expirações, configurar
   o tempo máximo de espera e definir os limites de aceitação antes da coleta.

**Conclusão de viabilidade:** há um caminho técnico identificado para M2–M5, mas
a coleta permanece condicionada à preparação do ambiente e à aprovação dos pilotos.
M1 depende de especificação. Esta seção não deve ser tratada como evidência de
medições já executadas nem como encerramento da validação prática.

## 4. Níveis de pontuação e critérios de julgamento

<!--
F2-C5: níveis de pontuação para TODAS as métricas e critérios de julgamento explícitos
(como o resultado da medição vira um julgamento).
-->

| Métrica | Insatisfatório | Aceitável | Bom | Excelente |
|---------|----------------|-----------|-----|-----------|
| M1 | | | | |

**Critério de julgamento:** *A preencher.*

## 5. Diagrama GQM

<!--
F2-C6: diagrama completo com todos os objetivos, identificando os níveis (conceitual, operacional, quantitativo).
O exemplo abaixo é só o formato; substitua pelos objetivos reais.
-->

```mermaid
flowchart TD
    subgraph Conceitual
        G1["G1: objetivo"]
    end
    subgraph Operacional
        Q1["Q1: questão"]
        Q2["Q2: questão"]
    end
    subgraph Quantitativo
        M1["M1: métrica"]
        M2["M2: métrica"]
        M3["M3: métrica"]
    end
    G1 --> Q1
    G1 --> Q2
    Q1 --> M1
    Q1 --> M2
    Q2 --> M3
```

---

Anterior: [Fase 1](fase-1.md) · Próxima: [Fase 3 — Projeto da avaliação](fase-3.md).
