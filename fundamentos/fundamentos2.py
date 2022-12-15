#%%----------------------------------------------------------------
print('--------------------- Conversao de tipos ----------------------')
# Conversão de tipos
# Nem toda convesão é possível de ser feita, não dá pra transfomar uma frase tipo string em um número.

2 + 3 # 5
'2' + '3' # 23
# 2 + '3' # erro

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b)) # converteu string para número inteiro
print(str(a) + b) # converteu número para string

#%%----------------------------------------------------------------
print('--------------------- Coercao Automatica ----------------------')
# Coerção Automática
# São conversões implicitas, feitas pelo Python

print(type(10 / 2)) # Float - resulta em 5, mas fica do tipo 'float', toda divisão resulta número float
print(type(10 // 3)) # Int
print(type(10 // 3.3)) # Float

#%%------------------------------
print('--------------------- Tipos Numericos ----------------------')
# Tipos Numéricos

dir(int) #mostra tudo que tem dentro de 'int' para ser usado.
dir(float)

a = 5
b = 2.5

print(b.is_integer()) # false
print(5.0.is_integer()) # true, é um float, porque tem ponto, mas é um inteiro pq as casas decimais estão zeradas.

dir(int)
print(int.__add__(2, 5)) # outra forma de somar.
print(int.__abs__(-3)) # de negativo passa a positivo.

# Decimal

print(1.1 + 2.2) # 3.30000000000003 - isso é sem usar o Decimal

from decimal import Decimal, getcontext
Decimal(1.1) + Decimal(2.2)

getcontext().prec = 2 # precisão de 2 casas decimais
print(Decimal(1.1) + Decimal(2.2))

dir(Decimal) # mostra tudo que há dentro da função

#%%------------------------------
print('--------------------- Tipo String ----------------------')
# Tipo String

dir(str)
nome = 'Maisa Pierini Preis'

print(nome[0])
# nome[0] = 'P' # erro, pois strings são imutáveis,

print("Marca d'agua")
print('Marca d\'agua')
print('Texto que precisam ter "aspas" dentro dele.')
print('Texto com quebras de \n..... linhas') # /t dá um tab

doc1 = """ Texto com multipla
    ..... linhas"""
doc2 = ''' Texto com multipla
    ..... linhas'''

print(doc1) # com aspas duplas
print(doc2) # com aspas simples

sobrenome = 'Pierini'

print(sobrenome[0])
print(sobrenome[5])
print(sobrenome[-3]) # contagem de tras para frente, inicia em -1 -2 -3 4 ....
print(sobrenome[:4]) # acessa intervalo de 0 a 3
print(sobrenome[4:]) # acessa intervalo de 4 até o final
print(sobrenome[-4:]) # acessa de tras pra frente
print(sobrenome[2:5]) # acessa de 2 a 4

numeros = '1234567890'
print(numeros[::]) # acessa tudo
print(numeros[::2]) # acessa um, pula, acessa outro, pula, de 2 em 2 (pegou números ímpares)
print(numeros[1::2]) # iniciou pelo um, pula, acessa outro, pula, de 2 em 2 (pegou números pares)
print(numeros[::-1]) # inverteu a string

frase = 'Python eh demais'
print('py' in frase) # false, porque tem diferenciação entre letra maiusculas e minusculas.
print('py' in frase.lower()) # true
print('dem' in frase) # true

print(len(frase)) # conta caracteres, isso inclui os espaços
print(frase.lower())
print(frase.upper())
print(frase.split()) # quebra a frase entre os espaços

dir(str)
# help(str.center) # ele diz exatamente o que faz a função centrer

w = '123'
q = ' da Silva'

print(w + q)
print(w.__add__(q)) # funcionalidade __add__
print(str.__add__(w, q))

print(len(w)) # desta forma é mais alto nível
print(w.__len__()) # funcionalidade __len__

print('1' in w)  # desta forma é mais alto nível
print(w.__contains__('1')) # funcionalidade __contains__

# essas funcionalidades existem, mas na prática, não são usadas.
# são chamados de 'metodos mágicos', é como as funções acontecem internamente.

#%%------------------------------
print('--------------------- Listas (arrays) ----------------------')
# Listas (arrays)
# é dinâmico, é heterogênio, pode mudar de tamanho, pode misturar string, number, boolean (assim como em JavaScript)

lista = []
print(type(lista)) # list

dir(lista)
# help(list) # mostra as informações

lista.append(1) # adiciona novos elementos na lista
lista.append(5)
lista.append([1, 8, 7])
print(lista)

nova_lista = ["Ana", 1, 3, "Bia"] # heterogênia, mas não é recomendado fazer isso como uma boa prática.
nova_lista.remove(3)
print(nova_lista)

nova_lista.reverse() # reverte a ordem
print(nova_lista) 

lista_2 = [1, 9, 'uva', 5, 'abacate', 5.54]

print(lista_2.index('uva')) # retorna o indice
print(lista_2[2])
print('uva' in lista_2) # true
print(lista_2[-1]) # pega o ultimo elemento

lista_3 = ['ana', 'rui', 'bia', 'liz', 'gabi', 'lia']

print(lista_3[1:3])
print(lista_3[1:-1]) # todos menos o primeiro e o ultimo
print(lista_3[1:]) # todos menos o primeiro
print(lista_3[:-1]) # todos menos o ultimo
print(lista_3[:]) # todos
print(lista_3[::2]) # pula um sim um não
print(lista_3[::-1]) # inverte

del lista_3[2]
print(lista_3)

#%%------------------------------
print('--------------------- Tuplas ----------------------')
# Tuplas
# Parece uma lista (array), mas a tupla não pode ser modificada. Não adiciona, não deleta, não modifica elementos.

tupla = tuple()
tupla = ()

print(type(tupla))
dir(tupla)
# help(tupla)

tupla = ('um') # tipo string
tupla = ('um', ) # tipo tuple
tupla[0] # também é uma estrutura indexada, pode-se acessar os indices dela

cores = ('verde', 'azul', 'amarelo', 'azul', 'preto', 'azul')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo')) # dá o index do elemento
print(cores.count('azul')) # conta elementos
print(len(cores)) # conta elementos

#%%------------------------------
print('--------------------- Dicionario (objeto) ----------------------')
# Dicionário (objeto)
# É parecido com um objeto de JavaScript, cada elemento possui chave e valor
# Mas em Pyhon, a chave também é escrita como uma string, ou seja, entre aspas. No JS a chave não vai entre aspas.

pessoa = {
    'nome': 'Ana',
    'idade': 38,
    'cursos': ['Ingles', 'Portugues']
}

print(type(pessoa)) # retorna 'dict' de dictionary
dir(dict)

print(len(pessoa)) # retorna quantidade de elementos
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.get('idade'))

pessoa['idade'] = 44 # alterando o valor de uma chave
pessoa['cursos'].append('Espanhol') # adicionado elementos
print(pessoa)

pessoa.pop('idade') # lê o valor e retira ele de dentro do dicionário
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'M'}) # adiciona elemento chave e valor
print(pessoa)

del pessoa['cursos'] # deleta elemento
pessoa.clear() # limpa o dicionário por completo
print(pessoa)


#%%------------------------------
print('--------------------- Conjunto (Set) ----------------------')
# Conjunto (Set)
# É delimitado por chaves {}, mas possui apenas valores.
# Não tem uma ordenação, não é indexado, e não aceita repetição.

a = {1, 2, 3}
print(type(a)) # "set"

# a[0] # dá erro, não tem index

a = set('Maisa')
print(a) # não vem na ordem correta, SEM ORDENAÇÃO, e SEM REPETIÇÃO, veio apenas um 'a'.

print('M' in a, 5 not in a) # true, true
print({1, 2, 3} == {3, 2, 1, 3}) # true

# Operações de conjuntos

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2)) # cria um novo conjunto com a união dos 2
print(c1.intersection(c2)) # cria um novo conjunto com a intersecção dos 2

