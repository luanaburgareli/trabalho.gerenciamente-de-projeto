from services import listar_projetos, listar_tarefas, listar_tarefas_por_projeto, buscar_projeto, get_id_entity
from utils import diferenca_datas, data_atual

def get_projeto_resumo(project_id):
    projeto = next((p for p in listar_projetos() if p['id'] == project_id), None)
    if not projeto:
        return None

    tarefas = listar_tarefas_por_projeto(project_id)
    total_tarefas = len(tarefas)
    
    if total_tarefas == 0:
        return {
            "projeto": projeto['nome'],
            "total_tarefas": 0,
            "status": {"pendente": 0, "andamento": 0, "concluída": 0},
            "percentual_concluidas": 0.0
        }, "Resumo gerado com sucesso."

    status_contador = {"pendente": 0, "andamento": 0, "concluída": 0}
    concluidas = 0
    
    for task in tarefas:
        status = task.get('status', 'pendente')
        status_contador[status] = status_contador.get(status, 0) + 1
        if status == 'concluída':
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
        if task.get('status') != 'concluída':
            prazo = task.get('prazo')
            #se o bgl tiver negativo é pq ta atrasado
            if prazo and diferenca_datas(prazo, atual_data) < 0:
                projeto = next((p for p in listar_projetos() if p['id'] == task['projeto_id']), {'nome': 'N/A'})
                responsavel = get_id_entity('usuarios', task['responsavel_id']) if task.get('responsavel_id') else {'nome': 'N/A'}

                tarefas_atrasadas.append({
                    "id": task['id'],
                    "titulo": task['titulo'],
                    "projeto": projeto['nome'],
                    "responsavel": responsavel['nome'],
                    "prazo": prazo,
                    "status": task['status']
                })

    resumo = {
        "total_atrasadas": len(tarefas_atrasadas),
        "detalhes": tarefas_atrasadas
    }
    return resumo
