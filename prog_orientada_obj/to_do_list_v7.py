# !python
# Lista de coisas a fazer.

# Tratamento de Exceções.

from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception): # Exception é a Super Classe/Classe Pai das Exceções em Python.
    pass # ele vai usar por padrão as exceções nativas do próprio Python.

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__() # Agora o projeto passa a ser interado. "Se anda como Pato, e nada como Pato, então Pato é".

    # Sobrecarga do operador +=
    # projeto =+ tarefa
    def __iadd__(self, tarefa): # Esse método é para quando há sobrecarga de operador.
        tarefa.dono = self # O dono da tarefa será a instancia atual de projeto (self)
        self._add_tarefa(tarefa) # e dentro dele, eu adicionei a tarefa.
        return self

    def _add_tarefa(self, tarefa, **kwargs): # Método PRIVADO. O 'vencimento' estará dentro dos parâmentros variados (**kwargs).
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None))) # kwargs é um dicionário, uso 'get' para pegar o 'vencimento'.

    def add(self, tarefa, vencimento=None, **kwargs): # chama o método se o parametro 'tarefa', for uma instancia da classe 'Tarefa'.
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento # colocando o 'vencimento' dentro de 'kwargs'.
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito] # List Comprehention.
       
    def procurar(self, descricao):
        try: # aqui poderá dar um IndexError e cair na Exception para tratamento.
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0] # índice 0 para pegar o primeiro elemento encontrado com a descrição passada.
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e)) # o Erro será convertido para string - str()
    
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


class TarefaRecorrente(Tarefa): # Tarefa é a classe pai desta subclasse 'TarefaRecorrente'.
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento) # Aqui eu chamo o construtor da classe Pai, eu referencio a classe PAI ou a Super Classe.
        self.dias = dias
        self.dono = None

    def concluir(self): # ele quer complementar o método 'concluir()', pegando a funcionalidade já existe lá, e adicionar + aqui.
        super().concluir() # aqui com o SUPER, ele chama o método da SUPER Classe(Pai).
        novo_vencimento = datetime.now() + timedelta(days=self.dias) # comportamento adicionado ao método Concluir()
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono: # se o 'dono' da tarefa está 'settado', configurado.
            self.dono += nova_tarefa # Sobrecarga de operadores.
        return nova_tarefa

def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Lavar o banheiro')
    casa.add('Limpar o quarto', datetime.now() + timedelta(days=3, minutes=15))
    print(casa)

    casa.add(TarefaRecorrente('Trocar roupa de cama', datetime.now(), 7)) # Por causa das 2 funções ADD extras.    
    casa.add(casa.procurar('Trocar roupa de cama').concluir()) # Agora não precisa mais chamar assim 'casa.tarefas.append()'

    casa += TarefaRecorrente('Limpar fogao', datetime.now(), 7) # Usando Sobrecarga de Operador += | Não mais 'casa.add(TarefaRecorrente())'
    casa.procurar('Limpar fogao').concluir() # Usando Sobrecarga de Operador += | Não mais 'casa.add(casa.procurar())'
    print(casa)

    try:
        casa.procurar('Limpar as paredes').concluir() # ERRO, não irá encontrar a tarefa.
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"') # A causa foi "list index out of range".
    finally:
        print('O bloco "finally" sempre será executado, mesmo com ERRO nas linhas acima.')

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
