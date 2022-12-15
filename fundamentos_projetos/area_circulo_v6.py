import math

# Vai ser criada uma condição para que esse módulo só seja executado se estiver no módulo __main__

if __name__ == '__main__': # em Python, o bloco desse 'if' é determinado pelos tabs, e não por {}
    pi = math.pi
    raio = input('Informe o raio: ') # quando digitado no terminal, ele vem como string, e dá erro.
    area = pi * (float(raio) ** 2) # por isso, aqui a gente tranforma ele para número flutuante.
    print('Área do circulo:', area)
