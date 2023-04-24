import mysql.connector
import dbconnector

db = dbconnector.dbtabelas

mycursor = db.cursor()


def removerTear(id):

    try:

        sql = "DELETE FROM tear WHERE id = %s"

        mycursor.execute(sql, id)

        db.commit()

    except:
        print("Algum erro ocorreu.")

    else:
        return print(f"{id} removido com sucesso.")