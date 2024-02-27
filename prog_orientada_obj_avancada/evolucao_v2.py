# Em Python temos:
#   Método de Classe - classe como primeiro parâmetro (@classmethod)
#       decorator disponível no __builtins__ para transformar um método em método de classe
#   Método de Instância - 'self' como primeiro parâmetro, pois 'self' indica a instância atual.
#       decorator isponível no __builtins__ para transformar um método em método estático
#   Método Estático - nenhum parâmentro (@staticmethod) | É como se fosse um método qqr que poderia estar fora do bloco Class.

class Humano:
    especie = 'Homo Sapiens' # este atributo pertence a Classe. Ele irá para as Instâncias/Objetos apenas se passado no construtor: def __init__(self)

    def __init__(self, nome): # aqui este atributo pertence a Instância/Objeto instânciado.
        self.nome = nome

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
    # HomoSapiens.das_cavernas(jose)

    grokn = Neanderthal('Grokn')
    print(f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}') # mesmo resultado.
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}') # mesmo resultado.
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}') # True
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}') # False
    print(f'Jose evoluido? {jose.is_evoluido()}') # True
    print(f'Grokn evoluido? {grokn.is_evoluido()}') # False