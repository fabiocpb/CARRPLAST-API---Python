import mysql.connector

def criarTabela():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password= 'root123',
        database="carrplast"
    )

    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE [IF NOT EXISTS] tear (id int(3) primary key unique auto increment, tempo_ligado TIME(3), tempo_parado TIME(3), total_de_paradas int(3), tempo_medio TIME(3), eficiencia_total int(3))")

    mycursor.execute("CREATE TABLE [IF NOT EXISTS] erros (id int(3) primary key unique auto increment, tipo varchar(15), total_de_paradas int(3), tempo_em_paradas TIME(3), menor_tempo TIME(3), maior_tempo TIME(3), tempo_medio TIME(3), eficiencia_perdida int(3))")
