"""
Faça um programa de leia um número inteiro e imprima
"""

# Solicita um numero do usuário e faz um cast para inteiro
try:
    num = int(input('Digite um número inteiro: '))
except ValueError: # trata a excessão caso seja informado um valor invalido 
    print('O valor informado não é um número inteiro!')
else:
    # Imprime o valor inteiro informado
    print(f'O valor inteiro informado é {num}')