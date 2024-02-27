
# Herança Multipla.
# Quando uma Classe Filho/Subclasse herda atributos de outras classes, de mais de uma.
# Exemplo aqui: Homem Aranha, porque herda atributos da classe Homem e da classe Aranhã, as quais ambas herdam da classe Animal.


class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar') # Com o Super().capacidades, ele puxa as capacidades da Classe Pai, a classe Animal.


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha): # Herança Múltipla.
    @property
    def capacidades(self): # Aqui, 'super().capacidades' está puxando os atributos de Homem e de Aranha.
        return super().capacidades + \
            ('bater em bandidos', 'lançar teias')


if __name__ == '__main__':
    renan = Homem()
    print(f'Renan: {renan.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')