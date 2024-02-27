# SET

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'} # set
textos = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida'
]

# Comparar dois conjuntos, ou seja, dois 'sets'.
# Para isso, o 'texto' precisa ser transformado em um 'set'.
# 'split' quebra o texto por palavras.

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao: # se retornar vazio, vai ser 'False', e cai no 'else'.
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado:', texto)