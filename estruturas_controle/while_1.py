from random import randint

numero_informado = -1 # aqui o ideal é colocar um número que está fora do intervalo do número sorteado.
numero_secreto = randint(0, 9)  # vai 'sortear' um número inteiro aleatório entre 0 e 9.


# Enquanto a afirmação do 'while' for 'true' haverá uma quantidade indeterminada de repetições.


while numero_informado != numero_secreto: # enquanto eles forem diferentes, teremos um looping infinito
    numero_informado = int(input('Informe o numero: '))

print('O numero secreto {} foi encontrato!'.format(numero_secreto))