def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65): # o número 18 sim, mas o 65 aqui não faz parte do range (range é distância, intervalo entre um e outro)
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    idades = (17, 23, 54, 68, 103) # aqui é uma 'tuple'
    for idade in idades:  
        print(f'{idade}: {faixa_etaria(idade)}')


# outra opção > for idade in (17, 23, 54, 68, 103)