
# No Python não existe um SWITCH CASE nativo, mas é possível simular um.
# Simulando um SWITCH com Generator


def get_tipo_dia(dia):
    dias = {   # dicionário
        (1, 7): 'Fim de Semana',  # A chave é uma tupla: (1, 7)
        tuple(range(2, 7)): 'Dia da semana'  # A chave é uma tupla; (2, 3, 4, 5, 6)
    }

    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros) # generator
    return next(dia_escolhido, '** dia invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')