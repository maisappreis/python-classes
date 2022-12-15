
# Implementando uma versão própria do 'map()' 
# Aqui também tem o conceito de Lazy Evaluation: Avaliação Tardia. Também é um generator, fica gerando os resultados conforme a demanda.

def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))


# o parâmetro funcao seria 'lambda x: x ** 2' - a função anonima lambda.