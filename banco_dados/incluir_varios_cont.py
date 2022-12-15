from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES(%s, %s)'
args = (
    ('Ana', '99852-1475'),
    ('Bia', '99852-1475'),
    ('Pedro', '99852-1475'),
    ('Joana', '99852-1475'),
    ('Maisa', '99852-1475'),
    ('Gui', '99852-1475'),
    ('Jojo', '99852-1475'),
    ('Paula', '99852-1475'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Registros incluídos {cursor.rowcount} registros!')