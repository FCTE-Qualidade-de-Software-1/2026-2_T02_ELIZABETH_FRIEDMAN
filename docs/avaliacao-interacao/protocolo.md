# Protocolo de capacidade de interação — M6 a M9

Versão 0.2 · 08/11/2026 · [Issue #40](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/issues/40).
Situação: preparado para validação; piloto e recrutamento ainda pendentes.

## 1. Preparação e congelamento

Usar o commit `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`, sem modificar
mensagens, controles ou proteção para facilitar as tarefas. O ambiente e a massa
dependem de #37. Não consultar o SIGAA durante sessões.

Antes do piloto, preencher um manifesto restrito por configuração com:

- URL, commit, versão deste protocolo, responsável e contato de pesquisa.
- Sistema operacional, modelo do dispositivo, navegador/versão, resolução e viewport.
- Identificação e hash do arquivo da massa; semestre, departamentos e disciplinas.
- Disciplina A com turmas A1 e A2 e disciplina B com turma B1: combinações A1+B1 e A2+B1 sem choque.
- Códigos, nomes, horários e identificadores reais de A/A1/A2/B/B1; substituir os símbolos nos cartões de tarefas antes de apresentá-los.
- Grades iniciais S0 (sem seleção), S1 (A1+B1 selecionadas), G0 (grade A1+B1 salva), localização do backup e passos de restauração.
- Modalidades previstas: navegador e conta; identificar conta descartável e acesso funcional, sem guardar senhas no manifesto.

Esses símbolos são requisitos da massa, não disciplinas já verificadas. Não iniciar
sessões com cartões sem nomes reais. Antes do congelamento, demonstrar a restauração:
limpar somente dados de teste, repor o backup, entrar na modalidade prevista e conferir
disciplinas, turmas e horários do estado inicial. Registrar evidência. Restaurar S0
antes de cada M6; manter o armazenamento durante a prova de recuperação. Para M7/M8/M9,
restaurar o estado específico antes de cada cenário. No celular repetir a preparação
em navegador real; emulação não substitui essa verificação.

Fixar após o piloto a distribuição de modalidades por sessão: cada participante
executa **uma única M6**, no dispositivo e modalidade designados previamente.
Não repetir M6 na outra modalidade com a mesma pessoa. A amostra revisada é de
quatro participantes, dois por dispositivo. Se houver distribuição entre modalidades,
publicar o tamanho efetivo de cada recorte; duas pessoas por dispositivo não equivalem
a duas por dispositivo/modalidade. Ampliar o recrutamento antes da coleta se forem
necessárias duas por cada combinação de dispositivo e modalidade.
Modalidade indisponível permanece não avaliada, sem extrapolar a outra.

## 2. Sessão e instruções comuns

Sessões online por Google Meet, com Júlia e João como moderador e observador.
Validar antes do piloto acesso remoto privado ao ambiente de teste no dispositivo
do participante; o endereço local da máquina do avaliador não basta para acesso pela
internet. Usar compartilhamento da tela do dispositivo atribuído, com autorização
de captura/gravação conferida; compartilhar tela ao vivo não autoriza gravá-la.
Se a transmissão ou conexão impedir a observação, registrar falha de infraestrutura,
sem atribuí-la à interface. Confirmar no piloto a viabilidade no celular real.

Reservar até 45 minutos. Aplicar M6 → M7 → M9, sempre no dispositivo atribuído;
M8 é inspeção separada pelo avaliador. Obter consentimento e verificar triagem
antes de abrir a interface. A mesma pessoa do piloto fica excluída da amostra formal.

Ler: “Estamos avaliando o Sua Grade UnB. Vou apresentar objetivos para você realizar
usando a interface. Você pode consultar as orientações da própria aplicação e pode
interromper a participação a qualquer momento. Durante as tarefas, vou observar
sem indicar os passos. Se precisar de ajuda, pode pedir; esse pedido será registrado.”

Não exigir verbalização contínua durante M6/M7. Para pedido de ajuda, responder
uma vez “Tente usando as informações disponíveis na interface”. Se houver orientação
sobre como executar, registrar conteúdo, instante e motivo; classificar insucesso
na tarefa que exige independência. Nunca atribuir sucesso após ensinar o caminho.
Após insucesso, pode-se encerrar a tarefa e preparar a próxima, sem apagar o registro.

Os limites abaixo são decisões iniciais do protocolo, a conferir no piloto. Alterações
exigem versão e justificativa antes da coleta formal, sem ajuste a resultados desejados.

## 3. M6 — Primeiro uso

Exploração E = 3 minutos; tempo total T = 15 minutos, contado desde a disponibilização
da interface. A execução tem o tempo restante de T, não quinze minutos adicionais.
Registrar início/fim de exploração e execução separadamente. Não formular perguntas
M9 durante M6.

1. Confirmar ausência de uso prévio, modalidade e S0; iniciar cronômetro ao abrir a interface.
2. Ler: “Você tem até três minutos para conhecer livremente a aplicação. Depois receberá uma tarefa.”
3. Ao terminar a exploração, entregar: “Monte uma grade com as disciplinas [nome/código A] e [nome/código B], usando as turmas [A1] e [B1]. Gere uma opção compatível, salve-a [no navegador/na conta, conforme cartão] e deixe-a disponível para consultar novamente.”
4. Observar até concluir ou atingir T. Registrar desistência, ajuda, erros e expiração.
5. Dentro de T, verificar seleção, horários, geração e salvamento. Solicitar “Mostre a grade que ficou salva para consultar novamente”. Conferir recuperação após recarregar, preservando a modalidade/contexto; registrar quem recarregou e a evidência.
6. Sucesso exige todos os resultados corretos, independência e recuperação dentro de T. Não basta mensagem de sucesso nem exportação PDF.

Uma linha M6 por sessão. `S6/N6`: incluir insucessos e expirações entre sessões
válidas iniciadas. Separar por dispositivo e modalidade; mínimo operacional 80%.

## 4. M7 — Controle da grade

Limite de 3 minutos para cada tarefa; iniciar na entrega do cartão, após restauração.
Usar nomes reais e solicitar apenas o resultado, sem indicar botão ou caminho.

| ID | Estado inicial | Texto do cartão | Resultado esperado |
|---|---|---|---|
| M7-SEL | S0 | “Inclua [A1] de [A] e [B1] de [B] nas suas escolhas.” | Somente A1+B1 selecionadas |
| M7-REM | S1 | “Deixe nas suas escolhas apenas [B1] de [B].” | A1 removida, B1 preservada |
| M7-ALT | S1 | “Troque a turma [A1] pela [A2], mantendo [B1].” | A2+B1 selecionadas, A1 ausente |

Capturar antes/depois, conferir o estado final e registrar correções e ajuda.
Uma linha por tarefa; calcular S7/N7 por tarefa/dispositivo, mínimo 90%. Bloqueio
reproduzível de controle que impeça executar a tarefa determina nota 0 nesse cenário,
conforme Fase 2. Uso prévio adquirido em M6 deve constar no contexto; estas tarefas
posteriores não serão apresentadas como observações independentes de primeiro uso.

## 5. M8 e M9

Aplicar os [instrumentos](instrumentos.md). Em M9 usar até 60 segundos por ponto,
com as duas perguntas, registrando a resposta antes de dar retorno. A ordem é
seleção → geração em andamento → geração concluída → salvamento. Registrar que
ocorre após M6/M7 e não usar esses dados como compreensão no primeiro contato.

## 6. Registro e julgamento

Usar os [CSV e convenções](registros.md). Falhas de interação, defeitos da aplicação,
desistência por dificuldade, ajuda incompatível com independência e expiração são
insucessos, mantendo a observação válida no denominador. Falhas comprovadas de
equipamento, infraestrutura ou roteiro são inválidas, preservadas com justificativa.
Ponto não apresentado é não coletado e reduz cobertura. Denominador zero: Não
calculável, sem nota; métrica sem observações válidas: Não avaliada.

Publicar numerador/denominador, percentual e cobertura planejada/realizada por
recorte. Não misturar computador e celular nem calcular média de notas. Usar as
faixas e a menor nota com cobertura completa conforme [Fase 2, §4.4](../fase-2.md#44-regras-de-aplicacao-e-julgamento-de-interacao-m6m9).
Registrar fim da sessão, problemas e localização restrita das evidências. Agradecer
e lembrar o contato de retirada dos dados.