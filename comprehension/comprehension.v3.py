# Cria listas de uma forma muito mais concisa e rápida.
# Conciso é algo que está resumido ao essencial, que é sucinto e preciso.

# Agora criando Dicionario ao inves de Lista
# [ chave: expressão for item in list if condicional ]


dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)


for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')


dicionario2 = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dicionario2)