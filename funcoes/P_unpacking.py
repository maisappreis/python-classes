
# Packing & Unpacking.


def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros): # isso fará com que este parâmento se torne uma TUPLE.
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(6, 7, 1))

    # Packing
    print(soma_n(1, 1, 1))
    print(soma_n(2, 2, 2, 2, 2, 2, 2))

    # Unpacking
    tupla_nums = (1, 2, 3) # tupla
    print(soma_3(*tupla_nums)) # isso seria um 'unpacking', porque o 'nums' está sendo desempacotado.

    lista_nums = [1, 2, 3] # lista
    print(soma_3(*lista_nums)) # isso seria um 'unpacking', porque o 'nums' está sendo desempacotado.
    

# print(type(numeros))
