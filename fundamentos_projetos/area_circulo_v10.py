from math import pi
import sys


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':   
    if len(sys.argv) < 2:
        print("""\
            É necessário informar o raio do circulo.
            Sintaxe: area_circulo <raio>""")
    else:
        raio = sys.argv[1] # acessando o argumento da posição 1
        area = circulo(raio)
        print('Área do circulo:', area)


# NO TERMINAL
# dentro de '>cd fundamentos_projetos'
# >python area_circulo_v10.py

# ou
# >python area_circulo_v10.py 15 (aqui informando a área do circulo)
