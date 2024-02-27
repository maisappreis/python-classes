
# CONTINUE e BREAK

# CONTINUE: pula para o próximo elemento do FOR
# BREAK: interrompe completamente o FOR, quebra o looping


for x in range(1, 11):
    if x % 2 == 0:
        continue 
    print(x)


for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('FIM!')
