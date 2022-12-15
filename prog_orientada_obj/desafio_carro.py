
class Carro:
    def __init__(self, velocidade_maxima): # este é o construtor.
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        velocidade_atual = self.velocidade_atual
        velocidade_maxima  = self.velocidade_maxima        
        if velocidade_atual + delta <= velocidade_maxima:
            self.velocidade_atual += delta
            return self.velocidade_atual
        else:
            self.velocidade_atual  = velocidade_maxima
            return self.velocidade_atual

    def frear(self, delta=5):
        velocidade_atual = self.velocidade_atual
        if velocidade_atual >= delta:
            self.velocidade_atual -= delta
            return self.velocidade_atual
        else:
            return 0



if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))