a = input('Digite uma frase:')
print(a, 'É do tipo primitivo', type(a))
print(a, 'Possui apenas números?', a.isnumeric(), '!')
print(a, 'Possui apenas letras?',  a.isalpha(), '!')
print(a, 'Possui letra ou número?', a.isalnum())
print(a, 'Possuia apenas letras maiúsculas?', a.isupper())
print(a, 'Possui apenas letras minúsculas?', a.islower())

#"a" e o objeto