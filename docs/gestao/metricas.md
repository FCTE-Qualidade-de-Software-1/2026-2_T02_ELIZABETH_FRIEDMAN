
<!--
Seção 2 da especificação: registrar medições, interpretação e DECISÕES de gestão decorrentes.
Evidências no repositório: commits, issues, milestones, dashboards.
-->
# Gestão do projeto — Medição PSM/CID

Este documento descreve como o projeto é medido e gerido segundo o **PSM Continuous Iterative Development (CID) Measurement Framework, v2.1** (PSM, NDIA e INCOSE, 15/04/2021). Para cada decisão tomada pela equipe, ele indica o que o framework prevê e como ela foi adaptada. Os **valores** dos indicadores são calculados automaticamente e ficam em [indicadores](indicadores.md) e nos CSVs de `evidencias/`. Este documento define o que é medido e registra a interpretação e as decisões de gestão (seção 6), que também aparecem nas [atas](atas.md).

Convenção de referência: **P1**, **P2** e **P3** são as Partes 1, 2 e 3 do framework, seguidas da seção (ex.: P2 8.3). **I1 a I9** são os nove indicadores do projeto (seção 3).

## 1. Abordagem do framework

- **Modelo de informação (P1, seção 4).** Cada medida liga uma *necessidade de informação* a um *conceito mensurável* e a um *construto de medição*: medidas base, medidas derivadas e indicador, com modelo de análise e critérios de decisão. O produto final é o valor com sua interpretação.
- **Princípios (P1, seção 5).** Usar um conjunto mínimo de medidas, adaptado ao contexto, cada uma com stakeholder e decisão associada, com coleta automatizada na medida do possível e equilíbrio entre velocidade e qualidade.
- **Adaptação.** O framework foi escrito para programas de desenvolvimento contínuo e iterativo de grande escala. Ele próprio afirma que as medidas devem ser adaptadas ao ambiente de desenvolvimento (Resumo Executivo e P1, seção 5). Este projeto acadêmico aplica o mesmo raciocínio em escala menor.

As três categorias de informação exigidas pela especificação do trabalho correspondem às do framework: **Desempenho dos Processos** (*Process Performance*), **Calendário e Progresso** (*Schedule and Progress*) e **Recursos e Custos** (*Resources and Cost*).

## 2. Decisões de gestão e sua base no framework

