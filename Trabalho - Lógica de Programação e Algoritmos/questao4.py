print('Bem-vindo à Livraria de Julia Silva de Souza')
print('-' * 44)

# Definição das variaveis inicias
lista_livros = []
id_global = 0


# Função para cadastrar um novo livro
def cadastrar_livro(id):
    print()
    print('-' * 13, ' MENU CADASTRAR LIVRO ', '-' * 13)
    print(f'ID do livro: {id}')
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o autor do livro: ')
    editora = input('Digite a editora do livro: ')
    novo_livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}

    lista_livros.append(novo_livro)


# Função para exibir os dados de um livro 
def exibir_livro(livro):
    print()
    print(f'ID: {livro["id"]}')
    print(f'Nome: {livro["nome"]}')
    print(f'Autor: {livro["autor"]}')
    print(f'Editora: {livro["editora"]}')
    print()


# Função para consultar todos os livros, por ID ou por autor
def consultar_livros():
    print()
    print('-' * 13, ' MENU CONSULTAR LIVROS ', '-' * 13)
    print('Escolha a opção desejada:')
    print('1. Consultar todos os livros')
    print('2. Consultar livro por ID')
    print('3. Consultar livros por autor')
    print('4. Retornar')
    opcao_escolhida = input()

    if opcao_escolhida == '1':
        for livro in lista_livros:
            exibir_livro(livro)
    elif opcao_escolhida == '2':
        id_livro = int(input('Digite o ID do livro: '))
        for livro in lista_livros:
            if livro['id'] == id_livro:
                exibir_livro(livro)
    elif opcao_escolhida == '3':
        autor = input('Digite o nome do autor: ')
        for livro in lista_livros:
            if livro['autor'] == autor:
                exibir_livro(livro)
    elif opcao_escolhida == '4':
        return


# Função para remover um livro pelo ID
def remover_livro():
    print()
    id_livro = int(input('Digite o ID do livro a ser removido: '))
    for livro in lista_livros:
        if livro['id'] == id_livro:
            lista_livros.remove(livro)
            print('Livro removido com sucesso!')

# Loop principal do programa
while True:
    print()
    print('-' * 13, ' MENU PRINCIPAL ', '-' * 13)
    print('Escolha a opção desejada:')
    print('1. Cadastrar livro')
    print('2. Consultar livro')
    print('3. Remover livro')
    print('4. Sair')
    opcao_escolhida = input()

    if opcao_escolhida == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_escolhida == '2':
        consultar_livros()
    elif opcao_escolhida == '3':
        remover_livro()
    elif opcao_escolhida == '4':
        break
    else:
        print('Opção escolhida é invalida, tente novamente.')