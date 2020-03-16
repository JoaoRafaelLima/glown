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
        self.img_menu = PhotoImage(file="imgs/menu2.png")

    def criar_player(self, master):
        return Label(master, image=self.img_player, bd=0)

    def criar_enemigo(self, master):
        return Label(master, image=self.img_enemigo, bd=0)

    def criar_item(self, master, x, y):
        label = Label(master, image=self.img_item, bd=0)
        label.place(x=x, y=y)
        return label
        
    def criar_portal(self, master, x, y):
        label = Label(master, image=self.img_portal, bd=0)
        label.place(x=x, y=y)
        return label
    
    def criar_player_portal(self, master):
        label = Label(master, image=self.img_player_portal, bd=0)
        return label

    def criar_parede(self, master, x, y):
        label = Label(master, image=self.img_parede, bd=0)
        label.place(x=x, y=y)
        return label
      

    def criar_porta(self, master, x, y):
        label = Label(master, image=self.img_porta, bd=0)
        label.place(x=x, y=y)
        return label
        

    def criar_chao(self, master, x, y):
        label = Label(master, image=self.img_chao, bd=0)
        label.place(x=x, y=y)
        return label

    def criar_menu(self, master):
        self.menu = Label(master, image=self.img_menu, bd=0)
        self.menu.place(x=0, y=0)
