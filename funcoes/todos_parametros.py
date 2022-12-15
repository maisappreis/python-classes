
# *args vai gerar uma Tupla (Tuple) - São argumentos POSICIONAIS variáveis.
# **kwargs vai gerar um Dicionário (Dictionary) - São argumentos NOMEADOS variáveis.


def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c') # parâmentos posicionais, em um 'packing' de TUPLE.
    todos_params(1, 2, 3, legal=True, valor=12.99) # 3 parâmentros posicionais, na TUPLE e 2 parâmentros nomeados no DICTIONARY.

    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    todos_params(primeiro='Joao', segundo='Maria') # se iniciar colocando params nomeados, o restante DEVE ser NOMEADO também. OU:
    todos_params('Maisa', primeiro='Joao') # se iniciar colocando params nomeados, o restante DEVE ser NOMEADO também.
