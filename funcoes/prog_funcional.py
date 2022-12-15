
# Um pouco de Programação Funcional - CALLABLE
# Callable = chamavel, que tem a habilidade de ser chamado.

# É passado uma função como parâmetro para outra função.

def executar(funcao):
    if callable(funcao):  # para não gerar erro caso seja passado um parâmetro que não é passivel de ser chamado.
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa Tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1) # esse parâmetro não é passivel de ser chamado.