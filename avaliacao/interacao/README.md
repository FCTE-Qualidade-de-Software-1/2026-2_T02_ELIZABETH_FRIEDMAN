# Análise de G3 (M6 a M9)

Script que calcula M6 a M9 a partir do `observacoes.csv` preenchido, seguindo a
[Fase 2, seção 4.4](../../docs/fase-2.md#44-regras-de-aplicacao-e-julgamento-de-interacao-m6m9)
e o [protocolo](../../docs/avaliacao-interacao/protocolo.md).

## Como usar

1. Guardar a ficha preenchida **fora do Git**, em `dados-restritos/` (ignorada pelo Git).
2. Ajustar `plano-cobertura.csv` ao que foi realmente planejado e congelado (linhas de M8
   por dispositivo e modalidade, conforme o inventário). Linha sem `planejado` é ignorada.
3. Rodar na raiz do repositório:

```bash
python3 avaliacao/interacao/analisar_g3.py dados-restritos/observacoes.csv \
  --plano avaliacao/interacao/plano-cobertura.csv \
  --saida dados-restritos/saida-g3
```

4. Conferir os **avisos** impressos (campo faltando, M9 com sucesso sem os dois "sim",
   inválida sem motivo) e corrigir a ficha antes de usar o resultado.
5. Colar o `resumo-g3.md` na seção 2.2 de `docs/fase-4.md`. O `resultados-g3.csv` pode ir
   para `docs/avaliacao/dados/g3/` **só depois de revisado** (sem identificadores).

## O que o script faz e o que não faz

- Usa só `fase_coleta=formal`. Piloto nunca entra no denominador.
- Denominador = observações `valida` (insucessos incluídos). `invalida` e `nao_coletada`
  são contadas à parte e precisam de `motivo`.
- Recortes: M6 por dispositivo e modalidade; M7 e M9 por tarefa/ponto e dispositivo;
  M8 por dispositivo e modalidade. Não mistura recortes nem faz média de notas.
- A razão é exata (sem arredondar antes da faixa). M8 é binário (100% ou nota 0).
- Hipótese só aparece como sustentada com cobertura completa conforme o `plano`.
  Sem plano informado, fica inconclusiva.
- **Não detecta** bloqueio reproduzível de controle em M7 (nota 0 no cenário pela regra 4
  da Fase 2): conferir o `motivo` dos insucessos de M7 à mão.
- Não é teste estatístico; com poucas pessoas por recorte, os percentuais são grosseiros.