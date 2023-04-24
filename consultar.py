import dbconnector

# sql é o statement de inserir e val é o valor a ser inserido
#exemplo : sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")

db = dbconnector.dbtabelas

mycursor = db.cursor()

def obter_teares():
        
    try:

        sql = "SELECT * FROM tear"

        mycursor.execute(sql)

        resultado = mycursor.fetchall()

    except:
        print("Algum erro ocorreu.")

    else:
        print(resultado)
        return resultado


def obter_ultimo_tear(id):

    try:

        sql = "SELECT * FROM tear WHERE id = %s"

        mycursor.execute(sql, id)

        resultado = mycursor.fetchall()

    except:
        print("Algum erro ocorreu.")

    else:
        print(resultado)
        return resultado
