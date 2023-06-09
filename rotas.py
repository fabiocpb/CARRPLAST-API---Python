from flask import Flask, jsonify, request
from flask_cors import CORS
import database
import tabelas
import inserir
import consultar
import editar
import deletar

app = Flask(__name__)

CORS(app)

database.criarBanco()
tabelas.criarTabela()

tipos_de_defeitos = ['Quebra de Urdume', 'Quebra de Trama', 'Fim de trama']

# Consultar(todos)
@app.route('/teares',methods=['GET'])
def consultarTeares():
    return consultar.obter_teares()
   

# Consultar(id)
@app.route('/teares/<int:id>',methods=['GET'])
def consultarPorID(id):
    return consultar.obter_ultimo_tear(id)
    #return jsonify(teares[len(teares)- 1])

# Editar
@app.route('/teares/<int:id>',methods=['PUT'])
def editarTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total, id):
    editar.atualizarTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total, id)

@app.route('/teste/', methods=['POST'])
def rotaTeste():
    return print(request.accept_languages)

# Criar
@app.route('/teares/criar/' ,methods=['POST'])
def inserirDadosTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total):
    inserir.inserirDadosTear(tempo_ligado, tempo_parado, total_de_paradas, tempo_medio, eficiencia_total)

#Erros
@app.route('/teares/erros/<tipo>/<tempo_parado>/<total_de_paradas>/<tempo_em_paradas>/<menor_tempo>/<maior_tempo>/<tempo_medio>/<eficiencia_perdida>',methods=['POST'])
def inserirErrosTear(tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida):
    inserir.inserirErrosTear(tipo, tempo_parado, total_de_paradas, tempo_em_paradas, menor_tempo, maior_tempo, tempo_medio, eficiencia_perdida)
    
# Excluir
@app.route('/teares/<int:id>',methods=['DELETE'])
def excluir_tear(id):
    deletar.removerTear(id)