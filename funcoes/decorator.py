
# 'function' é a função que será decorada.
# 'log' será o DECORATOR que vai decorar a 'function'.

# *args vai gerar uma Tupla (Tuple) - São argumentos POSICIONAIS variáveis.
# **kwargs vai gerar um Dicionário (Dictionary) - São argumentos NOMEADOS variáveis.

def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y

@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(2,3))
    print(sub(6, y=3)) # com parâmentro NOMEADO.