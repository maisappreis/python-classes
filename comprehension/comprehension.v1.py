# List Comprehension

# Cria listas de uma forma muito mais concisa e rápida.
# Conciso é algo que está resumido ao essencial, que é sucinto e preciso.

# [ expressão for item in list ]

dobros = [i * 2 for i in range(10)]
print(dobros)

# com uma única linha cria-se uma lista.



# Versão SEM o List Comprehension: 

dobros2 = []
for i in range(10):
    dobros2.append(i * 2)
print(dobros2)