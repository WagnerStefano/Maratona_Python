'''Tela Inicial:
    Titulo: WebChat
    Botão: Iniciar Chat
            Quando clicar no botão:
            abrir um popup/modal/alerta
            Subtitulo: Bem vindo ao Webchat
            Caixa de Texto: Escreva seu nome no chat
            Botão: Entrar no Chat
                quando clicar no botão
                sumir com o titulo
                Sumir com botão Iniicar Chat
                    Carregar o Chat
                    Carregar o campo Enviar mensagem: "Digite sua mensagem"
                    botão enviar
                        quando clicar no botão enviar
                        enviar mensagem
                        limpar caixa de mensagem
            

'''
import flet as ft

def main (pagina:)
    #titulo
    titulo = ft.Text("WebChat")
    pagina.add(titulo)

    #botão inicial
    botao = ft.ElevateButton("Iniciar Chat")
    pagina.add(botao)

ft.app(main)