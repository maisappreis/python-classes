# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Agora usando a função SOMA


def fibonacci(limite):
    resultado = [0, 1]  # aqui é a LISTA    
    while resultado[-1] < limite: # [-1] é o último e [-2] é o penúltimo.
        resultado.append(sum(resultado[-2:])) # assim ele pega os 2 últimos valores da lista.
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(1000):
        print(fib)