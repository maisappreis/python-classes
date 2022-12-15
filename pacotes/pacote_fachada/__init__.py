
# um Pacote fachada serve para expor todas as funcionalidades presentes dentro da aplicação ou aquelas que se quer expor.
# permitindo a visualização de todas elas em um único arquivo.

from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao


__all__ = ['soma', 'subtracao']