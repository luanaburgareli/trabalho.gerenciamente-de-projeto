# main.py
import sys
from storage import iniciar_dados
from reports import get_projeto_resumo, get_tarefas_atrasadas
from services import (
    cadastrar_usuario, listar_usuarios, buscar_usuario, get_id_entity,
    atualizar_usuario, remover_usuario,
    cadastrar_projeto, listar_projetos, buscar_projeto, atualizar_projeto, remover_projeto,
    cadastrar_tarefa, listar_tarefas, listar_tarefas_por_projeto, listar_tarefas_por_responsavel,
    listar_tarefas_por_status, atualizar_tarefa, completar_tarefa, reabrir_tarefa, remover_tarefa
)
from ui import display_menu, display_entity_lista, display_relatorio
from utils import validar_data, validar_email

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
        if escolha == '0':
            return
        if escolha == '1':
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            perfil = input("Perfil (usuario/admin): ").strip().lower()
            if not nome or not email or not perfil:
                print("Todos os campos são obrigatórios.")
                continue
            if not validar_email(email):
                print("E-mail inválido.")
                continue
            if perfil not in ['usuario', 'admin']:
                print("Perfil inválido.")
                continue
            result = cadastrar_usuario(nome, email, perfil)
            print("Usuário cadastrado com sucesso." if result else "Erro ao cadastrar usuário (email já existe).")
        elif escolha == '2':
            display_entity_lista(listar_usuarios(), "Usuários")
        elif escolha == '3':
            termo = input("Digite o nome ou e-mail: ").strip()
            if not termo:
                print("Digite nome ou e-mail para buscar.")
                continue
            encontrados = buscar_usuario(termo)
            display_entity_lista(encontrados, "Usuários Encontrados")
        elif escolha == '4':
            user_id = input("ID do usuário para atualizar: ").strip()
            user = get_id_entity('usuarios', user_id)
            if not user:
                print("Usuário não encontrado.")
                continue
            novo_nome = input(f"Novo Nome [{user['nome']}]: ").strip() or user['nome']
            novo_email = input(f"Novo Email [{user['email']}]: ").strip() or user['email']
            novo_perfil = input(f"Novo Perfil [{user['perfil']}]: ").strip().lower() or user['perfil']
            if not validar_email(novo_email):
                print("E-mail inválido.")
                continue
            if novo_perfil not in ['usuario', 'admin', 'usuário']:
                print("Perfil inválido.")
                continue
            success = atualizar_usuario(user_id, novo_nome, novo_email, novo_perfil)
            print("Usuário atualizado com sucesso." if success else "Erro ao atualizar usuário.")
        elif escolha == '5':
            user_id = input("ID do usuário para remover: ").strip()
            user = get_id_entity('usuarios', user_id)
            if not user:
                print("Usuário não encontrado.")
                continue
            print("Usuário removido." if success else "Erro ao remover usuário - usuário associado com tarefa.")

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
        if escolha == '0':
            return
        if escolha == '1':
            nome = input("Nome: ").strip()
            descricao = input("Descrição: ").strip()
            data_inicio = input("Data de Início (YYYY-MM-DD): ").strip()
            data_fim = input("Data de Fim (YYYY-MM-DD) [opcional]: ").strip() or None
            if not nome or not descricao:
                print("Campos obrigatórios não podem estar vazios.")
                continue
            if not validar_data(data_inicio):
                print("Data de início inválida.")
                continue
            if data_fim and not validar_data(data_fim):
                print("Data de fim inválida.")
                continue
            result = cadastrar_projeto(nome, descricao, data_inicio, data_fim)
            print("Projeto cadastrado com sucesso." if result else "Erro ao cadastrar projeto.")
        elif escolha == '2':
            display_entity_lista(listar_projetos(), "Projetos")
        elif escolha == '3':
            termo = input("Digite o nome do projeto: ").strip()
            encontrados = buscar_projeto(termo)
            display_entity_lista(encontrados, "Projetos Encontrados")
        elif escolha == '4':
            projeto_id = input("ID do projeto: ").strip()
            projeto = get_id_entity('projetos', projeto_id)
            if not projeto:
                print("Projeto não encontrado.")
                continue
            nome = input(f"Novo nome [{projeto['nome']}]: ").strip() or projeto['nome']
            descricao = input(f"Nova descrição [{projeto['descricao']}]: ").strip() or projeto['descricao']
            data_inicio = input(f"Nova data início [{projeto.get('data_inicio')}]: ").strip() or projeto.get('data_inicio')
            data_fim = input(f"Nova data fim [{projeto.get('data_fim')}]: ").strip() or projeto.get('data_fim')
            success = atualizar_projeto(projeto_id, nome, descricao, data_inicio, data_fim)
            print("Projeto atualizado com sucesso." if success else "Erro ao atualizar projeto.")
        elif escolha == '5':
            projeto_id = input("ID do projeto para remover: ").strip()
            success = remover_projeto(projeto_id)
            print("Projeto removido." if success else "Erro ao remover projeto.")

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
        if escolha == '0':
            return
        if escolha == '1':
            titulo = input("Título: ").strip()
            projeto_id = input("ID do Projeto: ").strip()
            responsavel_id = input("ID do Responsável: ").strip()
            prazo = input("Prazo (YYYY-MM-DD): ").strip()
            status = input("Status (pendente/andamento/concluida): ").strip() 
            result = cadastrar_tarefa(titulo, projeto_id, responsavel_id, prazo, status)
            print("Tarefa cadastrada com sucesso." if result else "Erro ao cadastrar tarefa.")
        elif escolha == '2':
            display_entity_lista(listar_tarefas(), "Tarefas")
        elif escolha == '3':
            projeto_id = input("ID do projeto: ").strip()
            display_entity_lista(listar_tarefas_por_projeto(projeto_id), "Tarefas do Projeto")
        elif escolha == '4':
            responsavel_id = input("ID do Responsável: ").strip()
            display_entity_lista(listar_tarefas_por_responsavel(responsavel_id), "Tarefas por Responsável")
        elif escolha == '5':
            status = input("Status: ").strip()
            display_entity_lista(listar_tarefas_por_status(status), f"Tarefas - {status}")
        elif escolha == '6':
            tarefa_id = input("ID da tarefa: ").strip()
            tarefa = get_id_entity('tarefas', tarefa_id)
            if not tarefa:
                print("Tarefa não encontrada.")
                continue
            titulo = input(f"Título [{tarefa['titulo']}]: ").strip() or tarefa['titulo']
            projeto_id = input(f"Projeto ID [{tarefa['projeto_id']}]: ").strip() or tarefa['projeto_id']
            responsavel_id = input(f"Responsável ID [{tarefa['responsavel_id']}]: ").strip() or tarefa['responsavel_id']
            prazo = input(f"Prazo [{tarefa['prazo']}]: ").strip() or tarefa['prazo']
            status = input(f"Status [{tarefa['status']}]: ").strip() or tarefa['status']
            success = atualizar_tarefa(tarefa_id, titulo, projeto_id, responsavel_id, prazo, status)
            print("Tarefa atualizada com sucesso." if success else "Erro ao atualizar tarefa.")
        elif escolha == '7':
            tarefa_id = input("ID da tarefa para concluir: ").strip()
            success = completar_tarefa(tarefa_id)
            print("Tarefa concluída." if success else "Erro ao concluir tarefa.")
        elif escolha == '8':
            tarefa_id = input("ID da tarefa para reabrir: ").strip()
            success = reabrir_tarefa(tarefa_id)
            print("Tarefa reaberta." if success else "Erro ao reabrir tarefa.")
        elif escolha == '9':
            tarefa_id = input("ID da tarefa para remover: ").strip()
            success = remover_tarefa(tarefa_id)
            print("Tarefa removida." if success else "Erro ao remover tarefa.")

def menu_relatorios():
    menu_options = {
        '1': 'Resumo por Projeto',
        '2': 'Tarefas em Atraso'
    }
    while True:
        escolha = display_menu("Relatórios", menu_options)
        if escolha == '0':
            return
        if escolha == '1':
            project_id = input("ID do Projeto: ").strip()
            resumo = get_projeto_resumo(project_id)
            display_relatorio(resumo, "Resumo por Projeto")
        elif escolha == '2':
            resumo = get_tarefas_atrasadas()
            display_relatorio(resumo, "Tarefas em Atraso")

def main():
    iniciar_dados()
    main_menu_options = {
        '1': 'Gerenciar Usuários',
        '2': 'Gerenciar Projetos',
        '3': 'Gerenciar Tarefas',
        '4': 'Relatórios'
    }
    print("--- Sistema de Gerenciamento de Projetos ---")
    while True:
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
            print("Saindo. Dados salvos.")
            sys.exit(0)

if __name__ == '__main__':
    main()
