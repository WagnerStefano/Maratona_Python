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

    def enviar_mensagem(evento):
        texto = campo_enviar_mensagem.value
        chat.controls.append(ft.Text(texto))
        pagina.update

    campo_enviar_mensagem = ft.TextField(label=("Digite sua mensagem"))
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()
    linha_enviar = ft.Row(campo_enviar_mensagem, botao_enviar)



    def entrar_no_chat(evento):
        popup.open = False

        pagina.remove(titulo)

        pagina.remove(botao)

        pagina.add(chat)

        pagina.add(campo_enviar_mensagem)

        pagina.add(botao_enviar )

        pagina.update()


    #criar o popup
    titulo_popup= ft.Text("Bem vindo ao WebChat")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_no_chat)
    

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, 
                            actions=[botao_popup])



    #botão inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    #colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_popup)

#executar a função do App com o Flet
ft.app(main, view=ft.WEB_BROWSER)