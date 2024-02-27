
# Generator com List Comprehension

# Ele é um gerador de número, e consome menos memória que o List Comprehension.
# Porque o Generator vai gerando sob demanda, e o List Comprehension já gera completo.
# Isso deve ser considerado em caso de listas muito grandes.


# É uma função que possui retornos parciais (yield), de uma iteração, e que podem ser iteradas
# através da função next do __builtins__ até ser totalmente consumida, quando levantam uma exceção,
# ainda é possível consumir através de qualquer construção em Python que trabalhe com iteráveis
# (como no FOR, List Comprehension, etc), e neste caso o tratamento da exceção é automático.


# (expressão for item in list if condicional)

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) # A partir daqui gerará ERRO!


print('generator:', generator) # <generator object <genexpr> at 0x000002256A03ABA0>
# Retorna um objeto Generator
