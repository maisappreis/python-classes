
# Usando o método recursivo, ou seja, é ele chamando ele mesmo.
# Mas isso não pode ser por tempo indeterminado, porque ai fica num looping infinito.

#%%

def imprimir(maximo, atual):
    if atual >= maximo: # condição de parada
        return # aqui ele não retorna nada, e intenção é apenas sair da função
    print(atual)
    imprimir(maximo, atual + 1) # aqui é onde a função se auto chama, e ela ficará se auto chamando até alcançar a variável 'maximo' colocada ali.


imprimir(10, 1)


#%%
# Outra mandeira

def imprimir2(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir2(maximo, atual + 1)


imprimir2(5, 1)