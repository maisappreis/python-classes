
# Implementando um 'map()' 
# Aqui também tem o conceito de Lazy Evaluation: Avaliação Tardia. Também é um generator, fica gerando os resultados conforme a demanda.

# De uma forma diferente, também com avaliação tardia, e generator.

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    # print(list(resultado))

    print(next(resultado)) # vai chamando um a um.
    print(next(resultado))
    print(next(resultado))


# o parâmetro funcao seria 'lambda x: x ** 2' - a função anonima lambda.