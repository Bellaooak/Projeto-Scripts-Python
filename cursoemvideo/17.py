print('\t Tabuada ') #e um algoritmo mais sofisticado que int, uma opcao

numero = int(input('Digite o numero da tabuada que deseja: '))

print('\n Tabuada de', numero, ':')

for i in range(1, 11):

    print(numero, 'X', i, '=', (numero * i))