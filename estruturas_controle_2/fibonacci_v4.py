# Sequencia de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Agora usando a LISTA.


def fibonacci(limite):
    resultado = [0, 1]  # aqui é a LISTA    
    while resultado[-1] < limite: # [-1] é o ultimo e [-2] é o penultimo.
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(5000):
        print(fib)