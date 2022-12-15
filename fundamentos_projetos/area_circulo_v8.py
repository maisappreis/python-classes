from math import pi

# Agora dentro de uma função Python COM RETORNO


def circulo(raio):
    return pi * (float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do circulo:', area)


# NO TERMINAL
# dentro de '>cd fundamentos_projetos'

# >python (esse comando chama o interpretador)
# >import area_circulo_v8 as v8 (importa o arquivo pelo nome e dá um apelido)
# >v8.circulo(15) (chama o arquivo.nome da função)

# >area=v8.circulo(15)
# >area
# >area * 2 (dessa maneira, consigo manipular o valor pelo terminal)