| # | Decisão da equipe | O que o framework prevê | Como adaptamos e por quê |
|---|---|---|---|
| D1 | **Iteração = uma semana**, com um milestone e um prazo (iteração 1: 13/10 a 19/10; iteração 2: 20/10 a 25/10) <!-- CONFIRMAR as datas de início e o prazo de cada milestone --> | A iteração é um bloco de tempo curto no qual a equipe desenvolve e demonstra um conjunto de stories, também chamado de sprint (P1, seção 3). A duração não é fixa, e a maioria dos programas adota cadência com blocos de tempo definidos (*Release Style*, P1, seção 3) | Semana de calendário, compatível com os prazos de entrega do trabalho e com a frequência de reunião do grupo. O prazo do milestone é a referência de I5 e I6 |
| D2 | **Work item = issue do GitHub. Tamanho do trabalho = horas estimadas da issue**, registradas no campo "Horas estimadas" do template. **Esforço real = horas trabalhadas**, declaradas em `horas.csv` | Burndown, Committed vs. Completed e Velocity são medidos em story points, features ou unidade equivalente (P2 8.2, 8.3). A estimativa costuma se basear em medidas de esforço relativo, como stories, story points ou *outras alternativas validadas, com definições operacionais claras e repetíveis* (P2 8.2, Implementation Considerations) | **Adaptação:** não usamos story points. A issue é o work item, e as horas (estimadas e reais) alimentam I4, I7, I8 e I9. Diferença em relação ao framework: as horas são uma unidade absoluta e não relativa, e dependem de quem estima |
| D3 | **Definição operacional de issue concluída e do denominador do progresso.** *Concluída* = issue encerrada que atende o critério Done (D4). O denominador de I5 são as issues do milestone, **sem as descartadas** <!-- CONFIRMAR no script: como "concluída" e "descartada" são identificadas (estado, label ou motivo de fechamento) --> | O percentual concluído é (trabalho concluído × 100) ÷ trabalho comprometido, e só conta como concluído o item testado, que satisfaz o critério Done e não tem defeito aberto (P2 8.3). As medidas base são contagens em **escala inteira** (P2 8.2, 8.3) | **Adaptação:** a unidade de progresso passa a ser a **contagem de issues**, e não as horas estimadas. A contagem respeita a escala inteira do framework, o que as horas decimais não faziam. Como as issues têm tamanhos diferentes, I5 não pondera por complexidade (o framework admite essa ponderação, P2 8.3) |
| D4 | **Critério de pronto (Done):** a issue só conta como concluída se estiver fechada, com o entregável aceito, o PR revisado e integrado e sem defeito conhecido em aberto | Os itens só são contados como concluídos se foram testados, satisfazem o critério "Done" e não têm defeitos abertos. Caso contrário, não são considerados completos (P2 8.3) | Mantemos a regra. O texto do critério é nosso, e a equipe deve revisá-lo na reunião de planejamento. O script lê o estado da issue e não verifica o critério, então fechar a issue sem cumpri-lo infla I5. Os indicadores de retrabalho (I3 e I4) ajudam a detectar esse caso |
| D5 | **Um milestone do GitHub por iteração** | O compromisso e a conclusão são medidos por iteração (P2 8.2, 8.3) | Implementação nossa. Como uma issue só pode ter um milestone, o milestone representa a iteração. A entrega maior (E1) fica no board ou em label |
| D6 | **Compromisso definido no planejamento da iteração**, com base no que a equipe concluiu nos milestones anteriores (I5) e na disponibilidade dos integrantes | O compromisso de cada iteração é definido na reunião de planejamento, a partir da velocidade média e de fatores como férias, e os work items são selecionados para casar com esse compromisso (P2 8.2). Se a equipe terminar antes, seleciona itens adicionais do backlog (P2 8.3) | **Adaptação:** a velocidade (soma das horas estimadas concluídas) não é calculada pela automação, então o planejamento usa o I5 dos milestones anteriores. **Atenção:** o framework congela o compromisso no planejamento, mas o denominador de I5 são as issues que estão no milestone na data. Issues puxadas depois entram no denominador e reduzem o percentual. <!-- CONFIRMAR a regra do grupo: issues extras ficam fora do milestone (ou com label própria) para não distorcer I5? --> A estimativa de uma issue não deve ser alterada depois do planejamento, para não distorcer I8 |
| D7 | **Coleta automática semanal, todo domingo às 23:59, a cada issue fechada e a cada publicação da GitPage** | Burndown é atualizado diariamente, e Committed vs. Completed é coletado ao fim de cada iteração pelo líder, a partir da ferramenta de acompanhamento (P2 8.2, 8.3). A coleta deve ser automatizada e integrada ao fluxo de trabalho (P1, seção 5) | Aderente quanto à automação e ao uso do GitHub (issues, milestones e PRs) como ferramenta de acompanhamento. **Diferença:** não há série diária. O ritmo é semanal, o mesmo da iteração (D1), e a coleta a cada issue fechada mantém os valores atualizados sem esperar o domingo |
| D8 | **Histórico recalculado por inteiro a cada execução.** Fontes: issues (corpo, labels e eventos), milestones e PRs. Os valores ficam em `docs/gestao/indicadores.md` e em CSVs de `docs/gestao/evidencias/` | Cycle Time e Lead Time são gerados direto das ferramentas de gestão do projeto, a partir de carimbos de data e hora (P2 8.5). Os dados de iterações passadas são insumo para a análise de tendência (P2 8.3, 8.10) | Implementação nossa. Recalcular tudo evita linhas escritas à mão e permite corrigir um dado antigo (ex.: horas preenchidas depois) com efeito em todo o histórico. O histórico do git é a evidência datada. **Commits não são usados como fonte** |
| D9 | **Interpretação e decisão de gestão feitas pela equipe na reunião de revisão da iteração**, registradas na ata | Os dados são analisados ao fim de cada iteração, na revisão (ou retrospectiva), e alimentam o planejamento da iteração seguinte (P2 8.3, 8.5, 8.7, 8.10) | Seguimos a regra. A automação coleta e calcula, mas não interpreta nem decide. Cada medição registrada na seção 6 aponta a decisão tomada |
| D10 | **Objetivo de processo: PR mergeado só com aprovação de outra pessoa, em até 48 h da abertura** (I1 e I2) | O Cycle Time e o Lead Time medem a duração de work items (features, stories, defects) e permitem análise de previsibilidade (P2 8.5). A tabela de Garantia de Software lista *Code Passing Peer Review* como medida potencial (P3, Tabela 6, linha 16) | **Adaptação:** PR não é uma entidade listada em P2 8.5. Aplicamos o mesmo cálculo de tempo decorrido, aqui como limite de 48 h. A autoaprovação não conta, pois o objetivo da revisão por pares é a verificação por outra pessoa. O limite de 48 h é uma meta de processo definida pela equipe |
| D11 | **Horas reais registradas em `horas.csv`**: uma linha por issue e por responsável, com `XX` até o responsável declarar as horas. O arquivo é atualizado automaticamente todo domingo às 23:59 e a cada issue fechada | A tabela ICM lista *Effort* e *Estimate vs. Actual Effort* como medidas de Recursos e Custos (P1, seção 7, linhas 7 e 8), mas a Parte 2 não as especifica | **Adaptação:** definimos as medidas no formato do *template* das especificações (I7 e I8). As horas são **autodeclaradas**, então são um dado de menor precisão que os dados extraídos do GitHub. A atualização automática só cria e mantém as linhas, e nunca sobrescreve horas preenchidas. O indicador I9 mede quantas issues concluídas ainda estão sem horas |
| D12 | **Conjunto mínimo de nove indicadores (I1 a I9)** | Selecionar um conjunto mínimo e adaptado, cada medida com stakeholder, decisão e ação possível (P1, seção 5). A Parte 2 traz especificações para outras medidas | Não são coletados: Burndown (8.2) e Team Velocity (8.10) com série diária, médias e aceleração; Cycle Time / Lead Time (8.5) como tempos médios (só o limite de 48 h de I1 é usado); Automated Test Coverage (8.1), Cumulative Flow (8.4), Defect Detection (8.6), Defect Resolution (8.7), MTTR/MTTD (8.8), Release Frequency (8.9) e Product Value (8.11); e as medidas de Software Assurance e Dívida Técnica da Parte 3. Elas não respondem às necessidades de informação da gestão deste trabalho ou exigiriam dados que o fluxo atual não registra. Burndown e Velocity poderiam voltar, pois as horas estimadas já estão nas issues, mas isso exige ampliar o script |
| D13 | **Ler a conclusão por milestone (I5) e o retrabalho (I3, I4) como alerta de dívida técnica** | A Parte 3 observa que, se os itens comprometidos superam os concluídos sem ajuste de recursos ou prazo, haverá dívida técnica. Ela também diz que a falha em detectar defeitos é retrabalho futuro escondido, ou seja, dívida técnica (P3, Tabela 5, Committed vs. Completed e Defect Resolution) | Usamos a leitura como alerta: diferença persistente entre comprometido e concluído, ou retrabalho crescente, leva à revisão do escopo da iteração seguinte. Não medimos dívida técnica separadamente |
| D14 | **Retrabalho = issue concluída que tem a label `correcao` ou que foi reaberta** (I3), e as horas reais dessas issues em relação às horas reais das concluídas (I4) | A tabela ICM lista *Rework Stories*, *Rework Defects* e *Rework Hours* como medidas de Qualidade do Produto (P1, seção 7, linhas 18 e 19), sem especificá-las na Parte 2. A Parte 2 considera defeito o erro devolvido à equipe de origem que gera retrabalho (P2 8.7, Implementation Considerations) | **Adaptação:** definimos o retrabalho por duas marcas observáveis no GitHub: a label `correcao` (trabalho aberto para corrigir algo entregue) e a reabertura (trabalho que voltou). A medida depende de a equipe aplicar a label de forma consistente |

