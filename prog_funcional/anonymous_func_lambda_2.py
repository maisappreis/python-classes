
# Versão Alternativa à Lambda. A Lambda foi subtituida por uma outra função, 'calc_preco_total(compra)'.

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 5, 'preco': 20},
    {'quantidade': 6, 'preco': 15}
)


def calc_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calc_preco_total, compras))

print('Precos totais:', totais)
print('Total geral:', sum(totais))
