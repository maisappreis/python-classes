# Bons costumes do Python é criar constantes com letras maiusculas.

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica') # tupla
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]

for texto in textos:
    found = False  # se não encontrar, será 'false' (variável de controle)
    for palavra in texto.lower().split(): # 'split' quebra o texto por palavras.
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui palavras proibidas:', palavra)
            found = True
            break  # esse 'break' está associado ao 'for' mais próximo.

    if not found:
        print('Texto autorizado:', texto)
