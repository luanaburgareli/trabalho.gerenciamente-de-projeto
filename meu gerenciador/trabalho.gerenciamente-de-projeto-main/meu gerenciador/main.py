import sys
from storage import iniciar_dados
from services import *
from reports import *
from ui import *

def menu_usuarios():
    menu_options = {
        '1': 'Cadastrar Usuário',
        '2': 'Listar Todos',
        '3': 'Buscar por Nome/E-mail',
        '4': 'Atualizar Usuário',
        '5': 'Remover Usuário'
    }
    while True:
        escolha = display_menu("Gerenciamento de Usuários", menu_options)
        if escolha == '0': return

        if escolha == '1':
            nome = str(input("Nome: "))
            email = str(input("E-mail: "))
            perfil = str(input("Perfil (usuario/admin): "))

            if not nome or not email or not perfil:
                print("Todos os campos são obrigatórios.")
                continue
            if perfil not in ['usuario', 'admin']:
                print("Perfil inválido. Use 'usuario' ou 'admin'.")
                continue

            cadastrar_usuario(nome, email, perfil)
            print("Usuário cadastrado com sucesso.")

        elif escolha == '2':
            display_entity_lista(listar_usuarios(), "Usuários")

        elif escolha == '3':
            termo = str(input("Digite o nome ou e-mail: "))
            encontrados = buscar_usuario(termo)
            display_entity_lista(encontrados, "Usuários Encontrados")

        elif escolha == '4':
            user_id = str(input("ID do usuário para atualizar: "))
            user = get_id_entity('usuarios', user_id)
            if not user:
                print("Usuário não encontrado.")
                continue
            print(f"Atualizando Usuário: {user['nome']} ({user['id']}). Deixe em branco para manter o valor atual.")
            
            nome = str(input(f"Novo Nome [{user['nome']}]: "))
            email = str(input(f"Novo E-mail [{user['email']}]: "))
            perfil = str(input(f"Novo Perfil [{user['perfil']}]: "))
            
            if not nome : nome = user['nome']
            if not email : email = user['email']
            if not perfil : perfil = user['perfil']

            atualizar_usuario(user_id, nome, email, perfil)
            print(f"Atualização concluída.")

        elif escolha == '5':
            user_id = str(input("ID do usuário para remover: "))
            remover_usuario(user_id)
            print(f"Usuário removido com sucesso.")

def menu_projetos():
    menu_options = {
        '1': 'Cadastrar Projeto',
        '2': 'Listar Todos',
        '3': 'Buscar por Nome',
        '4': 'Atualizar Projeto',
        '5': 'Remover Projeto'
    }

    while True:
        escolha = display_menu("Gerenciamento de Projetos", menu_options)
        if escolha == '0': return

        if escolha == '1':
            nome = str(input("Nome: "))
            descricao = str(input("Descrição: "))
            data_inicio = str(input("Data de Início (YYYY-MM-DD): "))
            data_fim = str(input("Data de Fim (YYYY-MM-DD) [opcional]: "))

            if not nome or not descricao or not data_inicio:
                print("Campos obrigatórios não podem estar vazios.")
                continue

            cadastrar_projeto(nome, descricao, data_inicio, data_fim)
            print("Projeto cadastrado com sucesso.")

        elif escolha == '2':
            display_entity_lista(listar_projetos(), "Projetos")

        elif escolha == '3':
            termo = str(input("Digite o nome do projeto: "))
            encontrados = buscar_projeto(termo)
            display_entity_lista(encontrados, "Projetos Encontrados")

        elif escolha == '4':
            projeto_id = str(input("ID do projeto para atualizar: "))
            projeto = get_id_entity('projetos', projeto_id)
            if not projeto:
                print("Projeto não encontrado.")
                continue
            print(f"Atualizando Projeto: {projeto['nome']} ({projeto['id']}). Deixe em branco para manter o valor atual.")

            nome = str(input(f"Novo Nome [{projeto['nome']}]: "))
            descricao = str(input(f"Nova Descrição [{projeto['descricao']}]: "))
            data_inicio = str(input(f"Nova Data de Início [{projeto['data_inicio']}]: "))
            data_fim = str(input(f"Nova Data de Fim [{projeto['data_fim']}]: "))

            if not nome: nome = projeto['nome']
            if not descricao: descricao = projeto['descricao']
            if not data_inicio: data_inicio = projeto['data_inicio']
            if not data_fim: data_fim = projeto['data_fim']

            atualizar_projeto(projeto_id, nome, descricao, data_inicio, data_fim)
            print(f"Atualização concluída.")

        elif escolha == '5':
            projeto_id = str(input("ID do projeto para remover: "))
            remover_projeto(projeto_id)
            print(f"Projeto removido com sucesso.")


