# spotify_token.py
import requests
import base64
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_token():
    """Obtém um access token via Client Credentials Flow"""
    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError("CLIENT_ID ou CLIENT_SECRET não configurados no .env")

    url = "https://accounts.spotify.com/api/token"
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {"Authorization": f"Basic {b64_auth_str}"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token = response.json()["access_token"]
    return token

if __name__ == "__main__":
    print("Token gerado com sucesso:")
    print(get_token())
