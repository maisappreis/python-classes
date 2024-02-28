from math import pi
import sys

# Obtendo o argumento via terminal


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':   
    raio = sys.argv[1] # acessando o argumento da posição 1
    area = circulo(raio)
    print('Área do circulo:', area)


# NO TERMINAL
# dentro de '> cd fundamentos_projetos'
# > python area_circulo_v9.py
