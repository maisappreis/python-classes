# Sequencia de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Agora usando o FOR ao inves de WHILE.


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade): # poderia ser também 'range(quantidade - 2)' e tem o underline ali, porque é uma variável não usada.
        resultado.append(sum(resultado[-2:])) 
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10): # Gerar apenas os 10 primeiros números da LISTA (array).
        print(fib)