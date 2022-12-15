# !python
# Lista de coisas a fazer.

# Outro Método Mágico: __iter__() de interação.

from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__() # Agora o projeto passa a ser interado. "Se anda como Pato, e nada como Pato, então Pato é".

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito] # List Comprehention.

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0] # índice 0 para pegar o primeiro elemento encontrado com a descrição passada.
    
    def __str__(self):
        return f'{self.nome}: {len(self.pendentes())} tarefa(s) pendente(s)'


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
    casa = Projeto('Tarefas da Casa')
    casa.add('Lavar o banheiro')
    casa.add('Limpar o quarto')
    print(casa)

    casa.procurar('Lavar o banheiro').concluir()
    for tarefa in casa: # Por causa do __iter__(), não precisa mais chamar a tarefa 'casa.tarefas:' ELE INTEIROU AS TAREFAS.
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Lista de Compras')
    mercado.add('Frutas')
    mercado.add('Arroz')
    mercado.add('Queijo')
    print(mercado)
    
    comprar_frutas = mercado.procurar('Frutas')
    comprar_frutas.concluir()
    for tarefa in mercado: # Por causa do __iter__(), não precisa mais chamar a tarefa 'mercado.tarefas:' ELE INTEIROU AS TAREFAS.
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
