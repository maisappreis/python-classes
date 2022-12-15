
# Lazy Evaluation: avaliação tardia.
# Deixar o processamento para quando for realmente necessário. Como no generator, que gera conforme demanda.
# Usando o Generator da V1 com o FOR.

def sequence():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == '__main__':
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))