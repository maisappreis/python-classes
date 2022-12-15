
# Agora usando o Generator com o FOR.
# Ele é um gerador de número, e consome menos memória que o List Comprehension.
# Porque o Generator vai gerando sob demanda, e o List Comprehension já gera completo.
# Isso deve ser considerado em casa de listas muito grandes.

# [ expressão for item in list if condicional ]


generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
