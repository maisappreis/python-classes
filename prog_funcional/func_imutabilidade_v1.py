from functools import reduce
from operator import add

valores = [30, 10, 20, 70, 700] # Usando LISTA, que são objetos MUTAVEIS.

# funções SEM Mutabilidade - Paradigma Funcional.

print(sorted(valores))
print(min(valores)) # minimo - menor número da lista 
print(max(valores)) # maximo - maior número da lista 
print(sum(valores))
print(reduce(add, valores)) # mesma coisa que soma, da função 'sum'
print(list(reversed(valores))) # inverte lista. 


# funções COM Mutabilidade - Paradigma Orientado a Objeto.

valores.sort()
print(valores)
valores.reverse()
print(valores)

