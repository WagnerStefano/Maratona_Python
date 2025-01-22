from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Substitua por uma chave mais forte
socketio = SocketIO(app)

# Configurar o logging para registrar erros
logging.basicConfig(level=logging.DEBUG)

# Função para emitir mensagens para uma sala específica
def emit_message(room, data):
    try:
        emit('message', data, room=room)
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    join_room('general')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    leave_room('general')

@socketio.on('message')
def handle_message(data):
    try:
        print(f'Received message: {data}')
        emit_message('general', data, broadcast=True)
    except Exception as e:
        logging.error(f"Erro ao processar mensagem: {e}")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)