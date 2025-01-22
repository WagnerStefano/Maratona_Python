from flask import Flask, render_template #estrutura para criar o site
from flask_socketio import SocketIO, send #estrutura para criar o chat

app = Flask(__name__)#cria o site
app.config["SECRET_KEY"]= "chaveDeSegurançaAleatoria" #chave de segurança
app.config["DEBUG"] = True #Teste de código (será removido)
SocketIO = SocketIO(app, cors_allowed_origins="*") #cria conexão entre diferentes maquinas

@SocketIO.on("message") #define que a função abaixo vai ser acionada quando o evento "message" for ativado
def gerenciar_mensagens(mensagem):
    print(f"mensagem:  {mensagem}")
    send(mensagem, broadcast = True) # envia a mensagem para todos no site

@app.route("/") # inicia a rota do site
def home():
    return render_template("index.html") # o app deve carregar o arquivo HTML

if __name__ == "__main__":
    SocketIO.run(app, host = 'localhost') # define que o app vai iniciar em servidor local usando a minha rede
