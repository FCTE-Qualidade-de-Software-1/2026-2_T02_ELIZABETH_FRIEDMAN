# Protocolo de capacidade de interação — M6 a M9

Versão 0.3 · 15/11/2026 · [Issue #40](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/issues/40).
Situação: aplicado em 15/11/2026 nas sessões P01 a P04, sem piloto; os desvios estão na
[Fase 4, seção 2.3](../fase-4.md#23-g3-capacidade-de-interacao).
A versão 0.3 passa as sessões para o site público, com a conta Google do participante
([Fase 3, seção 4.1](../fase-3.md#41-o-que-mudou-em-relacao-a-fase-2-e-por-que), linha 6).

## 1. Preparação e congelamento

As sessões usam o site público [suagradeunb.com.br](https://suagradeunb.com.br/),
como a [Fase 1, Tabela 11](../fase-1.md#61-objetos-de-avaliacao) já previa para
Capacidade de interação. Em 15/11/2026, o último commit da `main` do produto era
`3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`, e o registro de *deployments* do GitHub
mostrava esse commit publicado em Production em 15/02/2026, sem publicação posterior.
Isso indica que o site roda a versão avaliada, mas não prova. Repetir as duas
conferências em cada dia de sessão e registrá-las no manifesto. Se aparecer uma
publicação nova, parar a coleta e decidir com a equipe antes de continuar. Não
modificar mensagens, controles ou proteção para facilitar as tarefas. Não consultar
o SIGAA durante sessões.

Antes do piloto, preencher um manifesto restrito por configuração com:

- URL, data, último commit e último *deployment* conferidos, versão deste protocolo, responsável e contato de pesquisa.
- Sistema operacional, modelo do dispositivo, navegador/versão, resolução e viewport.
- Período oferecido pelo site e captura datada da busca de A e B com as turmas A1, A2 e B1, repetida em cada dia de sessão, porque os mantenedores podem atualizar os dados.
- Disciplina A com turmas A1 e A2 e disciplina B com turma B1: combinações A1+B1 e A2+B1 sem choque.
- Códigos, nomes, horários e identificadores reais de A/A1/A2/B/B1; substituir os símbolos nos cartões de tarefas antes de apresentá-los.
- Estados S0 (nenhuma seleção e nenhuma grade salva na conta), S1 (A1+B1 selecionadas), S2 (A2+B1 selecionadas) e G0 (grade A1+B1 salva, usada só em M8 pelo avaliador).
- Modalidade: conta. O participante entra com a própria conta Google; não guardar e-mail nem senha no manifesto.

Esses símbolos são requisitos dos dados do período, não disciplinas já verificadas.
Não iniciar sessões com cartões sem nomes reais. No aparelho do participante não há
backup nem automação. Na versão avaliada, as turmas selecionadas ficam só na memória
da página e somem ao recarregar; as grades geradas ficam no armazenamento do navegador,
e as salvas, na conta. Assim, S0 se obtém recarregando a página com uma conta sem grades
salvas; em aparelho da equipe, limpar também os dados do site antes do login. Conferir
esse comportamento no site antes do congelamento e registrar evidência. Manter o
armazenamento durante a prova de recuperação de M6. No celular repetir a verificação
em navegador real; emulação não a substitui.

Cada participante executa **uma única M6**, no dispositivo designado previamente,
sempre na modalidade conta: na versão `3d399e7` não há ação de salvar no navegador
([Fase 3, seção 4.1](../fase-3.md#41-o-que-mudou-em-relacao-a-fase-2-e-por-que), linha 5).
Não repetir M6 com a mesma pessoa. A amostra revisada é de quatro participantes,
dois por dispositivo. Dispositivo indisponível permanece não avaliado, sem extrapolar
o outro.

## 2. Sessão e instruções comuns

Sessões online por Google Meet, com Júlia e João como moderador e observador.
A pessoa acessa o site público no dispositivo atribuído, próprio ou fornecido pela
equipe. Usar compartilhamento da tela desse dispositivo, com autorização
de captura/gravação conferida; compartilhar tela ao vivo não autoriza gravá-la.
Se a transmissão ou conexão impedir a observação, registrar falha de infraestrutura,
sem atribuí-la à interface. Confirmar no piloto a viabilidade no celular real.

Reservar até 45 minutos. Aplicar M6 → M7 → M9, sempre no dispositivo atribuído;
M8 é inspeção separada pelo avaliador. Obter consentimento e verificar triagem
antes de abrir a interface. A mesma pessoa do piloto fica excluída da amostra formal.

Antes de iniciar o cronômetro de M6, pedir que a pessoa entre no site com a própria
conta Google, pela opção de entrar com o Google da tela inicial. Essa escolha é indicada
pelo moderador e não é observada. A tela de login do Google fica fora do escopo
([Fase 1, Tabela 12](../fase-1.md#62-o-que-fica-fora-do-escopo)), por isso essa etapa
não conta no tempo nem no resultado. Pausar a gravação durante o login e, se possível,
também o compartilhamento. A pessoa digita a senha na página do Google; a equipe não
pede, não vê nem registra a senha. Retomar a gravação quando a primeira tela do Sua
Grade UnB depois do login aparecer; o cronômetro de M6 começa nesse instante. Não abrir
a página de grades salvas antes de M6: a ausência de grades na conta vem da triagem
(sem uso prévio) e é conferida no passo 5. Quem não quiser entrar com a conta Google
não faz a coleta formal; chamar o suplente.

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

1. Confirmar ausência de uso prévio, login concluído e S0; iniciar cronômetro ao abrir a interface.
2. Ler: “Você tem até três minutos para conhecer livremente a aplicação. Depois receberá uma tarefa.”
3. Ao terminar a exploração, entregar: “Monte uma grade com as disciplinas [nome/código A] e [nome/código B], usando as turmas [A1] e [B1]. Gere uma opção compatível, salve-a na sua conta e deixe-a disponível para consultar novamente.”
4. Observar até concluir ou atingir T. Registrar desistência, ajuda, erros e expiração.
5. Dentro de T, verificar seleção, horários, geração e salvamento. Solicitar “Mostre a grade que ficou salva para consultar novamente”. Conferir, após recarregar, que a grade aparece como salva na conta, e não só no navegador, e que é a única grade salva; registrar quem recarregou e a evidência.
6. Sucesso exige todos os resultados corretos, independência e recuperação dentro de T. Não basta mensagem de sucesso nem exportação PDF.

Uma linha M6 por sessão. `S6/N6`: incluir insucessos e expirações entre sessões
válidas iniciadas. Separar por dispositivo; mínimo operacional 80%.

## 4. M7 — Controle da grade

Limite de 3 minutos para cada tarefa; iniciar na entrega do cartão, com o estado
inicial conferido. Usar nomes reais e solicitar apenas o resultado, sem indicar
botão ou caminho.

| ID | Estado inicial | Texto do cartão | Resultado esperado |
|---|---|---|---|
| M7-SEL | S0 | “Inclua [A1] de [A] e [B1] de [B] nas suas escolhas.” | Somente A1+B1 selecionadas (S1) |
| M7-ALT | S1 | “Troque a turma [A1] pela [A2], mantendo [B1].” | A2+B1 selecionadas (S2), A1 ausente |
| M7-REM | S2 | “Deixe nas suas escolhas apenas [B1] de [B].” | A2 removida, B1 preservada |

Aplicar as tarefas nessa ordem: o estado final de cada uma é o inicial da seguinte,
já que no aparelho do participante não há backup para restaurar estados. Antes de
M7-SEL, pedir que a pessoa recarregue a página e conferir S0. Se uma tarefa terminar
em estado diferente do esperado, registrar o resultado e, antes de entregar o cartão
seguinte, ditar os passos até o estado inicial dele. Registrar essa preparação no
contexto da tarefa seguinte; ela não conta como ajuda nessa tarefa, mas mostra o caminho
e deve ser considerada na análise.

Capturar antes/depois, conferir o estado final e registrar correções e ajuda.
Uma linha por tarefa; calcular S7/N7 por tarefa/dispositivo, mínimo 90%. Bloqueio
reproduzível de controle que impeça executar a tarefa determina nota 0 nesse cenário,
conforme Fase 2. Uso prévio adquirido em M6 deve constar no contexto; estas tarefas
posteriores não serão apresentadas como observações independentes de primeiro uso.

## 5. M8 e M9

Aplicar os [instrumentos](instrumentos.md). Em M9 usar até 60 segundos por ponto,
com as duas perguntas, registrando a resposta antes de dar retorno. A ordem é
seleção → geração em andamento → geração concluída → salvamento. M9 parte do fim de
M7 (só B1 selecionada): pedir o resultado de cada etapa, sem indicar o caminho, para
chegar a A2+B1 selecionadas (V01), gerar (V02 e V03) e salvar na conta uma opção
gerada (V04). Usar A2+B1, e não A1+B1, porque o site não cria um registro novo ao
salvar de novo uma grade igual à de M6. Se M7 terminar em outro estado, ditar os passos
até B1 antes de V01 e registrar como preparação. Registrar que
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
Registrar fim da sessão, problemas e localização restrita das evidências. Oferecer à
pessoa excluir a grade salva na conta durante a sessão: a equipe não tem acesso ao banco
do site e não consegue apagá-la depois. Agradecer e lembrar o contato de retirada dos dados.