
# *args vai gerar uma Tupla (Tuple)
# **kwargs vai gerar um Dicionário (Dictionary)


# Agora gerando um Dicionário - **kwargs
# Obrigatoriamente chamar os parãmetros nomeados.


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} --> {piloto}') # aqui é o Packing de um dicionário.


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
