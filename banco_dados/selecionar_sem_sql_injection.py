
# SQL Injection é um tipo de ataque onde alguém injeta linguagem SQL dentro de um formulario
# Podendo comprometer um banco de dados inteiro.

from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome LIKE %s"


with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )

    cursor = conexao.cursor()
    cursor.execute(sql, args) # fazendo isso, a biblioteca te protege do SQL Injection.
        
    for x in cursor:
        print(x)