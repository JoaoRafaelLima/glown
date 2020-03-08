from tkinter import Frame, Label, CENTER, Button


class popUp(Frame):

    def __init__(self, master, status):
        super().__init__(master)
        #variaveis
        self.status = status
        #fonts
        self.font1 = ('Arial bold', 14)
        self.font2 = ('Arial', 12)
        #propriedades
        self['width'] = 300
        self['height'] = 150
        self['bg'] = "#000612"
        self['bd'] = 1
        self['relief'] = "ridge"
        #labels
        self.menssagem = Label(self, font=self.font1, bg="#000612", fg="white")
        self.botao_op = Button(self, relief="groove", width=10, font=self.font2, activebackground="#000612", bg="#000612", activeforeground="white", fg="white")
        self.botao_op2 = Button(self, relief="groove", width=10,  font=self.font2, activebackground="#000612", bg="#000612", activeforeground="white", fg="white")
    
    def exibir(self):
        if self.status == "jogando":
            self.menssagem['text'] = "Sair do jogo?"
            self.botao_op['text'] = "Sim"
            # self.botao_op['command'] = self.clear
            self.botao_op2['text'] = "Nao"
            self.botao_op2['command'] = self.continuar_jogo

        elif self.status == "ganhou":
            self.menssagem['text'] = "Voce ganhou?"
            self.botao_op['text'] = "Continuar"
            # self.botao_op['command'] = self.clear
            self.botao_op2['text'] = "Sair"
            # self.botao_op2['command'] = self.sair

        elif self.status == "perdeu":
            self.menssagem['text'] = "Voce perdeu"
            self.botao_op['text'] = "Restart"
            self.botao_op['width'] = 12
            self.botao_op2['text'] = "Sair"
            # self.botao_op2['command'] = self.clear

        self.place(x=100, y=120 )
        self.menssagem.place(x=90, y=20)
        self.botao_op.place(x=30,y=100)
        self.botao_op2.place(x=170,y=100 )
        
    def continuar_jogo(self):
        self.place_forget()
