# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Fazendo a troca das variáveis de outra maneira, tipo assim: a = 3 e b = 5
# (a, b) = (b, a) eu estou trocando os valores.

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limite:                  
        penultimo, ultimo = ultimo, penultimo + ultimo # aqui acontece a troca das variáveis. Fica menos claro, menos legível.
        print(ultimo, end=',')



if __name__ == '__main__':
    fibonacci(50000)