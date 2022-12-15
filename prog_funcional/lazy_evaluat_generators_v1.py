
# Implementando um Generator.
# É uma função com memória interna, que dá retornos parciais, ela tem consciencia dos elementos dela.
# Lazy Evaluation: avaliação tardia.
# Deixar o processamento para quando for realmente necessário. Como no generator, que gera conforme demanda.

# 'yield' produzir, produção, vai produzir um retorno parcialmente cada um dos valores.

def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator)) # No final ele dá um StopIteration.