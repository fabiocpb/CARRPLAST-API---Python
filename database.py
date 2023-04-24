import mysql.connector

def criarBanco():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password= 'root123'
    )

    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE [IF NOT EXISTS] carrplast")

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)