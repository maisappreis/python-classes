
# Funções anônimas
# Anonymous Functions: as 'Lambda'. São funções com funcionalidades bem específicas.

# Uma TUPLE de DICTIONARY

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 5, 'preco': 20},
    {'quantidade': 6, 'preco': 15}
)

totais = tuple(
    map(lambda compra: compra['quantidade'] * compra['preco'],
    compras)
)

print('Precos totais:', totais)
print('Total geral:', sum(totais))