import math

pi = math.pi
raio = input('Informe o raio: ') # quando digitado no terminal, ele vem como string, e dá erro.
area = pi * (float(raio) ** 2) # por isso, aqui a gente tranforma ele para número flutuante.

print('Área do circulo:', area)

print('Nome do modulo:', __name__) # __main__
print('Nome do pacote:', __package__) # None


# NO TERMINAL
# dentro de '>fundamentos_projetos'

# >python (esse comando entra no interpretador)
# >import area_circulo_v5 (importa o arquivo pelo nome)
# >Nome do modulo: area_circulo_v5