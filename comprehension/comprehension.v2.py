# Cria listas de uma forma muito mais concisa e rápida.
# Conciso é algo que está resumido ao essencial, que é sucinto e preciso.

# [ expressão for item in list if condicional ]

dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)

# com uma única linha cria-se uma lista.



# Versão SEM o List Comprehension: 

dobros_dos_pares2 = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares2.append(i * 2)
print(dobros_dos_pares2)