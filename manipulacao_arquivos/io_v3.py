 #! python
 
# Agora usando o 'strip()' para retirar espaços em branco entre as linhas.

# Usando um arquivo Comma Separated Values, valores separados por vírgula.
# Nesse caso aqui, ele não precisa carregar o arquivo todo antes de proceguir, ele vai lendo o arquivo sob demanda.
# Seria uma leitura 'striming', como o Youtube faz, ele não carrega todo o video para seu PC. Ele vai carregando aos poucos.
# Isso economiza recurso de memória.

arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # esse '*' é para extrair os dados. É isso o operador spread ... em JS.
arquivo.close()


# Aqui precisa fechar o arquivo após usar ele. E não antes.
