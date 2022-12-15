#! python

# Usando o parâmetro padrão ou parâmentro opcional.


def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


 # Assert faz testes. Se for falso, vai gerar um erro, e o programa vai parar.


if __name__ == '__main__':
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'
    print(tag_bloco('bloco'))


# Se eu executar e não retornar nada, é porque deu certo.
