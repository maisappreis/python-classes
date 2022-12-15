# Simulando uma estrutura Switch, por meio de uma função e usando dicionário.
# porque ela não existe em Python.

def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia da semana',
        3: 'Dia da semana',
        4: 'Dia da semana',
        5: 'Dia da semana',
        6: 'Dia da semana',
        7: 'Fim de semana'
    }
    return dias.get(dia, '** inválido **'); # parâmetro padrão para caso seja um valor inválido.


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')



