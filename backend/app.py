from flask import Flask, render_template, request, jsonify
from busca import buscar_trecho
import os
import requests

from scraper.baixar_letras import executar_scraper
import spotify_token

# Caminhos relativos ao diretório atual (backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "..", "frontend", "static")
LETRAS_DIR = os.path.join(BASE_DIR, "..", "letras")
SPOTIFY_TOKEN = spotify_token.get_token()

"""
VIDEOS = {
    "vampire":"RlPNh_PBZb4?si=666UCJ6uB14zXRyP", #1
    "bad_idea_right":"Dj9qJsJTsjQ?si=rliq29h3xPkizh1t", #2
    "the_grudge": "Qt5wB7KXSaM?si=de7EAQrCbeLtli5I", #3
    "all-american_bitch": "Qt5wB7KXSaM?si=IxTi9MbCirAMQAZj", #4
    "good_4_u": "gNi_6U5Pm_o?si=4AvnjRyz9gQ90dNJ", #5
    "obsessed":"QXcjPySjdJU?si=dJbfTLI-8DKbT-82", #6
    "drivers_license": "ZmDBbnmKpqQ?si=r2pUsEBjdGdEYpum", #7
    "get_him_back" : "ZsJ-BHohXRI?si=5U0ppJDwJ0irMEbD", #8
    "love_is_embarrassing": "AXi213cWgYM?si=anp6i0U247d67tGS", #9
    "logical" : "I6OeAufKDBg?si=AJFzpg0UrwFTVNvV", #10
    "so_american" : "W-PGNyhmSKA?si=_X8YoeTHLce83mgm", #11
    "traitor" : "CRrf3h9vhp8?si=c6MMaX0jfbm1326P", #12
    "deja_vu" : "cii6ruuycQA?si=bA-MvaGxAXbkv9v7", #13
    "favorite_crime" : "AyX_LL9nWSE?si=Mx2sZerh7-2ETsU5", #14
    "cant_catch_me_now" : "GlM6lcFbLSg?si=XvBYQbgBbUTsI1uW", #15
}"""

TRACKS_SPOTIFY = {
    "vampire": "1kuGVB7EU95pJObxwvfwKS",
    "bad_idea_right": "3IX0yuEVvDbnqUwMBB3ouC",
    "the_grudge": "3Nl5OkkmS5DaBZvuYofpAt",
    "all-american_bitch": "34sOdxWu9FljH84UXdRwu1",
    "good_4_u": "4ZtFanR9U6ndgddUvNcjcG",
    "obsessed": "6tNgRQ0K2NYZ0Rb9l9DzL8",
    "drivers_license": "5wANPM4fQCJwkGd4rN57mH",
    "get_him_back": "2gyxAWHebV7xPYVxqoi86f",
    "love_is_embarrassing": "26QLJMK8G0M06sk7h7Fkse",
    "logical": "53dtP2iUMvaF28JZcHnFuU",
    "so_american": "5Jh1i0no3vJ9u4deXkb4aV",
    "traitor": "5CZ40GBx1sQ9agT82CLQCT",
    "deja_vu": "6HU7h9RYOaPRFeh0R3UeAr",
    "favorite_crime": "5JCoSi02qi3jJeHdZXMmR8",
    "cant_catch_me_now": "56xHMIfQPoe0prrSi3BGhf",
}

# TODO: Pegar álbuns
# TODO: Mudar para API dos videos (spotify?)
# TODO: Implementar cache dos resultados de busca

if not os.path.exists(LETRAS_DIR) or not os.listdir(LETRAS_DIR):
    print("📥 Diretório de letras vazio ou inexistente. Iniciando download..." )
    os.makedirs(LETRAS_DIR, exist_ok=True)
    executar_scraper(LETRAS_DIR)
else:
    print("✅ Diretório de letras encontrado e não está vazio.")

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


def buscar_info_spotify(track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return None

@app.route("/musica/<nome>")
def mostrar_musica(nome):
    caminho_musica = os.path.join(LETRAS_DIR, nome + ".txt")
    print(caminho_musica)
    if os.path.exists(caminho_musica):
        with open(caminho_musica, "r", encoding="utf-8") as arquivo:
            letra = arquivo.read()
            titulo = nome.replace("_", " ").title()
            #video_id = VIDEOS.get(nome)

            # 🔹 Busca info do Spotify se a música estiver no dicionário
            spotify_info = None
            track_id = TRACKS_SPOTIFY.get(nome)
            if track_id:
                spotify_info = buscar_info_spotify(track_id)

            return render_template(
                "musica.html",
                titulo=titulo,
                letra=letra,
                spotify=spotify_info,
                track_id=TRACKS_SPOTIFY.get(nome)
)
    else:
        return "Arquivo não encontrado", 404


if __name__ == "__main__":
    print("Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)