
# Função de Alta Ordem
# High Order Functions: funções que recebem outras Funções como parametro. Ou Função retornando Função.

from first_class_function import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)