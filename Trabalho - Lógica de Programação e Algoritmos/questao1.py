print('Bem-vindo à Loja da Julia Silva de Souza!')

# Valor unitário e quantidade de produtos:
valor_unitario = input('Qual o valor do produto? ')
valor_unitario = float(valor_unitario)

quantidade_produto = input('Quantidade: ')
quantidade_produto = int(quantidade_produto)

# Cálculo total 
valor_total = valor_unitario * quantidade_produto

# Regras para descontos:
if valor_total < 2500:
    desconto = 0.0
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07
else:
    desconto = 0.11

# Aplicação de descontos
valor_desconto = valor_total * desconto 
valor_final_com_desconto = valor_total - valor_desconto


print(f'Valor total SEM desconto: R${valor_total}')
print(f'Valor total COM desconto: R${valor_final_com_desconto}')
