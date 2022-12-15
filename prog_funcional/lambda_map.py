
# map() -> mapeia uma lista(array) e retorna outra lista(array) conforme as modificações feita dentro do parametro ().
# Primeiro parametro é a transformação e o segundo parametro é quem será transformado.
# número de elementos é mantido o mesmo.

a = [1, 2, 3, 4, 5, 6, 7, 8]  # aqui pode ser LIST, ou TUPLE.

# retorna LIST 'a' com os elementos multiplicados por 2.
dobro = map(lambda i: i * 2, a)
print(list(dobro))


# retorna TUPLE 'a' com os elementos multiplicados por 3.
triplo = tuple(map(lambda i: i * 2, a))
print(tuple(triplo))


dicionario = [
    {'nome': 'Renan', 'idade': 35},
    {'nome': 'Maisa', 'idade': 28},
    {'nome': 'Duff', 'idade': 1},
]

so_nomes = map(lambda n: n['nome'], dicionario)
print(list(so_nomes))

so_idades = map(lambda i: i['idade'], dicionario)
print(sum(so_idades))

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', dicionario)
print(list(frases))