# FOR sendo usado com dicionario.

produto = {'nome': 'Caneta', 'preco': 19.99,
            'importada': True, 'estoque': 785}


for chave in produto.keys(): # pode colocar apenas 'produto:' que ele já irá percorrer as chaves
    print(chave)


for valor in produto.values():
    print(valor)


for chave, valor in produto.items(): # esses valores ficam disponíveis também fora do laço.
    print(chave, '=', valor)         # Já em JS, apenas se usasse a 'var' ficaria fora. Se usasse 'let', ficaria visivel apenas no bloco.


print(chave, valor) # isso prova que está visivel fora do bloco.