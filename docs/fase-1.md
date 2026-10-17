# Fase 1 — Estabelecer os requisitos da avaliação

<!--
Referência: ISO/IEC 25040, atividade 1. Critérios da Fase 1 (Moodle) indicados em cada seção.
Lembrete: nenhuma imagem sem texto alternativo — use ![descrição da imagem](assets/img/arquivo.png).
-->

## 1. Propósito da avaliação e uso pretendido

### 1.1 Contexto

O [Sua Grade UnB](https://suagradeunb.com.br/) é uma aplicação web que ajuda estudantes da
Universidade de Brasília a montar a grade horária do semestre. O estudante busca disciplinas
por nome ou código, seleciona as que deseja cursar e o sistema gera combinações de turmas sem
conflito de horário, que podem ser salvas na conta do usuário ou no próprio navegador. Os dados de turmas são obtidos por *web scraping* das turmas do SIGAA.

O sistema foi desenvolvido no segundo semestre de 2023 por seis estudantes na disciplina de Métodos de Desenvolvimento de Software (MDS) e é open source.

Repositório disponível em: [unb-mds/2023-2-SuaGradeUnB](https://github.com/unb-mds/2023-2-SuaGradeUnB).

Depois da disciplina, o projeto continuou com manutenções eventuais:

**Tabela 1 — Atividade no repositório do Sua Grade UnB**

| Ano | Commits na branch principal | Observação |
|-----|-----------------------------|------------|
| 2023 | 475 | Desenvolvimento durante a disciplina |
| 2024 | 33 | Novas funcionalidades pontuais (ex.: calculadora de IRA) |
| 2025 | 5 | Majoritariamente atualizações automáticas de dependências |
| 2026 | 2 | Correção do *web scraping* após mudança no SIGAA, feita por contribuidor externo |

Fonte: Histórico do repositório (consulta em 16/10/2026).

O que motiva a avaliação do produto:

1. **Uso recorrente e concentrado:** o sistema é usado a cada período de matrícula, quando muitos estudantes acessam ao mesmo tempo.
2. **Manutenção por voluntários:** a equipe idealizadora do projeto já concluiu a disciplina, e correções recentes vieram de propostas feitas por contribuidores externos.
3. **Dependência de uma fonte externa instável:** mudanças no SIGAA quebram a coleta de dados, como ocorreu em 2026 e o webscrapping que teve de ser refatorado. O que exige que o código seja fácil de entender e modificar por quem não o escreveu.

Até onde verificamos, o produto nunca passou por uma avaliação sistemática de qualidade.

### 1.2 Propósito

Avaliar a qualidade do Sua Grade UnB, em operação, para **identificar e priorizar os problemas de qualidade que mais afetam os estudantes no período de matrícula e a continuidade da manutenção do sistema por voluntários**, produzindo recomendações de melhoria para os mantenedores e embasando a ação de melhoria que a equipe executará na Fase 4.

### 1.3 Uso pretendido: decisões apoiadas

Esperamos que os resultados ajudem nas decisões da Tabela 2.

**Tabela 2 — Decisões apoiadas pela avaliação**

| Decisão | Quem decide |
|---------|-------------|
| D1 — Quais problemas corrigir primeiro antes do próximo período de matrícula | Mantenedores do Sua Grade UnB |
| D2 — Qual ação de melhoria executar na Fase 4 | Nossa equipe |
| D3 — Por qual parte do código começar a contribuir | Contribuidores externos e futuros mantenedores |

Os resultados serão publicados nesta GitPage e no artigo da disciplina. As recomendações destinadas aos mantenedores (D1) serão registradas como *issues* no repositório do Sua Grade UnB.

## 2. Requisitante e partes interessadas


### 2.1 Requisitante

A avaliação trata-se de uma **avaliação
independente**, conduzida em contexto acadêmico. O **requisitante** é a equipe Elizabeth
Friedman, que também atua como **avaliadora**, sob orientação da disciplina de Qualidade de Software. Os
**principais destinatários** dos resultados são os mantenedores do Sua Grade UnB, que tomam a
decisão D1 da [Tabela 2](#13-uso-pretendido-decisoes-apoiadas).

Consequências da avaliação:

- A equipe não tem acesso a logs e nem banco de dados de produção.
- As medições usarão o site público, o código-fonte e a reprodução local do sistema.

### 2.2 Mapa de partes interessadas

**Tabela 3 — Partes interessadas, necessidades e influência na avaliação**

| Parte interessada | Papel | Necessidades e expectativas | Critério de sucesso da avaliação | Influência na avaliação |
|-------------------|-------|-----------------------------|----------------------------------|-------------------------|
| Equipe Elizabeth Friedman | Requisitante e avaliadora | Avaliação viável em cerca de seis semanas, com dados base de evidências para a ação de melhoria | Todas as métricas coletadas conforme o plano da Fase 3; ação de melhoria justificada por resultados medidos (D2) | Limita escopo e profundidade ao prazo e aos recursos disponíveis |
| Profa. Cristiane Ramos | Orientadora e avaliadora do processo | Aplicação correta do processo SQuaRE, do GQM e do PSM/CID, com rastreabilidade dos dados | Resultados rastreáveis do dado bruto ao julgamento; entregas nos prazos | Define restrições de método: processo ISO/IEC 25040, três a quatro características, GQM, prazos das entregas |
| Mantenedores do Sua Grade UnB | Desenvolvedores, mantenedores e operadores | Manter o sistema funcionando a cada semestre e saber o que priorizar com tempo limitado | Receber problemas localizados e recomendações que possam virar *issues* (D1) | Direciona a avaliação para o código e a arquitetura, motivando a característica **Manutenibilidade** e recomendações entregues no formato de *issues* |
| Contribuidores externos | Desenvolvedores eventuais | Entender o código e contribuir | Diagnóstico de quais módulos são mais difíceis de analisar, modificar e testar (D3) | Reforça **Manutenibilidade**, com foco em analisabilidade, modificabilidade e testabilidade |
| Estudantes da UnB | Usuários finais | Montar a grade durante a matrícula, sem conflitos de horário, inclusive no celular | Identificação dos obstáculos no fluxo principal e dos tempos de resposta que podem prejudicar o uso | Motiva **Usabilidade** e **Eficiência**. As tarefas avaliadas seguirão o fluxo principal: buscar disciplina, selecionar turmas, gerar grade e salvar |
| Universidade de Brasília (SIGAA) | Fonte dos dados | Que a coleta não sobrecarregue o SIGAA e que os estudantes não sejam induzidos a erro por dados desatualizados ou incompletos | Avaliação feita sem gerar carga sobre o SIGAA | Restringe o método: não faremos coletas repetidas no SIGAA |

As características citadas na última coluna são as selecionadas pela equipe; a justificativa e
a priorização entre elas estão na [Seção 5](#5-selecao-e-priorizacao-das-caracteristicas).

## 3. Tipo de produto e descrição do software

<!--
Critério 3: classificar o tipo de produto; descrever módulos, interfaces, dependências e restrições.
Para nota máxima: diagrama de contexto/arquitetura e implicações para a avaliação (o que dá / não dá para medir agora).
Diagramas podem ser feitos em Mermaid diretamente aqui (bloco ```mermaid).
-->

*A preencher.*

## 4. Modelo de qualidade

<!--
Critério 4: modelo escolhido (ISO/IEC 25010), adaptações JUSTIFICADAS por contexto e stakeholders,
diagrama com ligações às subcaracterísticas.
-->

*A preencher.*

## 5. Seleção e priorização das características

<!--
Critério 5: 3 a 4 características (a especificação do trabalho pede 3–4; NÃO incluir usabilidade).
Para nota máxima: método explícito de priorização (ex.: matriz impacto × risco, MoSCoW com pesos) e trade-offs discutidos.
-->

| Característica (ISO/IEC 25010) | Subcaracterísticas | Justificativa | Prioridade |
|--------------------------------|--------------------|---------------|------------|
| | | | |

## 6. Escopo, profundidade e objetos de avaliação

<!--
Critério 6: o que entra, o que fica fora e por quê; nível de profundidade; limites de validade dos resultados.
-->

*A preencher.*

## 7. Objetivos de Desenvolvimento Sustentável (ODS)

<!--
Critério 7: ODS + metas + indicadores, com justificativa da pertinência ao software.
-->

*A preencher.*

---

Próxima etapa: [Fase 2 — Especificação da avaliação](fase-2.md).
