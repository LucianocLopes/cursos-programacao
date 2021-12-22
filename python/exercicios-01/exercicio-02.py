"""
Faça um programa que leia um número real e o imprima
"""

# Solicita ao usuário um número real
try:
    num = float(input('Digite um número real: '))
except ValueError: # Trata a excessão caso seja um valor inválido
    print('O valor informado não é numero!')
else:
    # Imprime o valor num em um cast para float
    print(f'O valor real informado é {num}.')
