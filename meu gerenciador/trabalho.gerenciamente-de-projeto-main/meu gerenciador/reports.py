# reports.py
from services import listar_projetos, listar_tarefas, listar_tarefas_por_projeto, get_id_entity
from utils import diferenca_datas, data_atual

def get_projeto_resumo(project_id):
    projeto = next((p for p in listar_projetos() if p['id'] == project_id), None)
    if not projeto:
        return None
    tarefas = listar_tarefas_por_projeto(project_id)
    total_tarefas = len(tarefas)
    status_contador = {"pendente": 0, "em andamento": 0, "concluida": 0}
    concluidas = 0
    for task in tarefas:
        status = task.get('status', 'pendente')
        if status not in status_contador:
            status_contador[status] = status_contador.get(status, 0) + 1
        else:
            status_contador[status] += 1
        if status == 'concluida':
            concluidas += 1
    percentual_concluidas = (concluidas / total_tarefas) * 100 if total_tarefas > 0 else 0.0
    resumo = {
        "projeto": projeto['nome'],
        "total_tarefas": total_tarefas,
        "status": status_contador,
        "percentual_concluidas": round(percentual_concluidas, 2)
    }
    return resumo

def get_tarefas_atrasadas():
    tarefas = listar_tarefas()
    atual_data = data_atual()
    tarefas_atrasadas = []
    for task in tarefas:
        if task.get('status') != 'concluida':
            prazo = task.get('prazo')
            if prazo and diferenca_datas(prazo, atual_data) < 0:
                projeto = next((p for p in listar_projetos() if p['id'] == task['projeto_id']), {'nome': 'N/A'})
                responsavel = get_id_entity('usuarios', task.get('responsavel_id')) or {'nome': 'N/A'}
                tarefas_atrasadas.append({
                    "id": task.get('id'),
                    "titulo": task.get('titulo'),
                    "projeto": projeto.get('nome', 'N/A'),
                    "responsavel": responsavel.get('nome', 'N/A'),
                    "prazo": prazo,
                    "status": task.get('status')
                })
    resumo = {
        "total_atrasadas": len(tarefas_atrasadas),
        "detalhes": tarefas_atrasadas
    }
    return resumo
