# Modelo para preencher a análise de G3

Este arquivo é um modelo de trabalho, não faz parte da documentação publicada. Os trechos
entre colchetes devem ser substituídos com os resultados reais. Os valores vêm do
`resumo-g3.md` e do `resultados-g3.csv` gerados por `analisar_g3.py`.

---

## Trecho 1: linhas para a tabela da seção 1 de `docs/fase-4.md`

Acrescentar abaixo da linha de M1.4. As colunas são as mesmas da tabela existente.

| Métrica | Data da coleta | Responsável | Dados brutos | Procedimento de cálculo |
|---------|----------------|-------------|--------------|-------------------------|
| M6 — Sucesso no primeiro uso | [datas das sessões] | Júlia (moderação) e João (observação) | [Observações anonimizadas](avaliacao/dados/g3/observacoes-anonimizado.csv). As fichas, as gravações e os termos originais ficam em pasta restrita, fora do Git. | [Protocolo v0.3](avaliacao-interacao/protocolo.md), seção 3, e [`analisar_g3.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/interacao/analisar_g3.py) |
| M7 — Sucesso nas tarefas de controle | [datas das sessões] | Júlia e João | Mesmo arquivo de M6 | Protocolo v0.3, seção 4, e `analisar_g3.py` |
| M8 — Proteção contra perda | [data da inspeção] | [nome do avaliador] | [Inventário de M8 preenchido](avaliacao/dados/g3/inventario-m8-preenchido.csv) e observações | Protocolo v0.3, seção 5, e `analisar_g3.py` |
| M9 — Compreensão da interface | [datas das sessões] | Júlia e João | Mesmo arquivo de M6 | Protocolo v0.3, seção 5, e `analisar_g3.py` |

---

## Trecho 2: seção 2.2 de `docs/fase-4.md`

Colar depois da seção 2.1 (G1).

### 2.2 G3 — Capacidade de interação

As sessões foram feitas no site público do Sua Grade UnB, com a conta Google de cada
participante, entre [data] e [data], conforme o [protocolo v0.3](avaliacao-interacao/protocolo.md).
Em cada dia, a equipe conferiu o último commit e o último *deployment* do produto
([registrar]). Participaram [N] pessoas com sessão válida: [x] em computador e [y] em
celular. M8 não envolve participantes: foi uma inspeção feita pelo avaliador, com a
conta de um integrante da equipe e grades descartáveis. Os valores não foram arredondados
antes da comparação com as faixas, e as notas não foram combinadas em média.

**Tabela 2 — Resultados de G3 por métrica e recorte**

[colar aqui a tabela do `resumo-g3.md`]

**Q6 — Aprendizagem (H6).** [Dizer, para cada dispositivo e modalidade, quantos
participantes concluíram a tarefa de M6 em até 15 minutos e sem ajuda (sucessos/válidas,
percentual e nota). Concluir se H6 tem sustentação operacional, é contrariada ou é
inconclusiva.]

**Q7 — Operabilidade (H7).** [Para cada tarefa (M7-SEL, M7-ALT, M7-REM) e dispositivo, informar
sucessos/válidas, percentual e nota. Citar qualquer bloqueio reproduzível de controle,
que determina nota 0 naquele cenário. Concluir sobre H7.]

**Q8 — Proteção contra erros do usuário (H8).** [Para cada dispositivo e modalidade,
informar quantos cenários de risco (R01 a R06) tinham proteção efetiva. M8 só atinge a
nota 3 com 100%. Citar os cenários sem proteção. Concluir sobre H8.]

**Q9 — Autodescrição (H9).** [Para cada ponto (V01 a V04) e dispositivo, informar
sucessos/válidas, percentual e nota. Registrar se V02 (geração em andamento) pôde ser
observado. Concluir sobre H9.]

**G3 — Resumo.** G3 não recebe nota única. [Resumir em uma frase o estado de H6, H7, H8 e H9
e a cobertura planejada em relação à realizada.]

**Limitações.**
- A amostra é pequena, com poucas pessoas por dispositivo, então os percentuais variam de
  forma grosseira (por exemplo, 50% ou 100% em M6) e não permitem inferência estatística.
- O site público é mantido por terceiros, e os dados do período podem ter mudado entre
  os dias de sessão.
- M7 e M9 foram aplicados depois de M6, quando a pessoa já havia usado a interface. Não são
  observações independentes de primeiro uso.
- [Informar se o piloto foi realizado e o que isso implica para a validação dos instrumentos.]
- [Informar sessões inválidas ou não coletadas e os motivos.]
- Gravações e fichas originais não são publicadas, para proteger os participantes.