 #! python

# Usando um arquivo Comma Separated Values, valores separados por vírgula.
# Neste caso aqui, ele carrega todo o arquivo para dentro da variavel 'dados'.

arquivo = open('pessoas.csv')    # abre o arquivo, isso usa recursos do Sistema Operacional. Aloca recursos.
dados = arquivo.read()           # lê o arquivo e armazena os dados dentro de uma variavel. 
arquivo.close()                  # fecha o arquivo para que não fique usando recursos do Sistema Operacional.

# Como aqui o arquivo ficou salvo na variável 'dados',
# então eu já posso fechar ele antes de percorrer com o FOR e extrair os dados.

for registro in dados.splitlines(): # quebra em linhas.
    print('Nome: {}, Idade: {}'.format(*registro.split(','))) # esse '*' é para extrair os dados. É tipo o operador spread ... em JS.


