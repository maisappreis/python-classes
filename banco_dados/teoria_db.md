
# Anotações sobre MySQL


## MySQLConnection

> O objeto de conexão retornado pelo connect(**parametros) é uma instância da classe MySQLConnection.
> MySQLConnection.cursor(), método que retorna um “cursor” para ler e executar comandos no
    servidor do banco de dados, este objeto é uma instância da classe MySQLCursor.
> MySQLConnection.commit(), método que confirma as alterações feitas e as aplica no servidor,
    sem ele os dados não serão gravados.
> MySQLConnection.close() finaliza a conexão com o servidor, liberando recursos, em um script pode não ser tão essencial
    já que este método é chamado assim que o objeto é destruído (se a conexão ainda estiver ativa).


## MySQLCursor

> MySQLCursor.execute(), método que envia um comando SQL para ser executado no servidor.
> MySQLCursor.lastrowid, propriedade que retorna o último id gerado no “cursor”.
> MySQLCursor.executemany(), método que executa o script passado vários dados para dar INSERT na tabela.
    cursor.execute(sql, args)
    cursor.executemany(sql, contatos)

    - Primeiro parâmetro do método 'execute' é um comando SQL
    - Segunto parâmetro do método 'execute' são dados a serem inseridos, é essencial para evitar SQL Injection,
        pricipalmente se forem dados inseridos pelo usuário

> MySQLCursor.rowcount, propriedade que retorna o número de registros afetados pela última execução.
> MySQLCursor.fetchall(), método que carrega todos os registros disponíveis e retorna uma lista.
> MySQLCursor.fetchone(), método que carrega o próximo registro indicado no “cursor”, deixando-o pronto para a próxima solicitação.
> No package mysql.connector, o método cursor(), aceita um parâmetro nomeado Dictionary, sendo passado um argumento
    verdadeiro (True), muda o resultado da execução para uma lista de dicionários, ao invés de lista de listas.
> MySQLCursor.close() finaliza o “cursor”, liberando recursos. Este também é chamado assim
    que o objeto é destruído (e o “cursor” ainda esteja ativo)


# Anotações sobre SQLite

> Biblioteca em C que implementa um motor de banco de dados leve, rápido, alto
    contido, compatível com SQL ANSI e pode ser embutido nas mais diversas aplicações
> Foi incorporada a biblioteca padrão Python a partir da versão 2.5.