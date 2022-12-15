
# Lazy Evaluation: avaliação tardia.
# Deixar o processamento para quando for realmente necessário. Como no generator, que gera conforme demanda.
# Usando o Generator da V1 com o FOR.

from lazy_evaluat_generators_v1 import cores_arco_iris

if __name__ == '__main__':
    generator = cores_arco_iris()
    for cor in generator: # Usando o Lazy Evaluation: ele vai avaliando cada um, a partir que vai chamando o next.
        print(cor)
    print('Fim!')