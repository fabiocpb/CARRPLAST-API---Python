import mysql.connector

mydb = mysql.connector.connect(
     host="127.0.0.1",
     user = "root",
     password= 'root123',
     database="carrplast"
)

def atualizarTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total, id):

    val = (tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total, id)
    
    mycursor = mydb.cursor()

    sql = "UPDATE tear SET tempo_ligado = %s , tempo_parado = %s, total_de_paradas = %s, tempo_medio = %s, eficiencia_total = %s WHERE id = %s"

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "linha(s) afetada(s)")