# !python
# Lista de coisas a fazer.


from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__() # Agora o projeto passa a ser interado. "Se anda como Pato, e nada como Pato, então Pato é".

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito] # List Comprehention.

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0] # índice 0 para pegar o primeiro elemento encontrado com a descrição passada.
    
    def __str__(self):
        return f'{self.nome}: {len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao, vencimento=None): # construtor.
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento
    
    def concluir(self):
        self.feito = True

    def __str__(self): # método mágico nativo no Python.
        status = []
        if self.feito:
            status.append('- Concluida')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('- Vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'- Vence em {dias} dias')
    
        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Lavar o banheiro')
    casa.add('Limpar o quarto', datetime.now() + timedelta(days=3, minutes=15))
    print(casa)

    casa.procurar('Lavar o banheiro').concluir()
    for tarefa in casa: # Por causa do __iter__(), não precisa mais chamar a tarefa 'casa.tarefas:' ELE INTEIROU AS TAREFAS.
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Lista de Compras')
    mercado.add('Frutas')
    mercado.add('Arroz', datetime.now())
    mercado.add('Queijo', datetime.now() + timedelta(days=5))
    print(mercado)
    
    comprar_frutas = mercado.procurar('Frutas')
    comprar_frutas.concluir()
    for tarefa in mercado: # Por causa do __iter__(), não precisa mais chamar a tarefa 'mercado.tarefas:' ELE INTEIROU AS TAREFAS.
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
