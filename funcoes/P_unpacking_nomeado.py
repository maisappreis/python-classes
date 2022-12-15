
# *args vai gerar uma Tupla (Tuple)
# **kwargs vai gerar um Dicionário (Dictionary)


# Agora gerando um Dicionário - **kwargs
# Obrigatoriamente chamar os parãmetros nomeados.


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'primeiro': 'L. Hamilton',  # aqui é um Dicionário.
              'segundo': 'M. Verstappen',
              'terceiro': 'S. Vettel'}
    resultado_f1(**podium)  # aqui é o unpacking do Dicionário, desempacotando dicionário.
