from math import pi
import sys
import errno


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0])) # Sintaxe: area_circulo_v11.py <raio>


def circulo(raio):
    return pi * (float(raio) ** 2)

# sys.argv[0] é o nome do script
# sys.argv[1] é o raio

if __name__ == '__main__':   
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM) # erro importado, o qual diz que a operação não foi permitida 

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1] # acessando o argumento da posição 1, que é o raio.
    area = circulo(raio)
    print('Área do circulo:', area)


# NO TERMINAL
# > cd fundamentos_projetos
# > python area_circulo_v14.py abc (cai na validação)
# > python area_circulo_v14.py 15 (aqui informando a área do circulo)



