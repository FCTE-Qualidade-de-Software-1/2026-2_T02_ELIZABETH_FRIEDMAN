"""Confere as combinações dos conjuntos de M4 com o gerador do próprio produto (F3-C8).

Resolve as turmas por código da disciplina e número da turma (os ids mudam a cada carga
do seed_referencia.py) e roda o ScheduleGenerator com preferências 1/1/1, sem limite de
retorno. A API (POST /courses/schedules/generate/) devolve no máximo 5 dessas grades
(MAXIMUM_RETURNED_SCHEDULES em api/api/views/views.py).

Uso (no diretório do produto, com os serviços de pé e a massa carregada):
  docker exec -i django-api python3 manage.py shell < <caminho>/m4_combinacoes.py
"""
from api.models import Class
from utils.schedule_generator import ScheduleGenerator
from utils.sessions import get_current_year_and_period

ano, periodo = get_current_year_and_period()
CONJUNTOS = {
    "m4-a": {"PPGPS2475": ["01"], "PPGPS2939": ["01"]},
    "m4-b": {"PPGPS0156": ["02", "03", "04", "05"], "PPGPS0161": ["01", "02", "03", "04"],
             "PPGPS0163": ["01", "02"], "PPGPS0165": ["01", "02", "03", "05"],
             "PPGPS2475": ["01"], "PPGPS2939": ["01"]},
}
for nome, conjunto in CONJUNTOS.items():
    ids = [Class.objects.get(discipline__code=codigo, _class=turma,
                             discipline__department__year=ano,
                             discipline__department__period=periodo).id
           for codigo, turmas in conjunto.items() for turma in turmas]
    candidatas = 1
    for turmas in conjunto.values():
        candidatas *= len(turmas)
    gerado = ScheduleGenerator(ids, [1, 1, 1]).generate()
    print(f"{nome} ({ano}/{periodo}): {len(conjunto)} disciplinas, {len(ids)} turmas, "
          f"{candidatas} candidatas, {len(gerado['schedules'])} válidas, "
          f"exibidas pela API: {min(len(gerado['schedules']), 5)}; "
          f"mensagem: {gerado['message'].splitlines()[0]}")
