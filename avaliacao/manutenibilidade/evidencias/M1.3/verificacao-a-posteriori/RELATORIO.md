# Verificação a posteriori dos patches de C1 e C2

Data: 15/11/2026. Feita pela equipe com apoio de Claude (IA), a partir dos patches entregues no commit `18bd323` (12/11/2026, Joaquim) e já presentes na `main`.

**Esta verificação não é a coleta formal de M1.3.** Ela não mede tempo e não substitui a execução cronometrada por um executor elegível. Serve apenas para saber se os patches, aplicados sobre o commit inicial do produto, passam na suíte da API.

## Método

1. Cópia limpa do produto no commit `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`, três vezes: `base` (sem alteração), `c1` e `c2`.
2. `git apply` de `C1/C1.patch` e `C2/C2.patch` nas respectivas cópias (`--check` antes). Os dois patches aplicaram sem conflito.
3. Suíte completa da API: `python manage.py test --noinput`, no diretório `api/`, com PostgreSQL e Redis locais.
4. Cada cópia foi executada ao menos duas vezes, e as três também foram executadas com o Redis limpo.

Ambiente: Linux x86_64, Python 3.11 com as dependências de `api/requirements.txt` e `setuptools` 68.2.2, PostgreSQL 16.15 e Redis local. **Não foi usado Docker**, diferentemente da coleta formal de M1.4. Os resultados da base (108 testes) coincidem com os da coleta formal.

## Resultados

| Cópia | Testes | Resultado | Falhas |
|-------|--------|-----------|--------|
| base (commit inicial) | 108 | OK | 0 |
| C1 aplicado | 110 | OK | 0 |
| C2 aplicado | 114 | **FALHA** | 9 |

### C1

Os dois testes novos passam e a suíte completa fica aprovada (110 testes, em duas execuções e com Redis limpo).

### C2

A suíte completa falha em todas as execuções (quatro, incluindo com Redis limpo), com 9 falhas:

- **8 falhas nos testes novos** (`test_with_invalid_preference` e `test_with_invalid_preference_length`, em `utils/tests/test_schedule_generator.py`). Os testes usam `assertRaisesRegex(ValueError, PREFERENCE_RANGE_ERROR)` e a mensagem contém `[1, 3]`, que como expressão regular é uma classe de caracteres. O padrão não casa com o texto literal da exceção, embora a exceção correta seja lançada.
- **1 falha em teste existente**: `api.tests.test_search_api.TestSearchAPI.test_with_incomplete_correct_search` (`VINICIUS CARVALHO RISPOLI` em vez de `VINICIUS RISPOLI`). Esse teste passa isolado (14 testes OK) e passa na base, e só falha na suíte completa com o patch de C2. A causa não foi investigada.

Pelo critério de conclusão (testes novos e suíte completa aprovados), **C2, como entregue, não está concluída**.

## Limites

- Não há evidência de tempo, de quem executou, do método de medição nem de uso de IA. O tempo informado verbalmente continua sem registro.
- O log de C2 que está na `main` (`C2/testes-django.log`) é um erro de ambiente (`ModuleNotFoundError: decouple`, caminho `/mnt/data/...`) e não mostra a suíte rodando.
- Esta verificação foi feita fora do Docker do projeto. Uma repetição com Docker é recomendável antes de citar o resultado de C2 como definitivo.

Arquivos: `base-suite.log`, `c1-suite.log`, `c2-suite.log`.
