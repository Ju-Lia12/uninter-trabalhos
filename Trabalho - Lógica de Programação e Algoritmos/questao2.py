print('Bem-vindo à Loja de Gelados da Julia Silva de Souza!')
print('-' * 20, 'Cardápio', '-' * 20)
print('-' * 50)
print('-' * 5, '| Tamanho | Cupuaçu (CP) | Açaí (AC) |', '-' * 5)
print('-' * 5, '|    P    |    R$ 9,00   |  R$11,00  |', '-' * 5)
print('-' * 5, '|    M    |    R$14,00   |  R$16,00  |', '-' * 5)
print('-' * 5, '|    G    |    R$18,00   |  R$20,00  |', '-' * 5)
print('-' * 50)

# Definindo while e total do pedido
pedir_novamente = 'SIM'
total = 0
while pedir_novamente == 'SIM' or pedir_novamente == 'sim':
    sabor = input('Qual o sabor desejado CP/AC? ')
    if sabor != 'CP' and sabor != 'AC' and sabor != 'cp' and sabor != 'ac':
        print('Sabor inválido, tente novamente.')
        continue  
    while True:
        tamanho = input('Qual o tamanho que você gostaria P/M/G? ')
        if tamanho != 'P' and tamanho != 'p' and tamanho != 'M' and tamanho != 'm' and tamanho != 'G' and tamanho != 'g':
            print('Tamanho inválido, tente novamente.')  
            continue  
        else: 
            break
    
    # Checando sabores, tamanhos e calculando valor de cada pedido
    if(sabor == 'CP' or sabor == 'cp') and (tamanho == 'P' or tamanho == 'p'):
        print('O valor do seu pedido é de: R$ 9,00')
        total = total + 9
    elif(sabor == 'CP' or sabor == 'cp') and (tamanho == 'M' or tamanho == 'm'):
        print('O valor do seu pedido é de: R$ 14,00')
        total = total + 14
    elif(sabor == 'CP' or sabor == 'cp') and (tamanho == 'G' or tamanho == 'g'):
        print('O valor do seu pedido é de: R$ 18,00')
        total = total + 18
    elif(sabor == 'AC' or sabor == 'ac') and (tamanho == 'P' or tamanho == 'p'):
        print('O valor do seu pedido é de: R$ 11,00')
        total = total + 11
    elif(sabor == 'AC' or sabor == 'ac') and (tamanho == 'M' or tamanho == 'm'):
        print('O valor do seu pedido é de: R$ 16,00')
        total = total + 16
    elif(sabor == 'AC' or sabor == 'ac') and (tamanho == 'G' or tamanho == 'g'):
        print('O valor do seu pedido é de: R$ 20,00')
        total = total + 20
    print('')
    # Verificando se o usuário deseja continar fazendo outros pedidos ou não 
    pedir_novamente = input('Deseja pedir mais alguma coisa? ')
    if pedir_novamente == 'NAO' or pedir_novamente == 'nao':
        break
    elif pedir_novamente == 'SIM' or pedir_novamente == 'sim':
        continue

print('')
print(f'O valor total a ser pago é de: R${total},00')