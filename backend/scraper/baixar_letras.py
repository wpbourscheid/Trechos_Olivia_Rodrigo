import requests
from bs4 import BeautifulSoup
import os
import time
import re

from scraper.utils import limpar_musicas

BASE_URL = "https://www.letras.mus.br"
ARTISTA_URL = f"{BASE_URL}/olivia-rodrigo/"
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#PASTA_SAIDA = os.path.join(BASE_DIR, "..", "..", "letras")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_SAIDA = os.path.join(BASE_DIR, "..","letras")

def executar_scraper(pasta_saida=PASTA_SAIDA):
    links = obter_links_musicas()
    print(f"🎶 {len(links)} músicas encontradas.")
    
    for url in links:
        try:
            baixar_letra(url, pasta_saida)
            time.sleep(1)  # pausa entre requisições
        except Exception as e:
            print(f"⚠️ Erro ao baixar {url}: {e}")

def obter_links_musicas():
    print("🔍 Coletando links das músicas...")
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resposta = requests.get(ARTISTA_URL, headers=headers)
    sopa = BeautifulSoup(resposta.text, "html.parser")

    links = []
    for a in sopa.find_all("a", href=True):
        href = a["href"]

        # Padrão: /olivia-rodrigo/nome-da-musica/
        if re.fullmatch(r"/olivia-rodrigo/[a-z0-9\-]+/", href):
            link_completo = BASE_URL + href
            print("🎵 Música encontrada:", link_completo)
            links.append(link_completo)

    return list(set(links))  # evita duplicatas


def limpar_nome(titulo):
    nome = titulo.lower().replace(" ", "_").replace("/", "-")
    limpar_musicas(PASTA_SAIDA)
    return ''.join(c for c in nome if c.isalnum() or c in ['_', '-'])

def baixar_letra(url, PASTA_SAIDA):
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, "html.parser")

    titulo = sopa.find("h1").text.strip()
    letra_div = sopa.find("div", class_="lyric-original")

    if letra_div:
        letra = letra_div.get_text(separator="\n").strip()
        nome_arquivo = limpar_nome(titulo) + ".txt"

        os.makedirs(PASTA_SAIDA, exist_ok=True)
        with open(os.path.join(PASTA_SAIDA, nome_arquivo), "w", encoding="utf-8") as f:
            f.write(letra)
        print(f"✅ Letra salva: {nome_arquivo}")
    else:
        print(f"⚠️ Letra não encontrada em: {url}")

def main():
    print("🚀 Iniciando o scraper de múltiplas letras...")
    links = obter_links_musicas()
    print(f"🎶 {len(links)} músicas encontradas.")

    for url in links:
        try:
            baixar_letra(url)
            time.sleep(1)  # pausa entre requisições
        except Exception as e:
            print(f"⚠️ Erro ao baixar {url}: {e}")


if __name__ == "__main__":
    print("🚀 Iniciando o scraper...")
    main()
