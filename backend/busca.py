import os
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_LETRAS = os.path.join(BASE_DIR, "..", "letras")

def normalizar_texto(texto):
    # Remove acentos e coloca tudo em minúsculo
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto.lower().strip()

def buscar_trecho(trecho_busca):
    trecho_busca_norm = normalizar_texto(trecho_busca)
    resultados = []

# TODO: Permitir busca por nome da música além do trecho


    for nome_arquivo in os.listdir(PASTA_LETRAS):
        if not nome_arquivo.endswith(".txt"):
            continue
        
        caminho = os.path.join(PASTA_LETRAS, nome_arquivo)
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                linhas = f.readlines()
        except Exception as e:
            print(f"⚠️ Erro ao ler {nome_arquivo}: {e}")
            continue

        linhas_encontradas = []
        for linha in linhas:
            linha_norm = normalizar_texto(linha)
            if trecho_busca_norm in linha_norm:
                linhas_encontradas.append(linha.strip())

        if linhas_encontradas:
            resultados.append({
                "musica": nome_arquivo.replace(".txt", "").replace("_", " ").title(),
                "arquivo": nome_arquivo.replace(".txt", ""),
                "trechos": linhas_encontradas[:3]  # até 3 trechos por música
            })

    return resultados

if __name__ == "__main__":
    trecho = input("Digite um trecho da música: ").strip()
    achados = buscar_trecho(trecho)

    if not achados:
        print("❌ Nenhuma música encontrada com esse trecho.")
    else:
        print(f"\n🎵 {len(achados)} resultado(s) encontrado(s):\n")
        for resultado in achados:
            print(f"🎤 Música: {resultado['musica']}")
            for linha in resultado['trechos']:
                print(f"   ➜ {linha}")
            print()
