
class Humano:
    especie = 'Homo Sapiens' # este atributo pertence a Classe. Ele irá para as Instâncias/Objetos apenas se passado no construtor: def __init__(self)

    def __init__(self, nome): # aqui este atributo pertence a Instância/Objeto instânciado.
        self.nome = nome

    def das_cavernas(self): # atributo de Instância/Objeto.
        self.especie = 'Homo Neanderthalensis' # aqui tmb é 'especie', este atributo prevalece em relação ao atributo de Classe da linha 3.
        return self # dai consigo encadear a chamada do método na linha 15.


if __name__ == '__main__':
    jose = Humano('Jose')
    grokn = Humano('Grokn').das_cavernas() # determinei que o Grokn é homem das cavernas, com o método 'das_cavernas()'.
  # Humano.das_cavernas(grokn) # também funciona.

    print(f'Humano.especie: {Humano.especie}') # acessou atributo de Classe.
    print(f'jose.especie: {jose.especie}') # acessou atributo de Classe.
    print(f'grokn.especie: {grokn.especie}') # acessou atributo de Instância, porque nele foi chamado o método 'das_cavernas()'.