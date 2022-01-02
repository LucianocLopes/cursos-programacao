"""
Leia um número real e imprima a quinta parte deste número
"""

while True:
    try:
        num = float(input('Informe um número real: '))
    except ValueError as err:
        print(f'Valor informado não é valido! {err}')
    else:
        print(f'A quinta parte do valor {num:.2f} informado é {num / 5:.2f}')
        break
