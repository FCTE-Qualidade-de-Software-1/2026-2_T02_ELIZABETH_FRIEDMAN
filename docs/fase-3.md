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

| Métrica ([Fase 2](fase-2.md#3-metricas-nivel-quantitativo)) | Método / técnica | Ferramenta | Instruções |
|---------------------------------------------------------------|------------------|------------|------------|
| M1.1–M1.4 | Preparação em issue própria (#38) | A definir nessa entrega | Pendente |
| M2–M5 | Preparação em issue própria (#39) | A definir nessa entrega | Pendente |
| M6 — Primeiro uso | Teste observado com estudantes sem uso prévio; mede conclusão independente do fluxo | Navegador, cronômetro, massa fixa, CSV e evidência de recuperação | [Protocolo, §3](avaliacao-interacao/protocolo.md#3-m6-primeiro-uso) |
| M7 — Controle da grade | Tarefas observadas de seleção, remoção e alteração; conferência do estado final | Computador/celular reais, estados restauráveis, CSV e capturas | [Protocolo, §4](avaliacao-interacao/protocolo.md#4-m7-controle-da-grade) |
| M8 — Proteção contra perda | Inspeção por cenários de risco, executada pelo avaliador | Grades descartáveis, inventário, CSV e capturas antes/depois | [Instrumentos M8/M9](avaliacao-interacao/instrumentos.md) |
| M9 — Compreensão | Perguntas neutras sobre estado e próxima ação, classificadas por gabarito | Estados reais, captura no instante da pergunta e CSV | [Instrumentos M8/M9](avaliacao-interacao/instrumentos.md) |

O protocolo observado permite conferir comportamento e respostas de estudantes; a
inspeção de M8 permite provocar perdas com dados descartáveis sem expor participantes.
Automação pode preparar estados e capturas, mas não substitui respostas humanas.
As fórmulas e os critérios de julgamento continuam sendo os da [Fase 2, §3.3](fase-2.md#33-metricas-de-capacidade-de-interacao-g3).
Este documento cobre F3-C8 para M6–M9; as demais métricas dependem de suas próprias entregas.

## 2. Recursos e ambiente de avaliação

<!--
F3-C2: hardware e software necessários, massa de dados (dados-exemplo) quando pertinente,
perfil exigido dos avaliadores/usuários (conhecimento em informática e no domínio).
-->

Para M6–M9, usar a versão `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`
do Sua Grade UnB em ambiente local isolado, com massa fixa, conta de teste quando
necessária e acesso por computador e celular físicos. Registrar sistema operacional,
navegador/versão, dimensões e URL efetiva no manifesto da sessão. As sessões serão online por Google Meet. Validar acesso remoto privado ao ambiente
nos dispositivos dos participantes antes do piloto; `localhost` no celular aponta
para o próprio celular. O compartilhamento de tela também deve ser validado.

O avaliador deve saber restaurar o estado, conferir disciplinas/turmas e preservar
registros sem orientar o caminho. Participantes: estudantes adultos sem uso prévio,
com conhecimento básico de navegador e do conceito de disciplina/turma. Planejam-se
dois estudantes no computador e dois no celular, com um suplente por grupo;
uma pessoa adicional participa apenas do piloto. A redução de dez para quatro
participantes foi definida antes da coleta em 08/11/2026 para viabilizar a execução
pela dupla, com menor cobertura e sem alterar os limiares de julgamento da Fase 2.
Trata-se de amostra exploratória
por conveniência, sem pretensão de representatividade estatística.

Recursos, instruções, tempos e pendências estão no [protocolo](avaliacao-interacao/protocolo.md).
O [consentimento](avaliacao-interacao/consentimento.md), o [recrutamento](avaliacao-interacao/recrutamento.md)
e os [modelos CSV](avaliacao-interacao/registros.md) fazem parte do instrumento.
O [procedimento de proteção dos dados](avaliacao-interacao/dados.md) orienta a equipe
sobre o preenchimento do termo e o tratamento das autorizações e registros.
A massa real, acesso às modalidades de salvamento e ambiente operacional ainda
precisam ser confirmados junto à preparação do ambiente (#37). Preparação documental
não constitui coleta validada.

## 3. Cronograma da avaliação

<!--
F3-C3: cronograma realista com atividades distribuídas e alinhadas à execução da Fase 4.
-->

| Atividade | Responsável | Início | Fim | Métricas envolvidas |
|-----------|-------------|--------|-----|---------------------|
| Confirmar ambiente, massa e responsáveis; iniciar triagem | Lucas e Kaleb | 03/11/2026 | 04/11/2026 | M6–M9 |
| Preparar roteiro, consentimento, CSV e instrumentos | Equipe | 03/11/2026 | 05/11/2026 | M6–M9 |
| Executar piloto e verificar recursos nos dois dispositivos | Lucas (moderador) e Kaleb (observador) | 06/11/2026 | 06/11/2026 | M6–M9 |
| Corrigir instrumentos, repetir trechos afetados e congelar protocolo | Equipe | 06/11/2026 | 07/11/2026 | M6–M9 |
| Coleta formal e análise na Fase 4 | Equipe | Após liberação do piloto | Agendar antes da coleta | M6–M9 |

### Situação da issue #40

Materiais preparados em 03/11/2026 e revisados em 08/11/2026, protocolo 0.2, **aguardando validação humana**.
O [registro de piloto e fechamento](avaliacao-interacao/piloto.md) mantém os critérios
de liberação e as pendências. Não encerrar a issue antes de confirmar recrutamento,
inventário no ambiente real e piloto com pessoa fora da amostra.

---

Anterior: [Fase 2](fase-2.md) · Próxima: [Fase 4 — Execução e resultados](fase-4.md).
