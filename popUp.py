from tkinter import Frame, Label, CENTER, Button
from config import *

class popUp(Frame):
    ativo = False
    def __init__(self, master, status):
        super().__init__(master)
        #variaveis
        self.status = status
        self.master = master
        #fonts
        self.font1 = ('Arial bold', 14)
        self.font2 = ('Arial', 12)
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
                self.botao_op['text'] = "Restart"
                self.botao_op['width'] = 12
                self.botao_op['command'] = self.reiniciar_jogo
                self.botao_op2['text'] = "Sair"
                self.botao_op2['command'] = self.sair
            

            self.place(x=100, y=120 )
            self.menssagem.place(x=50, y=30)
            self.botao_op.place(x=30,y=100)
            self.botao_op2.place(x=170,y=100 )
            popUp.ativo = True
        else:
            print("ja tem um popUp fixado!!!")   
    def sair(self):
        self.place_forget()
        self.master.sair_partida()
        popUp.ativo = False
    
    def reiniciar_jogo(self):
        self.place_forget()
        self.master.sair_partida()
        popUp.ativo = False

    def continuar_jogo(self):
        self.place_forget()
        popUp.ativo = False
    
    def proxima_fase(self):
        self.place_forget()
        self.master.proxima_fase()
        popUp.ativo = False

