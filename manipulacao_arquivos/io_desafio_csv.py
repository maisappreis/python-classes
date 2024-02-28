 #! python

import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada: # ao invés de usar o arquivo .csv local, vamos pegar ele remotamente, pela URL.
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1') # alterando o encoding do arquivo. ISO 8859-1 e não UTF-8
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}') # imprimir a 9ª coluna, de índice 8 e a de índice 3.


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv') # usar o 'r' na frente para evitar que caracteres especiais sejam interpretados de forma errada.




# para dar quebra de linhas: print('\n')
# mas para de fato printar \n, fazer: print('\\n') ou (r'\n)