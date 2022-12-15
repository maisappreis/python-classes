from random import randint


# for i in range(1, 11):
#     if i == 6:
#         break (com o 'break' aqui ele pula o 'else').
#     print(i)
# else:
#     print ('Fim')


# Jogar dado.



def sortear_dado():
    return randint(1, 6)

for numero_escolhido in range(1, 7):
    if numero_escolhido % 2 == 1:
       continue

    if sortear_dado() == numero_escolhido:
        print('Acertou!', numero_escolhido)
        break
else:
    print ('Nao acertou.')



