# Sequencia de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Usando While Infinito.


def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while True:                                 # while infinito, laço infinito.
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()