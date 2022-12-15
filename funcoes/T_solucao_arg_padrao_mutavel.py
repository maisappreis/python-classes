
# Tuplas são imutáveis.
# Listas são mutáveis.

# Por isso, se um parâmetro de função for uma LISTA, isso pode dar PROBLEMAS.
# Mutáveis como valor default(padrão) são uma armadilha.

# SOLUÇÃO:

def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1] # Se 'sequencia' for nulo, e é, então pega [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2]) # ultimo elemento, e penultimo.
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio)) # [0, 1, 1] - id é autogerado pelo Python.

    print(fibonacci(inicio)) # [0, 1, 1, 2]

    restart = fibonacci() # Esperamos que volte para a função de inicio, com 'return': [0, 1, 1]
    print(restart, id(restart)) # Agora ele retorna corretamente o inicio [0, 1, 1]


# Conclusão, Listas são mutáveis, e vão se alterando em cada linha de código. Diferente das Tuplas.
# Uma das soluções seria substituir a LISTA por uma TIPLA.