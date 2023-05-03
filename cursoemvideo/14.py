#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite aqui seu salario: R$ '))
AumentoSalario15 = 0.15*salario #calculo de porcentagem "salario * valor da porcentagem / 100"
print(f'Você recebeu um aumento de R$ {AumentoSalario15:.2f}')
print(f'Agora seu salario atual é de R$ {salario+AumentoSalario15:.2f} Parabéns! =D')