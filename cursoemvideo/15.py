#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em °C: '))
print('A temperatura em Fahrenheit é {:.1f} °F.'.format(celsius * 1.8 + 32))

# Celsius*1.8+32 é exatamente a mesma coisa que ([(Celsius*9)]/2)+32, pois, 9/5=1.8.