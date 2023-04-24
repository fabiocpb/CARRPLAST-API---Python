import mysql.connector

db = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password= 'root123',
        database="carrplast"
    )

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