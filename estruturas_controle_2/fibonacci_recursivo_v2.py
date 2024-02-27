
# Agora usando operador ternário, IF e ELSE.
# Aquela '\' é apenas para quebrar a linha.


# Aqui usando um parâmetro padrão para armazenar em um tupla os 2 número iniciais, em 'sequencia'.
# E usando tupla com a função soma também.


def fibonacci(quantidade, sequencia=(0, 1)):
    return sequencia if len(sequencia) == quantidade else \
    fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),)) # (sum(sequencia[-2:]),) isso aqui é uma Tupla de 1 único elemento.


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
