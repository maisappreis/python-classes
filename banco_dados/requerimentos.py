#!python
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector não instalado!')
else:
    print('MySQL Conector instalado e pronto!')