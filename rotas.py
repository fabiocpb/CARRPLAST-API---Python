from flask import Flask, jsonify, request
from flask_cors import CORS
import database
import tabelas
import inserir
import consultar

app = Flask(__name__)

CORS(app)

database.criarBanco()
tabelas.criarTabela()

tipos_de_defeitos = ['Quebra de Urdume', 'Quebra de Trama', 'Fim de trama']

# Consultar(todos)
@app.route('/teares',methods=['GET'])
def consultar():
    return consultar.obter_teares()
   

# Consultar(id)
@app.route('/teares/last',methods=['GET'])
def consultar():
    return consultar.obter_ultimo_tear()
    #return jsonify(teares[len(teares)- 1])
# Editar
@app.route('/teares/<int:id>',methods=['PUT'])
def editar_tear_por_id(id):
    tear_alterado = request.get_json()
    for indice,tear in enumerate(teares):
        if tear.get('id') == id:
            teares[indice].update(tear_alterado)
            return jsonify(teares[indice])
# Criar
@app.route('/teares',methods=['POST'])
def incluir_novo_tear():
    novo_tear = request.get_json()
    teares.append(novo_tear)
    return jsonify(teares)
    
# Excluir
@app.route('/teares/<int:id>',methods=['DELETE'])
def excluir_tear(id):
    for indice, tear in enumerate(teares):
        if tear.get('id') == id:
            del teares[indice]

    return jsonify(teares)