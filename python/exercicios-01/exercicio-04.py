"""
Leia um número real e imprima o resultado do quadrado desse número
"""

while True:
    try: # Solicita um valor e faz um cast para float
        num = float(input('Informe um número real: '))
    except ValueError as err: # Trata a excessão se informado um valor inválido e usa Alias para renomear a excessão
        print(f'Valor informado não é valido! Tente novamento. {err}')
    else:
        quadrado = num * num # Realiza a conta e sai do loop
        break
# Imprime o valor informado e o resultado do quadrado desse valor
print(f'O quadrado do valor real {num} é {quadrado:.2f}.')
