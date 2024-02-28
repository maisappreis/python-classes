 #! python
 
# Agora usando o 'with'. Aqui já fica garantido que o arquivo será fechado posterioramente.
# Sendo desnecessário chamar o 'arquivo.close()'

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # esse '*' é para extrair os dados. É isso o operador spread ... em JS.


if arquivo.closed:
    print('Arquivo foi fechado!')
