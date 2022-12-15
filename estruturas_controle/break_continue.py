
# o CONTINUE interrompe prematuramente a iteração, para ir para a próxima iteração.
# ele interronpe o FOR, e não o IF, pq ele está associado a repetição.


for x in range(1, 11):
    if x % 2 == 0:
        continue 
    print(x)


# Já o BREAK ele sai do laço.


for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('FIM!')
