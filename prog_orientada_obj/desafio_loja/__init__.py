
# FACHADA do PACOTE - Isso fará com que eles fiquem disponíveis dentro do pacote 'desafio_loja'.

from .cliente import Cliente
from .vendedor import Vendedor
from .compra import Compra


__all__ = ['Cliente', 'Vendedor', 'Compra']