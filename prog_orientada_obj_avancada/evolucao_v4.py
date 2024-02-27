
# Propriedades
# Não mais usando Get and Set, mas sim o decorator @property e @nome.setter
# property: decorator disponível no __builtins__ para transformar um método em uma propriedade

class Humano:
    especie = 'Homo Sapiens' # este atributo pertence a Classe. Ele irá para as Instâncias/Objetos apenas se passado no construtor: def __init__(self)

    def __init__(self, nome): # aqui este atributo pertence a Instância/Objeto instânciado.
        self.nome = nome
        self._idade = None # atributo privado.

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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1] # o último

if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    jose.idade = 40  # acesso desta maneira por causa do decorator @property.
    print(f'Nome: {jose.nome} - Idade: {jose.idade}') # acesso desta maneira por causa do decorator @property.