
# Filter
# Filtra dados, o resultado gera um novo conjunto, seja lista, tupla ou dicionário.
# Mas a quantidade de elementos é menor em relação à original.


pessoas = [
    {'nome': 'Renan', 'idade': 35},
    {'nome': 'Maisa', 'idade': 28},
    {'nome': 'Duff', 'idade': 1},
    {'nome': 'Mirian', 'idade': 27},
    {'nome': 'Luna', 'idade': 9},
    {'nome': 'Gabriela', 'idade': 19},
]

# em FILTER, o primeiro parâmetro vai retornar TRUE ou FALSE.

menores = filter(lambda p: p['idade'] < 18, pessoas) # se TRUE, entra no resultado final.
print(list(menores))

nomes_grandes = filter(lambda p: len(p['nome']) > 6, pessoas)
print(list(nomes_grandes))