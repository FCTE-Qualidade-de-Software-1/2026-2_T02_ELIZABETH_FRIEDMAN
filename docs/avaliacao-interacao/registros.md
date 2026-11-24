# Fichas e convenções de registro

!!! info "Os arquivos desta página são modelos vazios"
    Os registros preenchidos da coleta, anonimizados, estão em
    [sessões M6, M7 e M9](../avaliacao/dados/g3/m6-m9-sessoes.csv),
    [inventário M8](../avaliacao/dados/g3/m8-inventario.csv),
    [observações M8](../avaliacao/dados/g3/m8-observacoes.csv) e
    [resultados por recorte](../avaliacao/dados/g3/m6-m9-resultados.csv).
    A análise está na [Fase 4, seção 2.3](../fase-4.md#23-g3-capacidade-de-interacao).

Baixar os modelos vazios e salvar cópias preenchidas fora da documentação pública:

- [Observações M6–M9](observacoes.csv): uma linha por sessão M6, tarefa M7, cenário M8 ou ponto M9.
- [Inventário M8](inventario-m8.csv): candidatos preliminares; completar e desdobrar por dispositivo/modalidade antes de congelar.
- [Recrutamento](recrutamento.csv): cabeçalho vazio, para uso restrito.

Arquivos em UTF-8, delimitador vírgula, cabeçalho fixo. Aspas duplas em textos que
contenham vírgulas/quebras; aspas internas duplicadas. Horários ISO 8601 com fuso
(`2026-11-06T14:00:00-03:00`); durações em segundos, decimais com ponto. Célula vazia
significa não aplicável/ainda não registrado, nunca zero. Não preencher linhas de
exemplo como se fossem coleta real.

| Campo ou grupo | Convenção |
|---|---|
| `sessao_id`, `protocolo_versao`, `fase_coleta` | Identificador único; versão; `piloto` ou `formal` |
| `metrica`, `participante_codigo` | `M6`…`M9`; código pseudonimizado; vazio para inspeção M8 |
| `experiencia_previa`, `ordem` | `sem_uso_previo`, `apos_M6`, `apos_M7` ou `na`; registrar ordem das tarefas |
| `dispositivo`, `modalidade` | `computador`/`celular`; `navegador`/`conta`/`na`. M6 e M9 usam `conta`; em M8, `navegador` indica grade não salva na conta |
| Ambiente | Modelo, SO, navegador e versão, viewport; em `versao_sistema`, o commit e o último *deployment* conferidos no dia; em `massa_id`, o período e a referência da captura datada de A e B |
| Cenário e resultados | IDs do roteiro, estado inicial, resultado esperado e resultado observado concretos |
| Tempos | `inicio`, `fim`, `duracao_s`; M6 também `exploracao_inicio`, `exploracao_fim`, `execucao_inicio`, `execucao_fim` |
| Ajuda | `nenhuma`, `solicitada_sem_orientacao`, `orientacao_fornecida`; detalhar instante, conteúdo e motivo em `ajuda_detalhe` |
| `estado_observacao` | `valida`, `invalida`, `nao_coletada` |
| `resultado` | `sucesso`, `insucesso`; vazio para inválida/não coletada |
| `motivo` | Expiração, desistência por dificuldade, defeito, falha de equipamento/roteiro ou outro fato, sem dados pessoais |
| `evidencia_antes`, `evidencia_depois` | Referências relativas às cópias restritas; substituir por cópias revisadas somente para publicação |
| M9 | Perguntas, respostas literais, `estado_correto` e `acao_correta` como `sim`/`nao`; sucesso exige ambos sim |
| M8 | `mecanismo_protecao`: `prevencao`, `confirmacao`, `recuperacao` ou `nenhum`; `conteudo_perdido` |

No inventário, `a_validar` não é cenário aprovado nem observação válida. Cenário
`ausente` precisa de verificação e justificativa; `sem_acesso` reduz cobertura. No
recrutamento, registrar apenas autorizações efetivamente obtidas: `sim`/`nao`.

Conferência ao terminar cada sessão: todos os IDs e resultados preenchidos, tempos
coerentes, evidências acessíveis e consentimento compatível com o registro produzido.
Piloto fica em arquivo separado e nunca entra nos denominadores formais. Para análise,
contar apenas `valida` de `formal`, preservando insucessos. Relatar inválidas e não
coletadas separadamente; comparar cobertura com o inventário e agenda congelados.
