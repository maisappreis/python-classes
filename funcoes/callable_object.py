
# Objeto Chamável - Callable Object.

class Potencia:
    def __init__(self, expoente): # chamando o CONSTRUTOR do Python.
        self.expoente = expoente


    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2) # Aqui foi passado os EXPOENTES, usa a função "__init__()"
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}') 
        print(f'5³ => {cubo(5)}') # dentro destas 2 funções estou passando a BASE, usa a função "__call__()"
        print(Potencia(4)(2)) # aqui passe EXPOENTE e BASE.


# Isso é um OBJETO funcionando como se fosse uma FUNÇÃO.