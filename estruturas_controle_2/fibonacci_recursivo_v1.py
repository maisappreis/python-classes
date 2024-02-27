
# Aqui usando um parâmetro padrão para armazenar em um tupla os 2 número iniciais, em 'sequencia'.
# E usando tupla com a função soma também.


def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade: # condição de parada
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),)) # (sum(sequencia[-2:]),) isso aqui é uma Tupla de 1 único elemento.


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
