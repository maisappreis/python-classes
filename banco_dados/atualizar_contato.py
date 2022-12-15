from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Jojo Silva', 13)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterado(s).')