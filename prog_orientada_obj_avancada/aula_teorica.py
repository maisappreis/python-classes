
# Membros de Instância vs Estáticos

# Alguns atributos podem ser estáticos, isto é, estarão presentes apenas na Classe Pai (Super Classe)
# Este atributo não estará presente nas instâncias (filhos daquela classe)

class Data():
    pass

d1 = Data(2, 6)
d1.dia = 10      # modificação feita a partir da instância/objeto.
d1.metodo()

Data.ano = 2022  # modificação feita diretamente na Classe (estático).
Data.metodo()    # Metodo estático.


# Membros de classe × membros da instância

#   Método de Classe - classe como primeiro parâmetro (@classmethod)
#       decorator disponível no __builtins__ para transformar um método em método de classe
#   Método de Instância - 'self' como primeiro parâmetro, pois 'self' indica a instância atual.
#       decorator isponível no __builtins__ para transformar um método em método estático
#   Método Estático - nenhum parâmentro (@staticmethod) | É como se fosse um método qqr que poderia estar fora do bloco Class.


# Atributos setados dentro da classe diretamente (e não nos métodos), são membros de classe,
# e estão disponíveis diretamente através da classe e em todas as suas instâncias, a não ser que exista um
# membro de instância de mesmo nome.
# Ao setar um atributo através do objeto/instancia (self), o que criaremos será um membro de instância.
# Ao acessar um atributo em uma instancia e a mesma não possui-la, uma busca e feita em sua classe (incluindo toda a herança).
# Alterando o valor de um membro de classe “afeta” todas as instancias da mesma.


# Propriedades
# Atributos que precisam de validações, é muito comum usar Get and Set.
# Normalmente tem um getter e um setter, quando tem apenas um dos dois é read-only ou write-only respectivamente.
# Não mais usando Get and Set, mas sim o decorator @property e @nome.setter

# Classe Abstrata
# É o contrário de uma Classe Concreta, que tem todos os seus métodos implementados, com comportamento.
# Na Classe Abstrata pode-se ter métodos sem implementação. Python não tem isso de forma nativa.
# Por exemplo, o método fica sem implementação na Classe Pai/Super Classe.
# Mas o método deve ser implementado/resolvido na Classe Filho/Subclasse.
# Outra alternativa é usando 'ABCMeta' e '@abstractproperty'.
# É para atender a necessidade de marcar métodos como abstratos (que precisam
# ser definidas nas classes descendentes), que é atingida apenas levantando uma exceção
# NotImplementedError em qualquer tentativa de chamada.


# Herança Multipla.
# Quando uma Classe Filho/Subclasse herda atributos de outras classes, mais de uma.
# Exemplo aqui: Homem Aranha, porque herda atributos da classe Homem e da classe Aranhã, as quais ambas herdam da classe Animal.
# Mixins para Herança Multipla: Classes que surgem da mistura de outras classes.
# É como se uma classe recebesse outra classe como parâmetro. A classe que está no parâmetro é o pai.
# Exemplo: class TaskRecurring(Task):


# Iterator 
# Faz a iteração: processo de resolução de uma equação mediante operações em que
# sucessivamente o objeto de cada uma é o resultado da que a precede.