from .pessoa import Pessoa # import relativo usando o ponto.


def get_data(compra): # aqui 'data' está em Português, não é 'dados', é 'data' mesmo.
    return compra.data


class Cliente(Pessoa): # Cliente hera de Pessoa, pq Pessoa é a Classe Pai/Super Classe, e Cliente é filho/subclasse.
    def __init__(self, nome, idade): # Constructor.
        super().__init__(nome, idade) # Classe Filho precisa chamar o Super para herdar.
        self.compras = [] # lista de compras do cliente.
    
    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data # a função 'get_data' foi usada como chave(key) de ORDENAÇÃO das compras.

        # key=lamba compra: compra:data
        # função anônima que poderia ser usada.
        
    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total