## 3. Indicadores e rastreabilidade com a tabela ICM (P1, seção 7)

| Indicador | Categoria do projeto | Conceito mensurável (ICM) | Linha ICM | Base no framework | Aderência |
|---|---|---|---|---|---|
| I1 PRs revisados no prazo | Desempenho dos processos | Process Efficiency – Speed | P1 32 | Cycle Time / Lead Time (P2 8.5) | Adaptada a PRs |
| I2 PRs aprovados antes do merge | Desempenho dos processos | Security / Product Quality | P3 Tabela 6, linha 16 | *Code Passing Peer Review*, sem especificação | Adaptada |
| I3 Retrabalho (issues) | Desempenho dos processos | Functional Correctness | P1 18 e 19 | *Rework Stories / Defects*, sem especificação | Definição própria (D14) |
| I4 Retrabalho (horas) | Desempenho dos processos | Functional Correctness | P1 19 | *Rework Hours*, sem especificação | Definição própria (D14) |
| I5 Conclusão de issues por milestone | Calendário e progresso | Work Unit Progress (*Milestone Completion*) | P1 1 | Committed vs. Completed (P2 8.3) | Adaptada (D3, D6) |
| I6 Desvio de prazo médio | Calendário e progresso | Financial Performance (*Estimate vs. Actual Schedule*) | P1 8 | Sem especificação na Parte 2 | Definição própria |
| I7 Distribuição de esforço por pessoa | Recursos e custos | Financial Performance (*Effort*) | P1 7 | Sem especificação na Parte 2 | Definição própria |
| I8 Esforço real / estimado | Recursos e custos | Financial Performance (*Estimate vs. Actual Effort*, *Estimation Accuracy*) | P1 8 e 9 | Sem especificação na Parte 2 | Definição própria |
| I9 Issues concluídas sem horas reais | Recursos e custos | — | — | Não existe no framework | Controle de qualidade do dado |

