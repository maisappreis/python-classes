from math import pi
import sys
import errno


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0])) # Sintaxe: area_circulo_v11.py <raio>


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':   
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM) # erro importado, o qual diz que a operação não foi permitida 
        
    # else:
    raio = sys.argv[1] # acessando o argumento da posição 1, que é o raio.
    area = circulo(raio)
    print('Área do circulo:', area)
