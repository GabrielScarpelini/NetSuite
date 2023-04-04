from flask import Flask, jsonify, request


app = Flask(__name__) 

database = {
    'ALUNO': [{'id': 1, 'nome': 'Gabriel'},
                {'id': 2, 'nome': 'Mike'},
                {'id': 3, 'nome': 'Bruno'}],
    
    'PROFESSOR': [{'id' : 1, 'nome': 'Rogerio' },
                 {'id' : 2, 'nome': 'Andreia' },
                 {'id' : 3, 'nome': 'Rodolfo'}]
}


@app.route("/")
def start():
    return f'Vamos aprender a integrar Requests e Flask'

@app.route('/show_all')
def getAll():
    return jsonify(database)

@app.route('/alunos')
def getAlunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def getTeacher():
    return jsonify(database['PROFESSOR'])

@app.route('/professores/<int:id_teacher>')
def getTeacherById(id_teacher):
    for i in database['PROFESSOR']:
        if i['id'] == id_teacher:
            return i
    return f'Id não encontrado'

@app.route('/professores/<string:nome>')
def getTeacherByName(nome):
    nome = nome[0].upper() + nome[1:]
    for i in database['PROFESSOR']:
        if i['nome'] == nome:
            return i
    return f'Professor não encontrado'

@app.route('/professores/post', methods =["POST"])
def postTeacher():
    novo_teacher = request.json
    database['PROFESSOR'].append(novo_teacher)
    return jsonify(database['PROFESSOR'])

@app.route('/professores/put/<int:id_teacher>', methods =["PUT"])
def changeTeacher(id_teacher):
    novo_teacher = request.json
    for teacher in database['PROFESSOR']:
        if teacher['id'] == id_teacher:
            database['PROFESSOR'].remove(teacher)
            database['PROFESSOR'].append(novo_teacher)
            return jsonify(database['PROFESSOR'])
    return 'Professor Não Encontrado', 404



@app.route('/alunoss', methods =['POST'])
def inserir_aluno():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route('/aluno/<int:id_aluno>', methods=['PUT']) #put ele altera um que já existe 
def atualizar(id_aluno):
    atualiza_aluno = request.get_json()
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            database['ALUNO'].append(atualiza_aluno)
            return jsonify(database['ALUNO'])
    return 'Aluno não encontrado', 404



if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)