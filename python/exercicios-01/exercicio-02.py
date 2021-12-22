"""
Faça um programa que leia um número real e o imprima
"""

# Solicita ao usuário um número real
num = input('Digite um número real: ')

# Verifica se foi informado um valor numérico
if num.isnumeric():
    # Imprime o valor num em um cast para float
    print(f'O valor real informado é {float(num)}.')
else:
    # Retorna uma mensagem que o valor é inválido
    print(f'O valor informado não é numero! {num}')
