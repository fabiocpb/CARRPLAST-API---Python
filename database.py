import dbconnector

def criarBanco():
    db = dbconnector.dbiniciar

    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS carrplast")

    #mycursor.execute("SHOW DATABASES")

    #for x in mycursor:
        #print(x)