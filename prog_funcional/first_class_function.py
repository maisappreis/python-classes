
# Função de Primeira Classe
# First Class Functions: armazenar uma Função dentro de uma variável. Funções como dados.

def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


# Vai armazenar funções dentro de uma lista, ou seja, dentro de ambientes que seriam para armazenar dados.
# Conseguimos armazenar funções em variáveis. Função tradada como dado.
# Vai retornar alternamente o dobro ou quadrado nos números de 1 a 10.


if __name__ == '__main__':
    d = dobro # função 'dobro' armazenada dentro da variável 'd'.
    print(d(5))

    q = quadrado
    print(q(5))

    funcoes = [dobro, quadrado] * 5
    for funcao, numero in zip(funcoes, range(1, 11)):
        print(f'O {funcao.__name__} de {numero} eh {funcao(numero)}')

