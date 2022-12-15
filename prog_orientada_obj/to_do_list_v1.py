# !python
# Lista de coisas a fazer.

from datetime import datetime


class Tarefa:
    def __init__(self, descricao): # construtor.
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.feito = True

    def __str__(self): # método mágico nativo no Python.
        return self.descricao + (': Concluida' if self.feito else '') # Para cair no IF, o 'self.feito' precisa returnar TRUE.


def main():
    casa = []
    casa.append(Tarefa('Passar as roupas'))
    casa.append(Tarefa('Lavar os pratos'))
    casa.append(Tarefa('Aspirar o chao'))

    # Versão do Prof. usando List Comprehension.
    
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar os pratos']
    for tarefa in casa:
        print(f'- {tarefa}')

    # Minha versão

    # for tarefa in casa:
    #     if tarefa.descricao == 'Lavar os pratos':
    #         tarefa.concluir()
    #     print(f'- {tarefa}')
    

if __name__ == '__main__':
    main()
