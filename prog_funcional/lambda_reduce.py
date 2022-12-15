
# Reduce
# Pode gerar uma outra lista, gerar um único resultado.
# Tem um acumulador, 

from functools import reduce

pessoas = [
    {'nome': 'Renan', 'idade': 35},
    {'nome': 'Maisa', 'idade': 28},
    {'nome': 'Duff', 'idade': 1},
    {'nome': 'Mirian', 'idade': 27},
    {'nome': 'Luna', 'idade': 9},
    {'nome': 'Gabriela', 'idade': 19},
]

# lambda param1, param2: - param1 'idades' acumulador - param2 'p' pessoas.
# Aquele '0' é porque acumulador inicia em 0.

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades) 