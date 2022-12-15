
# Mixins para Herança Multipla: Classes que surgem da mistura de outras classes.


class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<string>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa): # Classes que surgem da mistura de outras classes.
    pass


class AnimalHtml(HtmlToStringMixin, Animal): # A ordem aqui é importante, primeiro a Classe que se quer que se prevaleça.
    pass


if __name__ == '__main__':
    p1 = Pessoa('Maria Eduarda')
    print(p1) # Maria Eduarda

    p2 = PessoaHtml('Roberto Carlos')
    print(p2) # <span>Roberto Carlos</span>

    toto = AnimalHtml('Toto')
    print(toto) # <span>Toto <string>(pet)</strong></span>
