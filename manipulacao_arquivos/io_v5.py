 #! python
 
# Agora usando o 'with'. Aqui já fica garantido que o arquivo será fechado posterioramente.

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # esse '*' é para extrair os dados. É isso o operador spread ... em JS.


if arquivo.closed:
    print('Arquivo foi fechado!')  


# Aqui precisa fechar o arquivo após usar ele. E não antes.
