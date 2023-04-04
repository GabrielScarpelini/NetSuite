from flask import Flask


app = Flask(__name__) 

@app.route("/")
@app.route("/boasvindas")
def boas_vindas():
    return "Primeira Aula de Flask"

@app.route("/boanoite")
def boa_noite():
    return "Boa noite"


@app.route("/bomdia")
def bom_dia():
    return "Bom dia"

if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)