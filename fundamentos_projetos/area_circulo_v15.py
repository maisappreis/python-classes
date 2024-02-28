from math import pi
import sys
import errno

# Deixando a cor de erro vermelha
# Essas cores ficam armazenadas no escopo global, e se isso não for necessário, então pode-se colocar dentro de uma classe.
# Porque tanto mais coisas no global, dir(), mais chances de uma coisa sobreescrever a outra.


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do circulo.")
    # Sintaxe: area_circulo_v11.py <raio>
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):
    return pi * (float(raio) ** 2)

# sys.argv[0] é o nome do script
# sys.argv[1] é o raio


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        # erro importado, o qual diz que a operação não foi permitida
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser um valor numérico' +
              TerminalColor.NORMAL)  # erro em vermelho, depois volta ao normal
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]  # acessando o argumento da posição 1, que é o raio.
    area = circulo(raio)
    print('Área do circulo:', area)


# NO TERMINAL
# > cd fundamentos_projetos
# > python area_circulo_v15.py abc (cai na validação)
# > python area_circulo_v15.py 15 (aqui informando a área do circulo)
