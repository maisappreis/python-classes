from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos LIMIT 10 OFFSET 10'


with nova_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql)
        
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())