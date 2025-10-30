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
        choice = display_menu("Gerenciamento de Usuários", menu_options)
        if choice == '0': return

        if choice == '1':
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

        elif choice == '2':
            display_entity_lista(listar_usuarios(), "Usuários")

        elif choice == '3':
            termo = str(input("Digite o nome ou e-mail: "))
            encontrados = buscar_usuario(termo)
            display_entity_lista(encontrados, "Usuários Encontrados")

        elif choice == '4':
            user_id = get_indice_entity("usuário para atualizar")
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

        elif choice == '5':
            user_id = get_indice_entity("usuário para remover")
            remover_usuario(user_id)
            print(f"Usuário removido com sucesso.")

#def menu_projetos():
#    while True:
#        print("\n=== MENU PROJETOS ===")
 #       print("1. Cadastrar")
  #      print("2. Listar")
  #      print("3. Buscar")
  #      print("4. Atualizar")
 #       print("5. Remover")
#        print("0. Voltar")
 #       opc = input("Escolha: ")
#
 #       if opc == "1":
  #        listar_projetos()
  #      elif opc == "3":
  #          buscar_projeto()
  #      elif opc == "4":
  #          atualizar_projeto()
  #      elif opc == "5":
  #          remover_projeto()
  #      elif opc == "0":
  #          break
  #      else:
  #          print("Opção inválida.")

