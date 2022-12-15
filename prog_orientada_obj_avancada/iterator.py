
# Iterator 
# Faz a iteração: processo de resolução de uma equação mediante operações em que
# sucessivamente o objeto de cada uma é o resultado da que a precede.


class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1] # pegando do ultimo para o primeiro.

    def __iter__(self):
        return self # 'self' aqui é um 'iterator'. Com isso, consigo iterar um FOR.

    # Esse é o padrão do Iterator
    def __next__(self):
        try:
            return self.cores.pop() # método pop() pega/lê o ultimo e exclui ele.
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores)) # a 4ª chamada aqui daria erro. IndexError: pop from empty list

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

    for cor in RGB():
        print(cor)
