# FOR
# Aplicando o FOR em intervalos com o range()

for i in range(1, 11): # intervalo de 1 a 10
    print('i = {}'.format(i))


for j in range(10): # intervalo de 0 a 9 - (10 repets)
    print(f'i = {j}')


for x in range(1, 11):
    for y in (range(1, 11)):
        print(f'{x} * {y} = {x * y}')