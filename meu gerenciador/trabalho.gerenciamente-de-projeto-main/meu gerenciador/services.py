from storage import carregar_dados, salvar_dados
from models import validar_usuario, validar_projeto, validar_tarefa, criar_usuario, criar_projeto, criar_tarefa

def get_indice_entity(entity_name, entity_id):
    data = carregar_dados(entity_name)
    for i, entity in enumerate(data):
        if entity.get('id') == entity_id:
            return i
    return -1

def get_id_entity(entity_name, entity_id):
    data = carregar_dados(entity_name)
    for entity in data:
        if entity.get('id') == entity_id:
            return entity
    return None

def cadastrar_usuario(nome, email):
    return criar_usuario(nome, email)

def listar_usuarios():
    return carregar_dados('usuarios')

def buscar_usuario(termo):
    usuarios = carregar_dados('usuarios')
    termo = termo.lower()
    resultados = []
    for usuario in usuarios:
        if termo in usuario.get('nome', '').lower() or termo in usuario.get('email', '').lower():
            resultados.append(usuario)
    if resultados:
        return resultados
    return []

def atualizar_usuario(user_id, nome=None, email=None):
    usuarios = carregar_dados('usuarios')
    indice = get_indice_entity('usuarios', user_id)
    if indice == -1:
        return False
    
    user = usuarios[indice]
    
    if nome is not None: user['nome'] = nome
    if email is not None: user['email'] = email
    
    if validar_usuario(user):
        usuarios[indice] = user
        salvar_dados('usuarios', usuarios)
        return True
    return False

def remover_usuario(user_id):
    usuarios = carregar_dados('usuarios')
    indice = get_indice_entity('usuarios', user_id)
    if indice == -1:
        return False
    
    tarefas = listar_tarefas()
    if any(tarefa.get('responsavel_id') == user_id for tarefa in tarefas):
        return False
    
    del usuarios[indice]
    salvar_dados('usuarios', usuarios)
    return True


def cadastrar_projeto(nome, descricao, data_inicio, data_fim=None):
    return criar_projeto(nome, descricao, data_inicio, data_fim)

def listar_projetos():
    return carregar_dados('projetos')

def buscar_projeto(termo):
    projetos = carregar_dados('projetos')
    termo = termo.lower()
    resultados = []
    for projeto in projetos:
        if termo in projeto.get('nome', '').lower():
            resultados.append(projeto)
    if resultados:
        return resultados
    return []
    
def atualizar_projeto(projeto_id, nome=None, descricao=None, data_inicio=None, data_fim=None):
    projetos = carregar_dados('projetos')
    indice = get_indice_entity('projetos', projeto_id)
    if indice == -1:
        return False
    
    projeto = projetos[indice]
    
    if nome is not None: projeto['nome'] = nome
    if descricao is not None: projeto['descricao'] = descricao
    if data_inicio is not None: projeto['data_inicio'] = data_inicio
    if data_fim is not None: projeto['data_fim'] = data_fim

    if validar_projeto(projeto):
        projetos[indice] = projeto
        salvar_dados('projetos', projetos)
        return True
    return False

def remover_projeto(projeto_id):
    projetos = carregar_dados('projetos')
    indice = get_indice_entity('projetos', projeto_id)
    if indice == -1:
        return False

    del projetos[indice]
    salvar_dados('projetos', projetos)
    return True


def cadastrar_tarefa(titulo, projeto_id, responsavel_id, prazo, status='pendente'):
    return criar_tarefa(titulo, projeto_id, responsavel_id, prazo, status)

def listar_tarefas():
    return carregar_dados('tarefas')

def listar_tarefas_por_projeto(projeto_id):
    tarefas = listar_tarefas()
    return [tarefa for tarefa in tarefas if tarefa.get('projeto_id') == projeto_id]

def listar_tarefas_por_responsavel(responsavel_id):
    tarefas = listar_tarefas()
    return [tarefa for tarefa in tarefas if tarefa.get('responsavel_id') == responsavel_id]

def listar_tarefas_por_status(status):
    tarefas = listar_tarefas()
    return [tarefa for tarefa in tarefas if tarefa.get('status') == status]

def atualizar_tarefa(tarefa_id, titulo=None, responsavel_id=None, prazo=None, status=None):
    tarefas = listar_tarefas()
    index = get_indice_entity('tarefas', tarefa_id)
    if index == -1:
        return False

    tarefa = tarefas[index].copy()
    
    if titulo is not None: tarefa['titulo'] = titulo
    if responsavel_id is not None: tarefa['responsavel_id'] = responsavel_id
    if prazo is not None: tarefa['prazo'] = prazo
    if status is not None: tarefa['status'] = status

    is_valid, message = validar_tarefa(tarefa, is_new=False)
    if not is_valid:
        return False, message

    tarefas[index] = tarefa
    salvar_dados('tarefas', tarefas)
    return True

def completar_tarefa(tarefa_id):
    return atualizar_tarefa(tarefa_id, status='concluída')

def reabrir_tarefa(tarefa_id):
    return atualizar_tarefa(tarefa_id, status='andamento')

def remover_tarefa(tarefa_id):
    tarefas = listar_tarefas()
    index = get_indice_entity('tarefas', tarefa_id)
    if index == -1:
        return False

    del tarefas[index]
    salvar_dados('tarefas', tarefas)
    return True
