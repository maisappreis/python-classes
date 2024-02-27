
# Classe Abstrata
# Usando 'ABCMeta' e '@abstractproperty'
# ABC: Abstract Base Class
# abstractproperty: decorator disponível no módulo abc para transformar uma propriedade em abstrata;

from abc import ABCMeta, abstractproperty


class Humano(metaclass=ABCMeta): # Isso faz com que a classe Humano passe a ser uma CLASSE ABSTRATA.
    especie = 'Homo Sapiens' # este atributo pertence a Classe. Ele irá para as Instâncias/Objetos apenas se passado no construtor: def __init__(self)

    def __init__(self, nome): # aqui este atributo pertence a Instância/Objeto instânciado.
        self.nome = nome
        self._idade = None # atributo privado.

    @abstractproperty
    def inteligente(self): # ABSTRATO, não se sabe dizer ao certo se é verdadeiro ou falso. Será um Método Não Implementado.
        pass

    @property
    def idade(self): # lê/pega um dado (GET). Nessa situação pode ter o mesmo nome.
        return self._idade

    @idade.setter
    def idade(self, idade): # altera/configura um dado (SET). Validação. Nessa situação pode ter o mesmo nome.
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

    def das_cavernas(self): # atributo de Instância/Objeto.
        self.especie = 'Homo Neanderthalensis' # aqui tmb é 'especie', este atributo prevalece em relação ao atributo de Classe.
        return self # consigo encadear a chamada do método das_cavernas()

    @staticmethod
    def especies(): #   Método Estático
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(classe): # esse parâmentro classe aqui se refere as 2 classes ali abaixo. Neanderthal, HomoSapiens e Humano tmb.
        return classe.especie == classe.especies()[-1] # se for a última espécie, é um ser evoluido.


class Neanderthal(Humano):
    especie = Humano.especies()[-2] # o penúltimo

    @property
    def inteligente(self): # Aqui é necessário resolver o método não implementado na classe Pai.
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1] # o último

    @property
    def inteligente(self): # Aqui é necessário resolver o método não implementado na classe Pai.
        return True


if __name__ == '__main__':
    
    try:
        anonimo = Humano('John Doe')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe Abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {} - Inteligente: {}'
        .format(jose.nome, jose.__class__.__name__, jose.inteligente))

    grogn = Neanderthal('Grogn')
    print('{} da classe {} - Inteligente: {}'
        .format(grogn.nome, grogn.__class__.__name__, grogn.inteligente))