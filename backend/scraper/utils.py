import os

folder = 'letras'

def limpar_musicas(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.txt') and 'unreleased' in filename.lower():
            file_path = os.path.join(folder, filename)
            print(f"🧹 Removendo arquivo indesejado: {file_path}")
            os.remove(file_path)