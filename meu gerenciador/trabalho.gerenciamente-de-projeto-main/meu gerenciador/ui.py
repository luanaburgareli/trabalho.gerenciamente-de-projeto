
def display_menu(titulo, opcoes):
    print()
    print("=== " + titulo + " ===")
    for chave, valor in opcoes.items():
        print("[" + chave + "] - " + valor)
    print("[0] - Voltar")

    while True:
        escolha = input("Escolha uma opção: ")
        if escolha in opcoes or escolha == "0":
            return escolha
        else:
            print("Opção inválida, tente novamente.")


def display_entity_lista(dados, titulo):
    if len(dados) == 0:
        print()
        print("Nenhum(a) " + titulo.lower() + " encontrado(a).")
        return

    print()
    print("=== Lista de " + titulo + " (" + str(len(dados)) + " registros) ===")

    if titulo == "Usuários":
        print("ID | Nome | E-mail | Perfil")
        print("-----------------------------------------")
        for d in dados:
            print(d.get("id", "N/A"), "|", d.get("nome", "N/A"), "|", d.get("email", "N/A"), "|", d.get("perfil", "N/A"))

    elif titulo == "Projetos":
        print("ID | Nome | Descrição | Início | Fim")
        print("-----------------------------------------")
        for d in dados:
            desc = d.get("descricao", "")
            if len(desc) > 30:
                desc = desc[:27] + "..."
            print(d.get("id", "N/A"), "|", d.get("nome", "N/A"), "|", desc, "|",
                  d.get("data_inicio", "N/A"), "|", d.get("data_fim", "N/A"))

    elif titulo == "Tarefas":
        print("ID | Título | Projeto ID | Responsável ID | Status | Prazo")
        print("-----------------------------------------")
        for d in dados:
            titulo_tarefa = d.get("titulo", "")
            if len(titulo_tarefa) > 20:
                titulo_tarefa = titulo_tarefa[:17] + "..."
            print(d.get("id", "N/A"), "|", titulo_tarefa, "|", d.get("projeto_id", "N/A"), "|",
                  d.get("responsavel_id", "N/A"), "|", d.get("status", "N/A"), "|", d.get("prazo", "N/A"))
    else:
        print("Tipo de lista não suportado.")

def display_relatorio(dados, titulo):
    if dados is None:
        print("Erro ao gerar relatório.")
        return

    print()
    print("=== Relatório:", titulo, "===")

    if titulo == "Resumo por Projeto":
        print("Projeto:", dados["projeto"])
        print("Total de tarefas:", dados["total_tarefas"])
        print("Status:")
        for status, qtd in dados["status"].items():
            print("  -", status, ":", qtd)
        print("Percentual Concluídas:", dados["percentual_concluidas"], "%")

    elif titulo == "Tarefas em Atraso":
        print("Total de tarefas em atraso:", dados["total_atrasadas"])
        if dados["total_atrasadas"] > 0:
            print()
            print("ID | Título | Projeto | Responsável | Prazo | Status")
            print("-----------------------------------------")
            for d in dados["detalhes"]:
                titulo = d["titulo"]
                projeto = d["projeto"]
                resp = d["responsavel"]
                if len(titulo) > 20: titulo = titulo[:17] + "..."
                if len(projeto) > 20: projeto = projeto[:17] + "..."
                if len(resp) > 20: resp = resp[:17] + "..."
                print(d["id"], "|", titulo, "|", projeto, "|", resp, "|", d["prazo"], "|", d["status"])
