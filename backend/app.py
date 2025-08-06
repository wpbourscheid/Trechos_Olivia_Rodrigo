from flask import Flask, render_template, request, jsonify
from busca import buscar_trecho
import os

# Caminhos relativos ao diretório atual (backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "..", "frontend", "static")

# Inicializando o Flask com caminhos personalizados
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    dados = request.get_json()
    trecho = dados.get("trecho", "")
    resultados = buscar_trecho(trecho)
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
