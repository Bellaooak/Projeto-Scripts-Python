from random import shuffle

def embaralhar(nome):

    a = list(nome)

    shuffle(a)

    a = ''.join(a)

    print(a.lower())

nome = input('Um truque de magica! digite seu nome, se ele se embaralhar voce ja matou aula:')

embaralhar(nome)
print('vou contar pra sua mae =D)';

