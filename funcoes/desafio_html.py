
def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs: # verifica se há esse parâmentro nomeado.
        kwargs['class'] = kwargs.pop('html_class') # 'pop' retorna o valor de uma chave, e exclui a chave, 'html_class', e substitui por 'class'.
    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items()) # gera todas as chave="valor"
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p', 
            tag('span', 'Curso Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leornado Leitao', id='ll'),
            tag('span', '.'),
            html_class='alert'),
            )
    