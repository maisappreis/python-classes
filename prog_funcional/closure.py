
# Closure - Fechamento.
# a função sabe o que tem dentro dela, e tmb tem conciência do que tem ao redor dela.
# interscope e outscope.


def multiplicar(x):
    def calcular(y): # a função 'calcular' não recebe 'x', mas ela tem conciência que 'x' pelo local onde ela foi definina, dentro de 'multiplicar'.
        return x * y
    return calcular   # uma função retornando outra função. High Order Functions ou Função de Alta Ordem.


if __name__ == '__main__':
    dobro = multiplicar(2) # qnd armazeno uma função dentro de uma variavel.
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)

    print(f'O triplo de 3 eh {dobro(3)}')
    print(f'O dobro de 7 eh {dobro(7)}')