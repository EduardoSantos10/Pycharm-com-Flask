from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flask-ti20n-default-rtdb.firebaseio.com/" # conectar o banco de dados

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Principal")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        extrair = request.form.get("extrair")
        dados = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco, "extrair":extrair}
        requisicao = requests.post(f'{link}/cadastrar/.json', data = json.dumps(dados))
        return 'Cadastro com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n\ {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicitação dos dados
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'Algo deu errado \n\n\ {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicitar
        dicionario = requisicao.json()
        idCadastro = "" #Armazenar o ID individual de cada um
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == {'13579'}:
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n\n{e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {""}
        requisicao = requests.patch(f'{link}/cadastrar/-O8JiDnoFjBpS88K7HVy/.json', data=json.dumps(dados))
        dicionario = requisicao.json()
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n\n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-O8JiDnoFjBpS88K7HVy/.json')
        return "Excluir com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n\n {e}'

@app.route('/extrair')
def extrair():
    try:
        extrair = requests.get(f'{link}/listar/-O8no3w7jn9DWwYVFndo/.json')
        dicionario = extrair.json()
        idConsulta = " "
        for codigo in dicionario:
            chave = dicionario[codigo]['extrair']
            if chave == {'codigo'}:
                idConsulta = codigo
                return idConsulta
    except Exception as e:
        return f'Algo deu errado \n\n{e}'
