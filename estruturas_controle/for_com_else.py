# Bons costumes do Python é criar constantes com letras maiusculas.

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica') # tupla
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split(): # 'split' quebra o texto por palavras.
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui palavras proibidas:', palavra)
            break  # esse 'break' está associado ao 'for' mais próximo.

    else:
        print('Texto autorizado:', texto)
