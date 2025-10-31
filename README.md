# 🎵 Trechos Olivia Rodrigo

Um site interativo que permite buscar trechos de músicas da Olivia Rodrigo e visualizar a letra completa junto com o player do Spotify, mostrando informações da faixa como álbum e duração.

O projeto foi desenvolvido em Python (Flask) com integração às APIs do Spotify e BeautifulSoup para coleta das letras.

## 🧠 Funcionalidades

✅ Buscar músicas digitando um trecho da letra
✅ Visualizar a letra completa da música encontrada
✅ Player interativo do Spotify integrado
✅ Coleta automática das letras via web scraping
✅ Interface simples, responsiva e moderna

## ⚙️ Instalação e Execução
1️⃣ Clonar o Repositório:
```bash
    git clone https://github.com/wpbourscheid/Trechos_Olivia_Rodrigo.git
    cd Trechos_Olivia_Rodrigo
```
2️⃣ Criar e Ativar o Ambiente Virtual
Linux / macOS:
```bash
    python3 -m venv venv
    source venv/bin/activate
```
Windows (PowerShell):
```bash
    python -m venv venv
    venv\Scripts\activate
```
3️⃣ Instalar Dependências
```bash
    pip install -r requirements.txt
```
4️⃣ Configuração do Spotify:

Para habilitar o player e as informações das músicas, é necessário configurar uma conta no Spotify for Developers.

    Acesse [Spotify for Developers](https://developer.spotify.com/dashboard)

    Crie um novo App com nome (ex: Trechos Olivia Rodrigo)

    Em Redirect URI, adicione:
```bash
    http://127.0.0.1:8888/callback
```
    Copie o Client ID e Client Secret

    Faça uma cópia do arquivo .env.example e renomeie para .env:
```bash
    cp .env.example .env
```
    Abra o .env e preencha com suas credenciais:
```bash
    SPOTIFY_CLIENT_ID=seu_client_id_aqui
    SPOTIFY_CLIENT_SECRET=seu_client_secret_aqui
```
5️⃣ Rodar o Servidor
```bash
    python backend/app.py
```
Abra no navegador:
👉 http://127.0.0.1:5000
Ou link fornecido no terminal


## 🧩 Exemplo de Uso

Na página inicial, digite um trecho da letra (ex: car ride to malibu)

O sistema exibirá as músicas que contêm esse trecho

Clique em uma das músicas para abrir:
    - Letra completa
    - Player oficial do Spotify
    - Informações da música (álbum, duração, etc.)


## 🧰 Tecnologias Utilizadas
|   Tecnologia   |          Descrição            |
| -------------  | ----------------------------- |
| Python 3	     | Linguagem principal           |
| Flask	Framework| Web                           |
| BeautifulSoup4 | Web scraping das letras       |
| Requests	     | Comunicação com APIs externas |
| Spotify Web API| Dados e player das músicas    |
| HTML/CSS/JS	 | Frontend responsivo           |
| python-dotenv	 | Gestão de credenciais seguras |


## 📦 Dependências
```bash
Flask==3.1.1
requests==2.32.4
beautifulsoup4==4.13.4
python-dotenv==1.0.1
lxml==5.2.2
```

## 💡 Próximos Passos / TODO

 Implementar cache dos resultados de busca

 Exibir capa do álbum e preview da faixa

 Adicionar sistema de favoritos local

 Explorar deploy no Render / Railway

## 👨‍💻 Autor

### William Pedrolo Bourscheid
Graduando em Ciência da Computação (UFPel)
Foco em desenvolvimento Back-End, aprendizado de máquina, análise de dados e desenvolvimento web.

🔗 [LinkedIn](https://www.linkedin.com/in/wpbourscheid/)

🐙 [GitHub](https://github.com/wpbourscheid)