def menu_tarefas():
    menu_options = {
        '1': 'Cadastrar Tarefa',
        '2': 'Listar Todas',
        '3': 'Listar por Projeto',
        '4': 'Listar por Responsável',
        '5': 'Listar por Status',
        '6': 'Atualizar Tarefa',
        '7': 'Concluir Tarefa',
        '8': 'Reabrir Tarefa',
        '9': 'Remover Tarefa'
    }
    
    while True:
        escolha = display_menu("Gerenciamento de Tarefas", menu_options)
        if escolha == '0': return
        
        if escolha == '1':
            titulo = str(input("Título: "))
            projeto_id = str(input("ID do Projeto: "))
            responsavel_id = str(input("ID do Responsável: "))
            prazo = str(input("Prazo (YYYY-MM-DD): "))
            status = str(input("Status (pendente/em andamento/concluida): "))
            if not status:
                status = 'pendente'

            if not titulo or not projeto_id or not responsavel_id:
                print("Campos obrigatórios não podem estar vazios.")
                continue

            cadastrar_tarefa(titulo, projeto_id, responsavel_id, prazo, status)
            print("Tarefa cadastrada com sucesso.")

        elif escolha == '2':
            display_entity_lista(listar_tarefas(), "Tarefas")

        elif escolha == '3':
            projeto_id = str(input("ID do Projeto: "))
            encontrados = listar_tarefas_por_projeto(projeto_id)
            display_entity_lista(encontrados, "Tarefas")

        elif escolha == '4':
            responsavel_id = str(input("ID do Responsável: "))
            encontrados = listar_tarefas_por_responsavel(responsavel_id)
            display_entity_lista(encontrados, "Tarefas")

        elif escolha == '5':
            status = str(input("Status (pendente/em andamento/concluida): "))
            encontrados = listar_tarefas_por_status(status)
            display_entity_lista(encontrados, "Tarefas")

        elif escolha == '6':
            tarefa_id = str(input("ID da tarefa para atualizar: "))
            tarefa = get_id_entity('tarefas', tarefa_id)
            if not tarefa:
                print("Tarefa não encontrada.")
                continue
            print(f"Atualizando Tarefa: {tarefa['titulo']} ({tarefa['id']}). Deixe em branco para manter o valor atual.")

            titulo = str(input(f"Novo Título [{tarefa['titulo']}]: "))
            projeto_id = str(input(f"Novo Projeto ID [{tarefa['projeto_id']}]: "))
            responsavel_id = str(input(f"Novo Responsável ID [{tarefa['responsavel_id']}]: "))
            prazo = str(input(f"Novo Prazo [{tarefa['prazo']}]: "))
            status = str(input(f"Novo Status [{tarefa['status']}]: "))
            
            if not titulo: titulo = tarefa['titulo']
            if not projeto_id: projeto_id = tarefa['projeto_id']
            if not responsavel_id: responsavel_id = tarefa['responsavel_id']
            if not prazo: prazo = tarefa['prazo']
            if not status: status = tarefa['status']
            
            atualizar_tarefa(tarefa_id, titulo, responsavel_id, prazo, status)
            print(f"Atualização concluída.")
        
        elif escolha == '7':
            tarefa_id = str(input("ID da tarefa para concluir: "))
            completar_tarefa(tarefa_id)
            print("Tarefa marcada como concluída.")
            
        elif escolha == '8':
            tarefa_id = str(input("ID da tarefa para reabrir: "))
            reabrir_tarefa(tarefa_id)
            print("Tarefa reaberta com sucesso.")
            
        elif escolha == '9':
            tarefa_id = str(input("ID da tarefa para remover: "))
            remover_tarefa(tarefa_id)
            print(f"Tarefa removida com sucesso.")
            
def menu_relatorios():
    menu_options = {
        '1': 'Resumo por Projeto',
        '2': 'Tarefas em Atraso'
    }
    while True:
        choice = display_menu("Relatórios", menu_options)
        if choice == '0': return

        if choice == '1':
            project_id = str(input("ID do Projeto: "))
            relatorio_data = get_projeto_resumo(project_id)
            if relatorio_data:
                print(relatorio_data, "Resumo por Projeto")
            else:
                print(f"\nErro: Projeto não encontrado.")

        elif choice == '2':
            relatorio_data = get_tarefas_atrasadas()
            display_relatorio(relatorio_data, "Tarefas em Atraso")

def main():
    iniciar_dados()
    
    main_menu_options = {
        '1': 'Gerenciar Usuários',
        '2': 'Gerenciar Projetos',
        '3': 'Gerenciar Tarefas',
        '4': 'Relatórios',
    }

    print("--- Sistema de Gerenciamento de Projetos ---")
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #(vai q o bgl n é o windonws né)
        choice = display_menu("Menu Principal", main_menu_options)
        
        if choice == '1':
            menu_usuarios()
        elif choice == '2':
            menu_projetos()
        elif choice == '3':
            menu_tarefas()
        elif choice == '4':
            menu_relatorios()
        elif choice == '0':
            print("Saindo do sistema. Dados salvos.")
            sys.exit(0)

if __name__ == '__main__':
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    main()
