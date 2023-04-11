from flask import Flask, request

app = Flask(__name__)

app.route('/')

def nao_entre_em_panico():

    return 'Hello World'

