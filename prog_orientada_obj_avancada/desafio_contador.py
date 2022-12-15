
# Desafio

class ClasseSimples:
    contador = 0 # essa variável pertence à classe, e não as instâncias dela.

    def __init__(self):
        self.contar()   # isso tmb funcionaria: self.__class__.contador += 1

    @classmethod
    def contar(classe):   
        classe.contador += 1 # variável da Classe 'contador' está sendo manipulada por um Método de Classe.


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)