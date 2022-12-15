
# Simulando um SWITCH com Generator

def get_tipo_dia(dia):
    dias = {   # dicionario.
        (1, 7): 'Fim de Semana',  
        tuple(range(2, 7)): 'Dia da semana'  # Cria essa tupla = (2, 3, 4, 5, 6)
    }

    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')