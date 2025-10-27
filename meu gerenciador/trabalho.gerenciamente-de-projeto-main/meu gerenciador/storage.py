import json
import os

data_dir = 'data'

def caminho_arquivo(entity_name):
    return os.path.join(data_dir, f'{entity_name}.json')

def carregar_dados(entity_name):
    caminho = caminho_arquivo(entity_name)
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except (FileNotFoundError or json.JSONDecodeError):
        return []
    
def salvar_dados(entity_name, data):
    caminho = caminho_arquivo(entity_name)
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, esfure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar dados para {entity_name}:{e}")
        
def iniciar_dados():
    entities = ['usuarios','projetos','tarefas']
    for entity in entities:
        caminho = caminho_arquivo(entity)
        if not os.path.exists(caminho):
            salvar_dados(entity, [])
    
