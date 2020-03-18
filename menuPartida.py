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
            activeforeground= CORES['texto']
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
        
        #places
        self.lb1.place(x=17, y=15)
        self.bt1.place(x=17, y=60)
        self.bt2.place(x=17, y=120)
        self.bt3.place(x=17, y=180)
    
    def continuar(self):
        self.place_forget()
    
    def sair(self):
        self.place_forget()
        self.master.ativar_popUp(1)
    
    def exibir(self, x, y):
        if MenuPartida.ativo == False:
            self.place(x=x, y=y)
            MenuPartida.atvio = True


