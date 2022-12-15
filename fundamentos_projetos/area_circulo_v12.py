from math import pi
import sys


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0])) # Sintaxe: area_circulo_v11.py <raio>


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':   
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1] # acessando o argumento da posição 1, que é o raio.
        area = circulo(raio)
        print('Área do circulo:', area)


# NO TERMINAL
# dentro de '>cd fundamentos_projetos'
# >python area_circulo_v12.py

# ou
# >python area_circulo_v12.py 15 (aqui informando a área do circulo)


# sys.argv[0] é o nome do stript
# sys.argv[1] é o raio
