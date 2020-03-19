from tkinter import Frame, Label, CENTER, Button
from config import *

class popUp(Frame):
    ativo = False
    def __init__(self, master, status):
        super().__init__(master)
        #variaveis
        self.status = status
        self.master = master
        #propriedades
        self['width'] = 300
        self['height'] = 150
        self['bg'] = CORES['bg']
        self['bd'] = 1
        self['relief'] = "ridge"
        #labels
        self.menssagem = Label(self, font=FONTS['titulo'], bg="#000612", fg="white")
        self.botao_op = Button(self, relief="groove", width=10, font=FONTS['texto'], activebackground="#000612", bg="#000612", activeforeground="white", fg="white")
        self.botao_op2 = Button(self, relief="groove", width=10,  font=FONTS['texto'], activebackground="#000612", bg="#000612", activeforeground="white", fg="white")
    
    def exibir(self):
       
        if_button2 = True
        if not popUp.ativo:
            if self.status == "jogando":
                self.menssagem['text'] = "Sair do jogo?"
                self.botao_op['text'] = "Sim"
                self.botao_op['command'] = self.sair
                self.botao_op2['text'] = "Nao"
                self.botao_op2['command'] = self.continuar_jogo

            elif self.status == "ganhou":
                self.menssagem['text'] = "Voce ganhou"
                self.botao_op['text'] = "Continuar"
                self.botao_op['command'] = self.proxima_fase
                self.botao_op2['text'] = "Sair"
                self.botao_op2['command'] = self.sair

            elif self.status == "perdeu":
                self.menssagem['text'] = "Voce perdeu"
                self.botao_op['text'] = "Restart"
                self.botao_op['width'] = 12
                self.botao_op['command'] = self.reiniciar_jogo
                self.botao_op2['text'] = "Sair"
                self.botao_op2['command'] = self.sair
            
            elif self.status == "zerou":
                self.menssagem['text'] = "Jogo terminado"
                self.botao_op['text'] = "Sair"
                self.botao_op['width'] = 12
                self.botao_op['command'] = self.voltar_menu
                if_button2 = False
               
            

            self.place(x=100, y=120 )
            self.menssagem.place(x=50, y=30)
            self.botao_op.place(x=30,y=100)
            if if_button2:
                self.botao_op2.place(x=170,y=100 )
            popUp.ativo = True
        else:
            pass

    def voltar_menu(self):
        self.default()
        self.master.iniciar_menu(1)
        self.master.status = 'jogando'
        self.master.mapa_atual = 0

    def sair(self):
        self.default()
        self.master.sair_partida()
    
    def reiniciar_jogo(self):
        self.default()
        self.master.sair_partida()

    def continuar_jogo(self):
        self.default()
    
    def proxima_fase(self):
        self.default()
        self.master.proxima_fase()
    
    def default(self):
        self.place_forget()
        popUp.ativo = False

