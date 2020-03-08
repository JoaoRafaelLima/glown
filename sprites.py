from tkinter import PhotoImage, Label


class Sprites(object):

    def __init__(self):
        #imagens
        self.img_player = PhotoImage(file="imgs/player.png")
        self.img_enemigo = PhotoImage(file="imgs/enemigo.png")
        self.img_item = PhotoImage(file="imgs/item.png")
        self.img_portal = PhotoImage(file="imgs/portal.png")
        self.img_player_portal = PhotoImage(file="imgs/player_in_port.png")
        self.img_parede = PhotoImage(file="imgs/parede.png")
        self.img_porta = PhotoImage(file="imgs/porta.png")
        self.img_chao = PhotoImage(file="imgs/chao.png")
        self.img_menu = PhotoImage(file="imgs/menu.png")

    def criar_player(self, master):
        self.player = Label(master, image=self.img_player, bd=0)

    def criar_enemigo(self, master):
        self.enemigo = Label(master, image=self.img_enemigo, bd=0)

    def criar_item(self, master, x, y):
        self.item = Label(master, image=self.img_item, bd=0)
        self.item.place(x=x, y=y)

    def criar_portal(self, master, x, y):
        self.portal = Label(master, image=self.img_portal, bd=0)
        self.portal.place(x=x, y=y)

    def criar_player_portal(self, master):
        self.player_portal = Label(master, image=self.img_player_portal, bd=0)
        

    def criar_parede(self, master, x, y):
        self.parede = Label(master, image=self.img_parede, bd=0)
        self.parede.place(x=x, y=y)

    def criar_porta(self, master, x, y):
        self.porta = Label(master, image=self.img_porta, bd=0)
        self.porta.place(x=x, y=y)

    def criar_chao(self, master, x, y):
        self.chao = Label(master, image=self.img_chao, bd=0)
        self.chao.place(x=x, y=y)

    def criar_menu(self, master):
        self.menu = Label(master, image=self.img_menu, bd=0)
        self.menu.place(x=0, y=0)