Observações sobre a classificação:

- A tabela ICM coloca *Rework* em Qualidade do Produto (linhas 18 e 19), e *Estimate vs. Actual Schedule* em Recursos e Custos (linha 8). O projeto agrupa I3 e I4 em Desempenho dos processos e I6 em Calendário e progresso, porque eles respondem a perguntas de processo (quanto do trabalho volta) e de prazo (quando fechamos em relação ao combinado).
- *Effort* está na linha 7 da ICM, no conceito **Financial Performance**. O conceito *Personnel Effort* (linhas 10 a 12) trata de experiência, rotatividade e satisfação da equipe, e não de horas trabalhadas.

## 4. Especificação dos indicadores

Cada indicador segue os campos do *template* das especificações da Parte 2, seção 8. Salvo indicação contrária, "concluída" segue o critério Done (D3 e D4). Quando o framework não traz critério de decisão, o limiar é **adotado pela equipe** e está marcado como tal.

### Desempenho dos Processos

#### I1 — PRs revisados no prazo (P2 8.5, adaptado)

| Campo | Especificação |
|---|---|
| Necessidade de informação | A revisão de código chega a tempo? A revisão é um gargalo no fluxo? |
| Medidas base | PRs mergeados. PRs mergeados aprovados **por outra pessoa**, **antes do merge** e **em até 48 h da abertura** (datas e horas de abertura e de aprovação, autor e aprovador) |
| Medida derivada | I1 = PRs aprovados no prazo ÷ PRs mergeados |
| Indicador | Percentual por domingo, desde o início do projeto |
| Modelo de análise | A revisão acompanha o ritmo de abertura de PRs? Quais PRs passaram de 48 h e por quê? Tempos longos costumam ter relação com excesso de trabalho em andamento (P2 8.5) |
| Critérios de decisão (adotados) | Meta da equipe: 100% (D10). Abaixo disso, investigar a causa na revisão da iteração. O framework pede revisar *outliers* de tempo, mas o script não calcula o tempo médio até a aprovação |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |
| Mudança de definição | O denominador era "PRs abertos" e passou a ser "PRs mergeados". "Revisado" passou a ser "aprovado antes do merge". Não comparar com a medição manual anterior |

#### I2 — PRs aprovados antes do merge (P3 Tabela 6, linha 16, adaptado)

| Campo | Especificação |
|---|---|
| Necessidade de informação | O código integrado passou pela revisão de outra pessoa? |
| Medidas base | PRs mergeados. PRs mergeados com aprovação antes do merge |
| Medida derivada | I2 = PRs aprovados antes do merge ÷ PRs mergeados |
| Indicador | Percentual por domingo, desde o início do projeto |
| Modelo de análise | PR mergeado sem aprovação indica falha do processo de integração. Complementa I1: I2 diz *se* houve aprovação, e I1 diz se foi *a tempo* |
| Critérios de decisão (adotados) | Meta: 100%. <!-- CONFIRMAR com a política de PR do grupo --> A Parte 3 cita a falta de revisão por pares como causa raiz de dívida técnica (P3 11.3) |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |

#### I3 — Retrabalho (issues) (P1 ICM, linhas 18 e 19)

