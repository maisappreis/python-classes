MAIOR_IDADE = 18 # Não existe constante em Python, MAS as variáveis que se comportam como CONSTANTES devem estar em letras maiusculas.


class Pessoa:
    def __init__(self, nome, idade): # construtor da classe.
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade: # se a idade não estiver settada.
            return self.nome
        return f'{self.nome} - {self.idade} anos'
    
    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE # se idade não estiver settada(for FALSE), vai pegar o 0. E 0 não é maior que 18, então FALSE. Is Adulto False.
