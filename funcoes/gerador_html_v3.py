#! python

# Usando o Generator.


def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens)) # Aqui tem um Generator, com ()
    # lista = ''.join([f'<li>{item}</li>' for item in itens]) # Mas poderia ser um List Comprehension, com []
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':    
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(inline=True, conteudo='inline')) # Aqui o parâmetro foi NOMEADO, para poder mudar a ordem.
    print(tag_bloco('falhou', classe='erro')) # Aqui o parâmetro foi NOMEADO.

    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))


