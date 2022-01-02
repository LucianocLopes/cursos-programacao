"""
Leia uma temperatura em graus Celsius e apresente-a convertida em Fahrenheit.
"""

while True:
    try:
        temp = float(input('Informe uma temperatura em °C: '))
    except ValueError as err:
        print(f'Valor informado não é uma temperatura válida!\n{err}')
    else:
        temp_f = (temp * (9.0 / 5.0 )) + 32
        print(f'A temperetura {temp:.0f}°C convertida em Fahrenheit é {temp_f:.0f}°F.')
        break

