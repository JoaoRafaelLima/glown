from tkinter import Frame, Button, Tk, Label
from config import *

class MenuPartida(Frame):
    ativo = False
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self['bg'] = CORES['bg']
        self['width'] = 300
        self['height'] = 280
        self['highlightthickness'] = 2
        self['highlightbackground'] = "#002252"
        self.opcoes = ['Continuar', 'Salvar', 'Sair']
        self.labels_opcoes = []
        self.lb1 = Label(
            self,
            width=16,
            text="Menu",
            font=FONTS['titulo'],
            bd=0,
            bg=CORES['bg'],
            activebackground= CORES['bg'],
            fg=CORES['texto'],
            activeforeground= CORES['texto']
        )
        '''
        self.bt1 = Button(
            self,
            width=16,
            text="Continuar",
            font=FONTS['titulo'],
            relief="groove",
            bg=CORES['bg'],
            activebackground= CORES['bg'],
            fg=CORES['texto'],
            activeforeground= CORES['texto'],
            command=self.continuar
        )
        self.bt2 = Button(
            self,
            width=16,
            text="Salvar",
            font=FONTS['titulo'],
            relief="groove",
            bg=CORES['bg'],
            activebackground= CORES['bg'],
            fg=CORES['texto'],
            activeforeground= CORES['texto'],
            command=self.salvar_jogo
        )
        self.bt3 = Button(
            self,
            width=16,
            text="Sair",
            font=FONTS['titulo'],
            relief="groove",
            bg=CORES['bg'],
            activebackground= CORES['bg'],
            fg=CORES['texto'],
            activeforeground= CORES['texto'],
            command=self.sair
        )
        '''
        self.exibir_opcoes()
        #places
        self.lb1.place(x=17, y=15)
        #self.bt1.place(x=17, y=60)
        #self.bt2.place(x=17, y=120)
        #self.bt3.place(x=17, y=180)

    
    def continuar(self):
        self.place_forget()
    
    def sair(self):
        self.place_forget()
        self.master.ativar_popUp(1)
    

    def salvar_jogo(self):
        resp = self.master.fase.salvar_jogo()
        if resp:
            self.place_forget()
            print("salvo com sucesso !!")
        else:
            print("error")
        
    def exibir(self, x, y):
        if MenuPartida.ativo == False:
            self.place(x=x, y=y)
            MenuPartida.atvio = True
        
    def exibir_opcoes(self):
        POSX = 17
        posy = 60
        for opcao in self.opcoes:
            botao = Button(
                self,
                width=16,
                text=opcao,
                font=FONTS['titulo'],
                relief="groove",
                bg=CORES['bg'],
                activebackground= CORES['bg'],
                fg=CORES['texto'],
                activeforeground= CORES['texto']
            )
            botao.place(x=POSX, y=posy)
            posy+=60
            self.labels_opcoes.append(botao)
        self.labels_opcoes[0]['command'] = self.continuar 
        self.labels_opcoes[1]['command'] = self.salvar_jogo
        self.labels_opcoes[2]['command'] = self.sair 


