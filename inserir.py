import mysql.connector
import dbconnector

# sql é o statement de inserir e val é o valor a ser inserido
#exemplo : sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")

db = dbconnector.dbtabelas

mycursor = db.cursor()

def inserirDadosTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total):

    val = (tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total)

    try:

        sql = "INSERT INTO tear (tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total) VALUES (%s, %s, %s, %s, %s)"

        mycursor.execute(sql, val)

        db.commit()
    
    except:

        return print("Algum erro ocorreu.")
    
    else:

        return print("Dados inseridos com sucesso")

    

def inserirErrosTear(tearID, tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida):

    val = (tearID, tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida)

    try:

        sql_erro = "INSERT INTO erros (tearID, tipo, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        mycursor.execute(sql_erro, val)

        db.commit()
    
    except:

        return print("Algum erro ocorreu.")
    
    else:

         return print("Dados inseridos com sucesso")
