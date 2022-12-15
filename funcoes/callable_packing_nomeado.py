
def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)


def imposto_x(importado):
    return 0.22 if importado else 0.139


def imposto_y(carga_explosiva, fator_perigo=1):
    return 0.11 * fator_perigo if carga_explosiva else 0


if __name__ == "__main__":
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True) # True entrou em '*params' que entrou em 'importado'.
    preco_final = calc_preco_final(preco_final, imposto_y, carga_explosiva=True, fator_perigo=1.5) # True e 1.5 entraram em '*params' que entraram em 'carga_explosiva e fator_perigo'.
    print(f'Preco final R$ {preco_final}')


# funções sendo colocadas como parâmetros de outra função.
# 
