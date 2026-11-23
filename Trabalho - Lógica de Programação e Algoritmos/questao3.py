print('Bem-vindo à Copiadora de Julia Silva de Souza!')
print('')

# Função perguta qual o serviço desejado e retorna o valor por página.
def escolha_servico():
    print('Escolha o serviço desejado: ')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    while True:
        servico = input('Serviço escolhido: ')
        if servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT':
            print('Escolha inválida, digite o tipo de serviço novamente.')
        elif servico == 'DIG':
            return 1.10
        elif servico == 'ICO':
            return 1.00
        elif servico == 'IPB':
            return 0.40
        elif servico == 'FOT':
            return 0.20

# Função pergunta o n° de páginas desejadas e aplica o desconto 
def num_pagina():
    while True: 
        paginas = input("Escolha a quantidade de páginas desejadas: ")
        try:
            paginas = int(paginas)
        except:
            print('Erro, tente novamente com valores numéricos.')
            continue
        if paginas < 20:
            desconto = 0
        elif paginas >= 20 and paginas < 200:
            desconto = 0.15
        elif paginas >= 200 and paginas < 2000:
            desconto = 0.20
        elif paginas >= 2000 and paginas < 20000:
            desconto = 0.25
        else:
            print('Você excedeu o limite de páginas. Por favor, tente novamente com menos páginas.')
            continue
        return paginas - paginas * desconto
    
# Função pergunta se o usuário deseja um serviço extra e retorna o valor 
def servico_extra():
    print('Deseja adicionar outros serviços?')
    print('1. Encadernação Simples: R$15.00')
    print('2. Encadernação Capa Dura: R$40.00')
    print('0. Não desejo adicionar serviços extras.')
    while True:
        extra = input('Extra escolhido: ')
        if extra == '1':
            return 15
        elif extra == '2':
            return 40
        elif extra == '0':
            return 0
        else:
            print('Opção inválida, tente novamente.')

servico_escolhido = escolha_servico()

quantidade_de_paginas = num_pagina ()

extra = servico_extra()

total_do_servico = servico_escolhido * quantidade_de_paginas + extra
print(f'Valor total: {total_do_servico} (Serviço: {servico_escolhido}, N° de páginas: {quantidade_de_paginas} + Serviço extra: {extra})')