from math import pi

# Agora dentro de uma função Python, porém essa função não tem um retorno.


def circulo(raio):
    print('Área do circulo:', pi * (float(raio) ** 2))


if __name__ == '__main__':
    raio = input('Informe o raio: ')

    circulo(raio)


# NO TERMINAL
# dentro de '>fundamentos_projetos'

# >python (esse comando chama o interpretador)
# >import area_circulo_v7 (importa o arquivo pelo nome)
# >area_circulo_v7.circulo(15) (chama o arquivo.nome da função)

# outra opção

# >from area_circulo_v7 import circulo(raio)
# >circulo(15)