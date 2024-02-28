 #! python
 
# Agora abrindo o arquivo no modo escrita, e não apenas leitura.

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida: # o segundo parâmentro aqui é o modo, 'w' de 'write', escrita.
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida) # escolhendo uma outra saída, que não de fato um print no console.
                                                                     # e então ele cria um arquivo .txt


if arquivo.closed:
    print('Arquivo foi fechado!')
