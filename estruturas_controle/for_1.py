

for i in range(1, 11): # isso é, de 1 a 10
    print('i = {}'.format(i))


for j in range(10): # no caso aqui, vai iniciar em 0 e acabar em 9 (10 repets)
    print(f'i = {j}')


for x in range(1, 11):
    for y in (range(1, 11)):
        print(f'{x} * {y} = {x * y}')