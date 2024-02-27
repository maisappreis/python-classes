# Recursividade

# Funções recursivas (que chamam a si mesmas), sem condição de parada, tornam-se um loop infinito 
# e pararia em um erro de estouro de pilha de chamadas (stack overflow), ao consumir todo o espaço dedicado para
# tal fim. Em Python a exceção gerada e RecursionError com a mensagem maximum recursion depth exceeded.


#%%

def imprimir(maximo, atual):
    if atual >= maximo: # condição de parada
        return # aqui ele não retorna nada, a intenção é apenas sair da função
    print(atual)
    imprimir(maximo, atual + 1) # aqui é onde a função chama a si própria, e ela ficará se auto chamando até alcançar a variável 'maximo' colocada ali.


imprimir(10, 1)


#%%
# Outra mandeira

def imprimir2(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir2(maximo, atual + 1)


imprimir2(5, 1)