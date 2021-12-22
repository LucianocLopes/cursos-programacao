"""
Peça ao usuário 3 valores inteiros e imprima a soma deles
"""

contador = 1 # Inicia um contador
nums = list() # Inicia uma lista 
# Solicita os valores ao usuário e faz o um cast para inteiros
while contador <= 3:
    try:
        valor = int(input(f'Informe um {contador}º número inteiro ({contador}/3): '))
    except ValueError: # Trata a excessão caso o seja um valor invalido
        print('Valor informado é invalido! Tente novamente.')
    else:
        contador += 1 # acrescenta o contador
        nums.append(valor) # adiciona o valor na lista
# imprime a lista de valores informados e a soma deles
print(f'A soma do valores inteiros {nums} é {sum(nums)}.')
