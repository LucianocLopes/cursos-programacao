"""
Leia uma temperatura em graus Kelvin e converta em graus Celsius
"""

while True:
    try:
        temp = float(input('Informe uma temperatura em °K: '))
    except ValueError as err:
        print(f'O valor informado não é uma temperatura em °K valida!!!\n{err}')
    else:
        temp_c = temp + 273.15
        print(f'A temperatura {temp:.2f}°K convertida em Celsius é {temp_c:.2f}°C.')
        break
