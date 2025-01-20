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

#Flet
#importar o Flet (ft)
import flet as ft

#criar uma função principal para rodar o aplicativo

def main (pagina): 
    #titulo
    titulo = ft.Text("WebChat")
    pagina.add(titulo)

    #criar o popup
    titulo_popup= ft.Text(title=("Bem vindo ao WebCH=hat"))
    caixa_nome = ft.TextField()
    botao_popup = ft.ElevatedButton("Entrar no Chat")
    

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, 
                            actions= [botao_popup  ])



    #botão inicial
    def abrir_popup(evento):
        pagina.dialog=popup

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    #colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)

#executar a função do App com o Flet
ft.app(main, view=ft.WEB_BROWSER)