c1.update(c2) # cria um novo conjunto usando o c2 para atualizar o c1
print(c1) # {1, 2, 3}
print(c2) # {2, 3}

print(c2 <= c1) # true (c2 é subconjunto de c1), pq c2 = {2, 3} está contido em c1 = {1, 2, 3}
print(c1 >= c2) # true (c1 é superconjunto de c2), pq c2 está contido em c1

{1, 2, 3} - {2} # diferneça entre conjuntos, não existe a soma '+' entre 2 conjuntos.
print(c1 - c2) # diferença também

c1 -= {2} # diferença também
print(c1)

#%%------------------------------
print('--------------------- Interpolacao ----------------------')
# Interpolacao
# Formas de interpolar strings.

# Forma 1 - forma mais antiga e menos recomendada.
nome, idade = 'Maisa', 28
print('Nome: %s, Idade: %d' % (nome, idade)) # padrão %s para strings, e %d para números inteiros, e %f para números reais, e %r true e false.

produto, preco = 'Smartphone', 2354.54485
print('Produto: %s, Preco: %.2f' % (produto, preco)) # padrão %f para números reais(float), e ainda com arredondamento '.2'

# Forma 2 - antes do Python 3.6
print('Nome: {0}, Idade: {1}'.format(nome, idade))

# Forma 3 - após Python 3.6
print(f'Nome: {nome}, Idade: {idade}') # forma mais fácil e enxuta.

# Forma 4
from string import Template

funcionario, salario = 'Marcos Aurelio', 2350.44
a = Template('Funcionario: $f, Salario: $s')
print(a.substitute(f=funcionario, s=salario))

