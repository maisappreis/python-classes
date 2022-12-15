from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
args = (3, 5)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall() # Caso sejam muuitos, esse fetchall() pode gerar problemas de desempenho.
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} -  {contato[0]:10s} Telefone: {contato[1]}')