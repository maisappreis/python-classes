
# Classe Abstrata
# É o contrário de uma Classe Concreta, que tem todos os seus métodos implementados, com comportamento.
# Na Classe Abstrata pode-se ter métodos sem implementação. Python não tem isso de forma nativa.
# Por exemplo, o método fica sem implementação na Classe Pai/Super Classe.
# Mas o método deve ser implementado/resolvido na Classe Filho/Subclasse.


class Humano:
    especie = 'Homo Sapiens' # este atributo pertence a Classe. Ele irá para as Instâncias/Objetos apenas se passado no construtor: def __init__(self)

    def __init__(self, nome): # aqui este atributo pertence a Instância/Objeto instânciado.
        self.nome = nome
        self._idade = None # atributo privado.

    @property
    def inteligente(self): # ABSTRATO, não se sabe dizer ao certo se é verdadeiro ou falso. Será um Método Não Implementado.
        raise NotImplementedError('Propriedade não implementada.')

    @property
    def idade(self): # lê/pega um dado. Nessa situação pode ter o mesmo nome.
        return self._idade

    @idade.setter
    def idade(self, idade): # altera/configura um dado. Validação. Nessa situação pode ter o mesmo nome.
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

    def das_cavernas(self): # atributo de Instância/Objeto.
        self.especie = 'Homo Neanderthalensis' # aqui tmb é 'especie', este atributo prevalece em relação ao atributo de Classe da linha 3.
        return self # dai consigo encadear a chamada do método na linha 15.

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
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('Classe Abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {} - Inteligente: {}'
        .format(jose.nome, jose.__class__.__name__, jose.inteligente))

    grogn = Neanderthal('Grogn')
    print('{} da classe {} - Inteligente: {}'
        .format(grogn.nome, grogn.__class__.__name__, grogn.inteligente))