import math

pi = math.pi
raio = input('Informe o raio: ') # quando digitado no terminal, ele vem como string, e dá erro.
area = pi * (float(raio) ** 2) # por isso, aqui a gente tranforma ele para número flutuante.

print('Área do circulo:', area)

