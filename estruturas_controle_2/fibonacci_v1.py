# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Usando While Infinito.
# Funções recursivas (que chamam a si mesmas), sem condição de parada, tornam-se um loop infinito 
# e pararia em um erro de estouro de pilha de chamadas (stack overflow), ao consumir todo o espaço dedicado para
# tal fim. Em Python a exceção gerada e RecursionError com a mensagem maximum recursion depth exceeded.


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