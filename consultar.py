import mysql.connector

# sql é o statement de inserir e val é o valor a ser inserido
#exemplo : sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")

db = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password= 'root123',
        database="carrplast"
    )

mycursor = db.cursor()

def obter_teares():

    sql = "SELECT * FROM tear"

    mycursor.execute(sql)

    resultado = mycursor.fetchall()

    for x in resultado:
        return x


def obter_ultimo_tear(id):

    sql = "SELECT * FROM tear WHERE id = %s"

    mycursor.execute(sql, id)

    resultado = mycursor.fetchall()

    for x in resultado:
        return x
