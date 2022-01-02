"""
Leia uma temperatura em graus Fahrenheit e converta em graus Celsius.
"""

while True:
    try:
        temp = float(input('Informe uma temperatura °F: '))
    except ValueError as err:
        print(f'O valor informado não é uma temperatura °F válida!!\n{err}')
    else:
        temp_c = 5.0 * ((temp - 32) / 9.0)
        print(f'A temperatura {temp:.0f}°F convertida em Celsius é {temp_c:.0f}°C.')
        break
