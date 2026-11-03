# Instrumentos de M8 e M9

Versão 0.1 · [Protocolo comum](protocolo.md).

## 1. Inventário M8

Inventário preliminar por leitura do commit fixado, em 03/11/2026. Os indícios abaixo
não demonstram proteção efetiva. Validar disponibilidade e completar o inventário
percorrendo todos os controles no ambiente real antes da coleta. Executar cada risco
disponível em computador e celular e na modalidade aplicável. Registrar uma linha
por cenário/dispositivo/modalidade no [modelo CSV](inventario-m8.csv).

| Risco | Preparação e ação | Verificação de proteção | Indício no código |
|---|---|---|---|
| R01 — Excluir grade local | Restaurar G0 no navegador; acionar exclusão e cancelar | Confirmação anterior à perda e G0 integral preservada após cancelamento e recarga | `web/app/components/SchedulePreview/SchedulePreview.tsx`, `DeleteModal` |
| R02 — Excluir grade na conta | Restaurar G0 em conta descartável; acionar exclusão e cancelar | Cancelamento preserva G0 também ao consultar novamente a conta | Mesmo componente e `web/app/utils/api/deleteSchedule.ts` |
| R03 — Sair com grade apenas local | Restaurar G0 somente local; acionar Sair no perfil e cancelar | Aviso anterior à perda, cancelamento mantém acesso e G0 recuperável | `web/app/schedules/profile/page.tsx`, modal e `handleLogoutAndRedirect` |
| R04 — Recarregar durante montagem | Restaurar S1 ainda não salva; recarregar página | Prevenção, confirmação cancelável ou recuperação integral das escolhas | Inspecionar contextos da seleção e navegação; comportamento ainda não verificado |
| R05 — Navegar para fora da montagem | Restaurar S1; usar navegação interna e, em cenário separado, voltar do navegador | Escolhas preservadas ou perda evitada; cancelar confirmação quando existir | Disponibilidade e caminhos a confirmar em execução |
| R06 — Trocar de conta | Restaurar G0 apenas local em sessão de teste; acionar Trocar de conta | Verificar aviso anterior ou preservação/recuperação integral | `web/app/schedules/profile/page.tsx`, `signInWithGoogle` |

Dividir R05 em cenários separados no inventário final. Acrescentar substituição de
grade e outras ações de descarte caso existam; se não existirem, registrar ausência
verificada e evidência, sem inventar controles. Para cada cenário, registrar estado
inicial, passos exatos, mecanismo, evidências antes/depois, conteúdo perdido e resultado.
Confirmar local/conta separadamente quando a ação se aplicar a ambas.

Restaurar a grade antes de cada execução. Se houver prevenção, demonstrar que a
ação foi impedida; se houver confirmação, **testar cancelar** e conferir o conteúdo;
se houver recuperação, executar a ação em dados descartáveis e recuperar toda a grade.
Um aviso posterior à perda não protege. Confirmar conscientemente a exclusão não
exige recuperação quando uma confirmação anterior eficaz é o mecanismo avaliado.

Estados de disponibilidade: `a_validar`, `disponivel`, `ausente`, `sem_acesso`.
Ausente exige evidência de que a ação não existe; sem acesso representa cobertura
pendente. Ação acessível sem proteção é insucesso, nunca ausência. Calcular P8/R8
por dispositivo/modalidade; qualquer risco executado sem proteção determina nota 0
nesse conjunto. Aceitação: 100% de proteção; sem riscos válidos, Não calculável.

## 2. Gabarito M9

Preencher exemplos concretos de respostas aceitas após conferir cada estado no
ambiente; congelar antes das sessões. Não ler o gabarito ao participante.

Perguntar, sem complementos que revelem o estado: **“Qual é o estado atual?”** e
**“O que você pode fazer agora?”**. Se a pessoa solicitar esclarecimento, repetir a
pergunta sem explicar a interface. Aceitar sinônimos e qualquer próxima ação de fato
disponível; não exigir o nome exato de um botão. Sucesso exige as duas partes corretas.

| Ponto | Estado real a preparar e comprovar | Interpretação correta | Próxima ação a aceitar se disponível |
|---|---|---|---|
| V01 | A1+B1 selecionadas, sem geração | Há turmas escolhidas; ainda não há resultado gerado | Revisar escolhas ou iniciar geração |
| V02 | Requisição de geração pendente | O sistema está processando; resultado ainda não está disponível | Aguardar o processamento; outra ação apenas se habilitada e válida |
| V03 | Resposta concluída com grade compatível | A geração terminou e há uma opção resultante | Consultar/escolher resultado, salvar ou exportar conforme controles reais |
| V04 | G0 salva na modalidade atribuída, com estado de armazenamento conferido | A grade ficou salva e é possível dizer onde, conforme a informação da interface | Consultar/abrir a grade salva ou outra ação disponível |

Se V04 não permitir distinguir salvamento no navegador/conta pela interface,
registrar informação insuficiente como insucesso; não fornecer a resposta verbalmente.
Adicionar estados de erro ou salvamento em andamento apenas com justificativa e
gabarito congelados antes da coleta.

### Apresentação do estado transitório V02

O código de geração aciona `setLoading` em
`web/app/schedules/home/components/GenerateScheduleButton.tsx`; o layout usa
`web/app/components/LoadingScreen.tsx`. Isso é um indício, não validação de observabilidade.

No ensaio técnico, tentar capturar a requisição de geração naturalmente pendente.
Se durar pouco, testar retenção controlada da resposta no ambiente de avaliação,
somente em M9, preservando resposta, rótulos e controles originais. Registrar ferramenta,
endpoint, intervalo e limitação de validade. Essa condição não entra em M6 nem em
medições de desempenho. Não apresentar tela inventada como estado real.

No piloto, demonstrar que o estado permanece visível durante as duas perguntas em
computador e celular reais e capturar a tela no instante da pergunta. Se mudar antes
de a pessoa conseguir observá-lo, registrar falha de apresentação/não coleta e
rever o método antes da coleta formal. Ausência de resposta a estado apresentado
adequadamente ou informação insuficiente na interface conta como insucesso.

Guardar resposta literal em acesso restrito; transcrever versão revisada para
publicação. Registrar correção de estado e ação separadamente e a classificação
final. Calcular C9/V9 por ponto/dispositivo; mínimo 90% com cobertura prevista completa.
