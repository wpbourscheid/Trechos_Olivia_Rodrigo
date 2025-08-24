from flask import Flask, render_template, request, jsonify
from busca import buscar_trecho
import os

# Caminhos relativos ao diretório atual (backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "..", "frontend", "static")
LETRAS_DIR = os.path.join(BASE_DIR, "..", "letras")

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

@app.route("/musica/<nome>")
def mostrar_musica(nome):
    caminho_musica = os.path.join(LETRAS_DIR, nome + ".txt")
    print(caminho_musica)
    if os.path.exists(caminho_musica):
        with open(caminho_musica, "r", encoding="utf-8") as arquivo:
            letra = arquivo.read()
            titulo = nome.replace("_"," ").title()
            print("➡️ Procurando arquivo:", caminho_musica)
        return render_template("musica.html", titulo=titulo, letra=letra)
    else:
        return "Arquivo não encontrado", 404
    

if __name__ == "__main__":
    print("Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)
