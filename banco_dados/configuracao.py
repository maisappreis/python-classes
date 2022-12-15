from mysql.connector import connect

conecao = connect(
    user='root',
    passwd='12345678',
    port=3306,
    host='localhost'
)

print(conecao)