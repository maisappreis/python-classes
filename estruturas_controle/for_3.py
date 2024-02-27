# FOR
# Aplicando o FOR com dicionários
# dict.keys(): me dá acesso as chaves
# dict.values(): me dá acesso aos valores
# dict.items(): me dá acesso as chaves e aos valores

# Caso eu não especifique, e coloque "for x in dict:" terei acesso apenas as chaves


produto = {'nome': 'Caneta', 'preco': 19.99,
            'importada': True, 'estoque': 785}


for item in produto: # Sem especificar, ele percorre as chaves
    print('Sem especificar:', item)


for chave in produto.keys():
    print('keys:', chave)


for valor in produto.values():
    print('values:', valor)


for chave, valor in produto.items(): # esses valores ficam disponíveis também fora do laço.
    print('items:', chave, '=', valor)         # Já em JS, apenas se usasse a 'var' ficaria fora. Se usasse 'let', ficaria visivel apenas no bloco.


print('Fora do bloco:', chave, valor) # isso prova que está visivel fora do bloco.