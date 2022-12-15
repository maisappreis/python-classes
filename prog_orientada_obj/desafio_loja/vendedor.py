from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario): # estes são os parâmentros de Vendedor.
        super().__init__(nome, idade) # os parâmetros do Super são os mesmos de Pessoa.
        self.salario = salario