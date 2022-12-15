#%%----------------------------------------------------------------
# Para que apontar erros referente ao pip8: file > preferences > settings > 'flake8' > marca a caixa.
# Normalmente cada sentença de código fica em uma linha. Não se usa ;

from re import X


print(True)
print(False)
print(1.2 + 2)
print("String com aspas duplas")
print('String aspas simples')
print('Você é ' + 3 * ' muito' + ' legal')
# print(3 + '3') => erro
print([1, 2, 3]) # chamado de lista, é semelhante ao Array, mas é dinâmico, como em JavaScript.
print({'nome': 'Pedro', 'idade': 22}) # chamado de dicionário, é semelhante ao Objeto de JavaScript, estrutura chave e valor.
print(None)

#%%----------------------------------------------------------------
# Variáveis - Tipagem dinâmica e fortemene tipada, apesar de eu não falar o tipo, ele sabe.
# variável também é chamada de identificador.

a = 10
b = 2.5
print(a + b)

a = "Agora sou string"
print(a)

#%%
# Comentários
# Comentário de 1 linha
""" E assim é comentário
de multiplas linhas...."""

#%%----------------------------------------------------------------
# Operadores Artiméticos, também chamados de binários.
# x + y é 'infix', porque o operador fica no meio, 'in'.
# ++y é pré-fixado (isso não existe em Python, seria y =+ y)
# y-- é pós-fixado (isso não existe em Python, seria y =- y)

print(1 + 5)
print(8 - 5)
print(8 * 5)
print(9.4 / 3)
print(9.4 // 3) # divisão de inteiros, para que o resultado dê um número inteiro obrigatoriamente. Ele arredonda o número.
print(2 ** 8) # potência, 2 elevado a 8
print(10 % 3) # módulo, ou seja, o resto da divisão

salario = 3450.45
despesas = 2456.2456

percentual_comprometido = (despesas * 100) / salario
print(percentual_comprometido)

#%%----------------------------------------------------------------
# Operadores Relacionais

print(3 >= 4)
print(3 == 3) # não existe operador de estritamente igual em Python '===' 
print(3 != 4)
print(3 >= 4)

#%%----------------------------------------------------------------
# Operadores de atribuição
a = 3
a = a + 7
print(a)

a += 5 # forma reduzida de somar a própria variável com outro número, e atribuir o novo valor à essa variável.
print(a)

a -= 2
print(a)

a *= 4
print(a)

a /= 4
print(a)

a %= 2
print(a)

a **= 8
print(a)

a //= 100
print(a)

#%%------------------------------
# Operadores Lógicos

7 != 3 and 2 > 3

print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false

print(True or True) # true
print(True or False) # true
print(False or True) # true
print(False or False) # false

# OU exclusivo, precisa ser exclusivamente um OU outro.

print(True != True) # false
print(False != False) # false
print(True != False) # true
print(False != True) # true

# Negação lógica (operador unitário)
# Qualquer número diferente de 0 é True

print(not True) # False
print(not False) # True
not 0 # não é 0
not not -1 # duas negações se cancelam, então é -1

# Cuidado, operador lógico não é operador bit a bit

False & True
True | True
False ^ True

# Operador bit-a-bit, transforma nossos números em zeros e uns, linguagem de máquina.

# AND bit-a-bit
print(3 & 2) # ele compara os bits desses números.
# 3 = 11
# 2 = 10
# _ = 10 # resulta 2

# OR bit-a-bit
print(3 | 2)
# 3 = 11
# 2 = 10
# _ = 11 # resulta 3

# XOR bit-a-bit
print(3 ^ 2)
# 3 = 11
# 2 = 10
# _ = 01 # resulta 1

# Desafio

trabalho_terca = True
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
    .format(tv_50, tv_32, sorvete, mais_saudavel)) # esse 'format' interpola os valores dentro dos {} na string.

#%%------------------------------
# Operadores Unários

-a # número negativo
+a # número positivo

a = 5
a += 1 # não existe ++a e nem a++, nem com o --a
print(a)


# Operadores Ternários
# Opta por uma opção ou outra, dependendo de retorna False ou True

esta_chovendo = True

print("Hoje estou com as roupas " + ("secas.", "molhadas.")[esta_chovendo]) # primeria é False e segunda True
print('Hoje estou com as roupas ' + ( 'molhadas.' if esta_chovendo else 'secas.')) # outra opção, ambas podem ser com '' ou ""

#%%------------------------------
# Operador de Membro

lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista) # true, porque 2 está na lista
print('Ana' not in lista) # false, porque Ana está na lista

# Operador de Identidade

x = 3
y = x
z = 3

print(x is y) # true, porque valor de um foi atribuido ao outro
print(y is z) # true, porque tem mesmo valor
print(x is z) # true, TODOS são iguais pq tem mesmo valor
print(x is not z) # false

# Já com Lista (Array) é diferente. Valores podem ser iguais, mas não são armazenamos no mesmo local de memória.

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b) # true, porque um foi atribuido ao outro
print(lista_b is lista_c) # false, porque mesmo tendo mesmo conteúdo, são listas (arrays) diferrentes.

#%%------------------------------
print('--------------------- Buildins ----------------------')
# Buildins
# Funções como 'type', como 'print' vem do Buildins

print(__builtins__.type('Fala galera!!'))
print(__builtins__.type(1))
print(__builtins__.type(2.8))
print(__builtins__.type(True))
# print(__builtins__.help(__builtins__.dir)) # dir() mostra o que está presente no escopo global

# quando de cria uma variável, ela vai para o escopo global, e fica armazena do 'dir()'

dir(__builtins__) # mostra todas as funções, tipos, palavras que pertencem a linguagem (true, open, print, set, slice, super)

nome = 'João da Silva'
print(__builtins__.len(nome)) # length
