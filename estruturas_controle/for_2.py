# FOR
# Aplicando o FOR com: strings, listas, tuplas e sets

# A diferença entre usar enumerate() e não usá-lo está na capacidade de obter
# tanto o valor quanto a posição do elemento durante a iteração. Ou seja, o enumerate() dá acesso ao index.

# Sobre o SET
# Pode ser escrito assim: {1, 2, 3, 4, 5, 6}
# Ou assim: set(1, 2, 3, 4, 5, 6)

palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=', ') # sem esse 'end' ele quebra as linhas, 
print('Fim')


aprovados = ['Bia', 'Liz', 'Leo', 'Gui', 'Dio']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)


dias_semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado') # é uma tupla, mas lista(array) também funciona aq.
for dia in dias_semana:
    print(f'Hoje eh {dia}')


for numero in {1, 2, 3, 4, 5, 6}: # isso é um set, também pode ser escrito assim: set(1, 2, 3, 4, 5, 6)
    print(numero)


# Assim, vemos que é possível percorrer strings, listas, tuplas e sets