| Campo | Especificação |
|---|---|
| Necessidade de informação | Quanto do trabalho dado como concluído volta a ser feito? O critério Done está sendo cumprido? |
| Medidas base | Issues concluídas. Issues concluídas com a label `correcao`. Issues reabertas (eventos de reabertura) |
| Medida derivada | I3 = (issues concluídas com a label `correcao` ou reabertas) ÷ issues concluídas <!-- CONFIRMAR se a issue que tem os dois sinais é contada uma só vez --> |
| Indicador | Percentual por domingo, desde o início do projeto |
| Modelo de análise | Um valor alto ou crescente sugere que as issues estão sendo fechadas antes de cumprir o Done (D4). Na leitura da Parte 3, a falha em detectar defeitos é retrabalho futuro escondido (P3, Tabela 5) |
| Critérios de decisão | Não há limiar no framework. <!-- CONFIRMAR o limiar do grupo --> |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |
| Mudança de definição | Antes só contava issues reabertas. Agora conta também a label `correcao` (D14) |

#### I4 — Retrabalho (horas) (P1 ICM, linha 19)

| Campo | Especificação |
|---|---|
| Necessidade de informação | Quanto esforço a equipe gasta refazendo ou corrigindo? |
| Medidas base | Horas reais das issues de retrabalho (critério de I3). Horas reais das issues concluídas |
| Medida derivada | I4 = horas reais das issues de retrabalho ÷ horas reais das issues concluídas |
| Indicador | Percentual por domingo, desde o início do projeto |
| Modelo de análise | Compara o custo do retrabalho com o custo total. Pode ser alto mesmo com I3 baixo, se poucas issues de retrabalho forem grandes |
| Critérios de decisão | Não há limiar no framework. <!-- CONFIRMAR o limiar do grupo --> |
| Limitação | Depende de `horas.csv`. Issues sem horas reais (I9) subestimam o numerador ou o denominador |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |

### Calendário e Progresso

#### I5 — Conclusão de issues por milestone (P2 8.3, adaptado)

| Campo | Especificação |
|---|---|
| Necessidade de informação | As issues foram entregues como comprometido? Quais estão em risco? |
| Medidas base | Issues do milestone, sem as descartadas (D3). Issues concluídas do milestone |
| Medida derivada | I5 = issues concluídas ÷ issues do milestone, **acumulado até a data**. Percentual concluído do framework: concluído × 100 ÷ comprometido |
| Indicador | Um valor por milestone, que evolui a cada coleta até o prazo. Pode ser agregado por responsável |
| Modelo de análise | A equipe conclui o que se comprometeu? Há risco de atraso na entrega? Issues não concluídas voltam ao backlog e são repriorizadas (P2 8.3) |
| Critérios de decisão | Do framework (P2 8.3), aplicados ao valor no prazo do milestone em relação a 100%: diferença acima de 5%, a equipe investiga as causas. Acima de 10% de atraso, a gestão investiga e considera ação corretiva |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |
| Mudança de definição | Antes era "fechadas no período ÷ planejadas no milestone". Agora é um valor por milestone, acumulado, e não por período. Ver a atenção sobre o denominador na decisão D6 |

#### I6 — Desvio de prazo médio (P1 ICM, linha 8, adaptado)

| Campo | Especificação |
|---|---|
| Necessidade de informação | As issues são fechadas no prazo combinado? |
| Medidas base | Data de fechamento de cada issue concluída. Prazo (data de vencimento) do milestone da issue |
| Medida derivada | I6 = média de (data de fechamento − prazo do milestone), em dias, nas issues concluídas |
| Indicador | Dias, por domingo, desde o início do projeto. Valor positivo = fechamento depois do prazo. Negativo = antes |
| Modelo de análise | Há atraso sistemático? O desvio muda de uma iteração para outra? Ler junto com I5, pois a média pode esconder issues muito adiantadas compensando outras muito atrasadas |
| Critérios de decisão | Não há limiar no framework. <!-- CONFIRMAR o limiar do grupo --> |
| Coleta e análise | Automática (D7). Análise na revisão da iteração |
| Mudança de definição | Antes era o desvio de cada issue (data real − data planejada). Agora é a média, e a data planejada é o prazo do milestone |

### Recursos e Custos

#### I7 — Distribuição de esforço por pessoa (P1 ICM, linha 7)

| Campo | Especificação |
|---|---|
| Necessidade de informação | O esforço está distribuído entre os integrantes? |
| Medida base | Horas reais declaradas por integrante e por issue em `horas.csv` (D11) |
| Medida derivada | I7 = horas reais da pessoa ÷ total de horas reais |
| Indicador | Percentual de cada integrante, por domingo, desde o início do projeto |
| Modelo de análise | Há sobrecarga ou ociosidade? A distribuição é coerente com os papéis? |
| Critérios de decisão (adotados) | Desvio superior a 10% de um integrante em relação à média do grupo leva à avaliação de redistribuição de issues |
| Limitação | Horas autodeclaradas. Como o arquivo não tem data, as horas de uma issue pertencem à iteração do seu milestone |
| Mudança de definição | Substitui "issues fechadas por integrante ÷ total de issues fechadas". As horas refletem o esforço melhor que a contagem, porque as issues têm tamanhos diferentes |

