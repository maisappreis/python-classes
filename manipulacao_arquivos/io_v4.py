 #! python
 
# Agora usando o 'try' e o 'finally', porque mesmo se der erro no 'try', ele ainda irá executar o 'finally'.

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # esse '*' é para extrair os dados. É isso o operador spread ... em JS.

finally:
    arquivo.close()  # o 'finally sempre será executado'. Isso garante que o arquivo seja fechado.


if arquivo.closed:
    print('Arquivo foi fechado!')   # mas se tiver erro no 'try', aquilo que vem abaixo do 'finally' não será executado,
                                    # apenas ele próprio será.
                                    # caso eu use o 'except IndexError: pass' abaixo do 'try', ai sim todo o resto
                                    # continua sendo executado.


# Aqui precisa fechar o arquivo após usar ele. E não antes.
