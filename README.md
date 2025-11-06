# Sistema de Gerenciamento de Projetos

Este é um sistema de linha de comando para gerenciar projetos, usuários e tarefas.

## Estrutura do Projeto

```
meugerenciador/
├── main.py      #Ponto de entrada da aplicação
├── ui.py        #Funções de interface com o usuário (menus)
├── services.py  #Lógica do negócio e operações CRUD
├── models.py    #Funções de validação e criação de registros
├── storage.py   #Funções pra salvar e ler os dados em JSON
├── reports.py   #Funções para gerar relatórios
├── utils.py     #Funções utilitárias (gerar ID, validar e-mail/data)
└── data/
    ├── usuarios.json # Armazena os dados dos usuários
    ├── projetos.json # Armazena os dados dos projetos
    └── tarefas.json  # Armazena os dados das tarefas
```

## Como Executar o Sistema

1.  **Pré-requisitos:**
    *   Python 3.x instalado.

2.  **Executar a Aplicação:**
    Navegue até a pasta raiz `meugerenciador` e execute o arquivo `main.py`:
    ```bash
    cd meugerenciador
    python3 main.py
    ```

## Como foi feito:

### Fase 1: Definindo o programa

- **Análise dos Requisitos:** Identificando as entidades e atributos, e separando dictório para json.


### Fase 2: Fazendo os códigos (em ordem)

1.  **`storage.py`:**
    *   Função pra carregar a lista de dicionários do arquivo json da entidade.
    *   Função pra salvar uma lista de dicionários no arquivo JSON.

2.  **`utils.py`:**
    *   Função pra gerar um ID único e aleatório para cada novo cadrastro.
    *   Funções para validar o formato de e-mails e datas.

3.  **`models.py`:**
    *   Regras para cada entidade (e-mail único para usuário, nome de projeto único, datas válidas).
    *   Funções pra criar os registros com dados fornecidos.

### Fase 3: Lógica

1.  **`services.py`:**
    *   CRUD (Create, Read, Update, Delete).
    *   Funções para cadastrar, listar, buscar, atualizar e remover registros.
    *   Regra pra n permitir excluir registro que tenha dependencias(por exemplo: usuario sendo responsavel por tarefas).

2.  **`reports.py`:**
    *   Gerar um resumo de tarefas por projeto.
    *   Lista todas as tarefas com prazo vencido.

### Fase 4: Interface do Usuário

1.  **`ui.py`:**
    *   Exibe menus de opções de forma padronizada.
    *   Formata e exibe listas de registros.
    *   Formata e exibe os relatórios gerados.

2.  **`main.py`:**
    *   **Ponto de Entrada (`main()`)**: Liga o sistema, exibe o menu principal.
    *   **Loop Principal**: Mantém o programa em execução, esperando a entrada do usuário para navegar entre os menus de gerenciamento (Usuários, Projetos, Tarefas) e Relatórios.
    *   **Funções para cada entidade**: Para gerenciar cada uma delas.

### Fase 5: Testes e Documentação

1.  **Testes Manuais:** Execução do `main.py` para simular o fluxo de uso: cadastrar usuários, projetos e tarefas; atualizar e remover registros; e gerar todos os relatórios para garantir que os resultados são os esperados diversas vezes durante os processos.
2.  **Criação do `README.md`**: Escrever esse documento falando do projeto, e como usar.


Luana Burgareli ,
Nicole Cerqueira Nakahara, Gabriel ferreira
