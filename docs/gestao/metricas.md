# Gestão do projeto — Métricas PSM/CID

<!--
Seção 2 da especificação: registrar medições, interpretação e DECISÕES de gestão decorrentes.
Evidências no repositório: commits, issues, milestones, dashboards.
-->

As medições de acompanhamento seguem o modelo PSM/CID nas três categorias exigidas.
As evidências estão no repositório (issues, milestones e commits) e nas
[atas de reunião](atas.md).

## Desempenho dos processos

| Indicador | Fórmula | Fonte | Frequência |
|-----------|---------|-------|------------|
| Taxa de PRs revisados no prazo | PRs revisados em até 48h / PRs abertos | Pull requests (GitHub) | Semanal |
| Taxa de retrabalho | Issues reabertas / issues fechadas | Issues (GitHub) | Semanal |

## Calendário e progresso

| Indicador | Fórmula | Fonte | Frequência |
|-----------|---------|-------|------------|
| Conclusão de issues planejadas | Issues fechadas no período / issues planejadas no milestone | Issues e milestones | Semanal |
| Desvio de prazo | Data real de conclusão − data planejada (dias) | Milestones e issues | Semanal |

## Recursos e custos

| Indicador | Fórmula | Fonte | Frequência |
|-----------|---------|-------|------------|
| Distribuição de carga | Issues fechadas por integrante / total de issues fechadas | Issues (assignees) | Semanal |
| Contribuição por integrante | Commits por integrante no período | Histórico de commits | Semanal |

## Registro de medições e decisões

| Data | Indicador | Valor | Interpretação | Decisão tomada |
|------|-----------|-------|---------------|----------------|
| 19/10 | Conclusão de issues planejadas | 13/13 (100%) | Todas as issues planejadas para a semana foram concluídas no prazo, sem atraso acumulado para a semana 2. | Manter o ritmo e incluir na semana 2 as issues restantes do milestone, sem reduzir escopo. |
| 19/10 | Taxa de PRs revisados no prazo | 10/10 (100%) | Todas as revisões ocorreram em até 48h, então a revisão não foi gargalo. | Manter a regra de revisão em até 48h e checá-la de novo na semana 2. |
| 19/10 | Distribuição de carga | 13/13 issues fechadas pelo responsável designado | A divisão do trabalho foi respeitada, sem issues sem dono nem reatribuições. | Manter a atribuição por integrante e, se alguém terminar antes, puxar issues do backlog em vez de esperar. |
