
# Classes são nomeadas com CamelCase
# todo método/função dentro de uma CLASSE precisa iniciar com 'self'.
# 'self' é o objeto que está sendo acessado naquele momento. Ele me parece ser tipo o 'this' em JavaScript.

class DataCriada:
    def __init__(self, dia, mes, ano): # o CONSTRUTOR.
        self.dia = dia # self representa o objeto atual, o 'dia' da direita é o parâmetro ali da linha de cima.
        self.mes = mes # e o 'dia' da esquerda é o objeto que está sendo criado.
        self.ano = ano

    def to_str(self): # todo método/função dentro de uma CLASSE precisa iniciar com 'self'.
        return f'{self.dia}/{self.mes}/{self.ano}'

# existe o método nativo do Python para substituir 'to_str', criado por mim, por '__str__' nativo.

d1 = DataCriada(5, 12, 2022) # Uma instância/objeto foi criado aqui. AQUI estou chamando o MÉTODO, o CONSTRUTOR da classe.
d1.dia = 29 # posso alrerar a data aqui
# d1.mes = 8
# d1.ano = 2022
print(d1.to_str())


d2 = DataCriada(30, 8, 2022) # Uma instância/objeto foi criado aqui.
# d2.dia = 23 # atributos podem ser criados fora da classe.
# d2.mes = 3
# d2.ano = 1994
print(d2.to_str())