 #! python

# Usando um arquivo comma-separated values, valores separados por vírgula.
# Neste caso aqui, ele carrega todo o arquivo para dentro da variavel 'dados'.

arquivo = open('pessoas.csv')    # aqui ele lê o arquivo. Isso usa recursos do Sistema Operacional. Aloca recursos.
dados = arquivo.read()           # armazena o arquivo dentro de uma variavel. 
arquivo.close()                  # fecho o arquivo para que não fique usando recursos do Sistema Operacional.

for registro in dados.splitlines(): # quebra em linhas.
    print('Nome: {}, Idade: {}'.format(*registro.split(','))) # esse '*' é para extrair os dados. É isso o operador spread ... em JS.


# Como aqui o arquivo ficou salvo na variável 'dados', então eu já posso fechar ele antes de percorrer com o FOR e extrair os dados.