
# Desafio do Maior Divisor Comum.
# O resto da divisão precisa ser 0. Módulo % igual a 0.
# Seria o menor número que pode dividir todos os números tendo o resto == 0.

def mdc(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1) # chamada recursiva.
    return calc(min(numeros)) # passando o menor dos números encontrados. Seria o primeiro candidato.


if __name__ == '__main__':
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 66, 3])) # 3
    print(mdc([7, 9])) # 1