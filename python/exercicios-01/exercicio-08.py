"""
Leia uma temperatura em graus Celsius e converta em graus Kelvim. 
"""

while True:
    try:
        temp = float(input('Informe uma temperatura em °C: '))
    except ValueError as err:
        print(f'O valor informado não é uma temperatura em °C valida!!!\n{err}')
    else:
        temp_k = temp - 273.15
        print(f'A temperatura {temp:.2f}°C convertida em Kelvin é {temp_k:.2f}°K.')
        break
