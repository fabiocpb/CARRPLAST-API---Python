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

def inserirDadosTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total):

    val = (tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total)

    sql = "INSERT INTO tear (tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total) VALUES (%s, %s, %s, %s, %s)"

    mycursor.execute(sql, val)

    db.commit()

    

def inserirErrosTear(tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida):

    val = (tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida)

    sql_erro = "INSERT INTO erros (tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql_erro, val)

    db.commit()
