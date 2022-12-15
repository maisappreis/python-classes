
# Membros Instância vs Estáticos
# Alguns atributos podem ser estáticos, isto é, estarão presentes apenas na Classe Pai (Super Classe)
# Este atributo são estará presente nas instâncias (filhos daquela classe)

# d1 = Data(2, 6)
# d1.dia = 10      --> modificação feita a partir da instância/objeto.
# d1.metodo()

# Data.ano = 2022  --> modificação feita diretamente na Classe (estático).
# Data.metodo()    --> Metodo estático.

# Em Python temos:
#   Método de Classe - classe como primeiro parâmetro (@classmethod)
#   Método de Instância - 'self' como primeiro parâmetro, pois 'self' indica a instância atual.
#   Método Estático - nenhum parâmentro (@staticmethod) | É como se fosse um método qqr que poderia estar fora do bloco Class.

# Propriedades
# Atributos que precisam de validações, é muito comum usar Get and Set.
# Não mais usando Get and Set, mas sim o decorator @property e @nome.setter

# Classe Abstrata
# É o contrário de uma Classe Concreta, que tem todos os seus métodos implementados, com comportamento.
# Na Classe Abstrata pode-se ter métodos sem implementação. Python não tem isso de forma nativa.
# Por exemplo, o método fica sem implementação na Classe Pai/Super Classe.
# Mas o método deve ser implementado/resolvido na Classe Filho/Subclasse.
# Outra alternativa é usando 'ABCMeta' e '@abstractproperty'.

# Herança Multipla.
# Quando uma Classe Filho/Subclasse hera atributos de outras classes Pai, de mais de uma.
# Exemplo aqui: Homem Aranha, porque herda atributos da classe Homem e da classe Aranhã, as quais ambas herdam da classe Animal.
# Mixins para Herança Multipla: Classes que surgem da mistura de outras classes.

# Iterator 
# Faz a iteração: processo de resolução de uma equação mediante operações em que
# sucessivamente o objeto de cada uma é o resultado da que a precede.