#### I8 — Esforço real / estimado (P1 ICM, linhas 8 e 9)

| Campo | Especificação |
|---|---|
| Necessidade de informação | As estimativas por issue são precisas e viáveis? |
| Medidas base | Horas reais (`horas.csv`) e horas estimadas (campo do template da issue), só nas issues que têm os dois registros |
| Medida derivada | I8 = horas reais ÷ horas estimadas. Valor 1,0 = estimativa exata. Acima de 1,0 = subestimado. Abaixo = superestimado. Equivale ao erro de estimativa anterior, (real − estimado) ÷ estimado, somado a 1 |
| Indicador | Razão agregada por domingo, desde o início do projeto <!-- CONFIRMAR se há quebra por milestone ou por pessoa --> |
| Modelo de análise | A equipe subestima ou superestima de forma sistemática? A precisão melhora entre iterações? |
| Critérios de decisão (adotados) | Razão fora do intervalo de 0,90 a 1,10 (erro acima de ±10%) leva à recalibração das estimativas no próximo planejamento |
| Limitação | Só entram issues com estimativa e com horas declaradas. Em issues com mais de um responsável, compara-se a soma das horas reais com a estimativa da issue |

#### I9 — Issues concluídas sem horas reais (controle de qualidade do dado)

| Campo | Especificação |
|---|---|
| Necessidade de informação | Os indicadores que dependem das horas reais (I4, I7 e I8) são confiáveis? |
| Medida base | Contagem de issues concluídas sem horas reais declaradas <!-- CONFIRMAR se a linha com XX em horas.csv conta como sem horas --> |
| Indicador | Contagem por domingo, desde o início do projeto |
| Modelo de análise | Quanto maior a contagem, menos representativos são I4, I7 e I8 |
| Critérios de decisão (adotados) | Meta: 0 ao fechar o milestone. <!-- CONFIRMAR --> Valor maior que 0 leva à cobrança das horas antes da revisão da iteração |
| Observação | Este indicador não existe no framework. É um controle sobre a qualidade do dado e responde ao princípio de que as medidas devem ser confiáveis para apoiar decisões (P1, seção 5) |

## 5. Coleta e automação

| Dado | Fonte | Frequência | Mecanismo | Situação |
|---|---|---|---|---|
| Indicadores I1 a I9 | Issues (corpo, labels e eventos), milestones e PRs | Domingo 23:59, a cada issue fechada e a cada publicação da GitPage | Script `scripts/coletar_metricas_psm.py` (PR #28) <!-- CONFIRMAR o nome do workflow e se o PR #28 já foi integrado --> | Implementado no PR #28 |
| Valores calculados | `docs/gestao/indicadores.md` e CSVs em `docs/gestao/evidencias/` | A cada execução do script, com o histórico recalculado por inteiro | Gerados pelo script | Implementado no PR #28 |
| Horas reais por issue e responsável | `docs/gestao/evidencias/horas.csv` | Domingo 23:59 e a cada issue fechada | Workflow `horas_semanal.yml` e script `sync_horas_csv.py` | Implementado |
| Horas estimadas por issue | Campo "Horas estimadas" no corpo da issue (template) | No planejamento da iteração | Preenchimento manual pelo responsável e leitura pelo script <!-- CONFIRMAR que o script lê esse campo --> | Em uso |
| Interpretação e decisão | Seção 6 e atas | Revisão de cada iteração | Manual | Em uso |

O histórico tem uma linha por domingo, desde o início do projeto. <!-- CONFIRMAR se o valor de cada domingo é acumulado até a data ou só da semana. I5 é explicitamente acumulado --> Como o histórico é recalculado a cada execução, preencher horas ou corrigir uma label hoje altera os valores de domingos passados. Para registrar uma medição como evidência da revisão, cite a data do domingo na ata.

Regras do `horas.csv`: cada responsável substitui o `XX` da sua linha pelas horas, com ponto decimal. Quando uma issue ganha um segundo responsável, surge outra linha com o mesmo número e título. Quando um responsável é removido, a linha só é apagada se ainda estiver como `XX`. Linhas com horas preenchidas são sempre mantidas.
