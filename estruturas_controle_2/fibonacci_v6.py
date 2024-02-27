# SequÊncia de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21.....


# Agora usando o BREAK


def fibonacci(quantidade):
    resultado = [0, 1]
    while True: 
        resultado.append(sum(resultado[-2:])) 
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10): # Gerar apenas os 10 primeiros números da LISTA (array).
        print(fib)