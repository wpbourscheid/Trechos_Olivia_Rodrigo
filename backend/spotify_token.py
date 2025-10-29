# spotify_token.py
import requests
import base64
import os

CLIENT_ID = open("backend/senha.txt").read().strip()
CLIENT_SECRET = open("backend/senha.txt").read().strip()

def get_token():
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
    print("Token:", get_token())
