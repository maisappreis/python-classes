#! python

# Usando o parâmetro nomeado.


def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'



if __name__ == '__main__':    
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(inline=True, texto='inline')) # Aqui o parâmetro foi NOMEADO, para poder mudar a ordem.
    print(tag_bloco('falhou', classe='erro')) # Aqui o parâmetro foi NOMEADO.



