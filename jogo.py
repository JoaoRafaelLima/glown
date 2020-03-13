from tkinter import *
import json
import sprites
import popUp
from fase import Fase
from player import Player
import execoes
import eventos



class Jogo(Tk):

    def __init__(self):
        super().__init__()
        #variaveis 
        self.label_itens = []
    
        #propriedades da janela
        self.geometry("496x527+248+0")
        self.minsize(496, 527)
        self.maxsize(496, 527)

        #widgets
        #/frames
        self.menu = Frame(self, width=496, height=527, bg="#212222")
        self.statusBar = Frame(self, width=496, height=31, bg="#000612")
        self.mapa = Frame(self, width=496, height= 496)

        #/labes
        self.player_name = Label(self.statusBar, fg="white", bg="#000612", font=("Arial bold", 14))
        self.player_vidas = Label(self.statusBar, fg="white", bg="#000612", font=("Arial bold", 14))
        self.player_itens = Label(self.statusBar, fg="white", bg="#000612", font=("Arial bold", 14))
        
        #labes/sprites
        self.sprites = sprites.Sprites()
        self.sprites.criar_menu(self.menu)
        
        #places
        self.menu.place(x=0, y=0)
        
        self.player_name.place(x=10, y=0)
        self.player_vidas.place(x=400, y=0)
        self.player_itens.place(x=210, y=0)

        #binds
        self.menu.bind('<Return>', self.start)
        self.menu.focus_force()
        self.mapa.bind('<Key>', self.ler_teclado)
        self.mapa.bind('<Escape>', self.ativar_poUp)
        
        self.mainloop()
    
    def ativar_poUp(self, ev):
        n = popUp.popUp(self, 'jogando')
        n.exibir()

    def carregar_jogo(self):
        with open('saves/save.json', 'r') as save:
            try:
                save_data = json.load(save)
                if len(save_data) == 0:
                    raise execoes.SaveVazio
                else:
                    player = save_data['player']
                    fase = save_data['fase']
                    return (player, fase)
                
            except execoes.SaveVazio as error:
                print(f"Erro: {error}")

            finally:
                save.close()

    
    def start(self, fase):
        data = self.carregar_jogo()
        if data:
            print("data")
        else:
            player = Player("joao", 1, 0, 1)
            self.fase = Fase(player)
            mapa = self.fase.ler_mapa("mapa1")
            

        self.configurar_partida(player, self.fase)
        self.render(mapa)
        self.sprites.criar_player(self.mapa)
        self.posi_obj_dinamicos()

    def ler_teclado(self, event):
        key = str(event.char)
        eventos.colide_mapa(self.fase.player, key, self.fase.mapa)
        eventos.coletarItem(self, self.fase.player, self.fase)
        self.atualizar_player()

    def posi_obj_dinamicos(self):
        self.atualizar_player()
        self.criar_enemigos(self.fase.ler_enemigos("mapa1"))

    def atualizar_player(self):
        posGhfX = self.fase.player.posx*31
        posGhfY = self.fase.player.posy*31
        self.sprites.player.place(x=posGhfX, y=posGhfY)

    def configurar_partida(self, player, f1):
        self.menu.place_forget()
        self.statusBar.place(x=0, y=0)
        self.atualizar_status_bar(player, f1)
        
        self.mapa.place(x=0, y=31)
        self.mapa.focus_force()

    def atualizar_status_bar(self, player, f1):
        self.player_name['text'] = "Player: "+player.nome
        self.player_itens['text'] = "itens: "+str(len(player.itens))+"/"+str(len(f1.itens))
        self.player_vidas['text'] = "Vidas: "+str(player.vidas)

    def retirar_item(self, pos):
        self.label_itens[pos]['image'] = self.sprites.img_chao
    
    def abrir_porta(self):
        self.sprites.porta['image'] = self.sprites.img_chao

    def criar_enemigos(self, *enemigos):
        enemigos = enemigos[0]
        self.enemigos4 = []
        objts = {}
        for enemigo in enemigos:
            enemigoGUI = self.sprites.criar_enemigo(self.mapa)
            enemigoGUI.place(x=enemigo.posx, y=enemigo.posy)
            objts['logico'] =  enemigo
            objts['grafico'] =  enemigoGUI
            self.enemigos4.append(objts.copy())
            objts.clear()
        self.fase.mover_enemigos(self.enemigos4)

    def render(self, mapa):
        posx = 0
        posy = 0
     
        
        for linha in mapa:
            for coluna in linha:

                if coluna == 0:
                    self.sprites.criar_chao(self.mapa, posx, posy)
                
                elif coluna == 1:
                    self.sprites.criar_parede(self.mapa, posx, posy)

                elif coluna == 2:
                    self.sprites.criar_item(self.mapa, posx, posy)
                    self.label_itens.append(self.sprites.item)
                  
                elif coluna == 3:
                    self.sprites.criar_porta(self.mapa, posx, posy)
                
                elif coluna == 4:
                    self.sprites.criar_portal(self.mapa, posx, posy)      
                    
                posx+=31
            posy+=31
            posx = 0

Jogo()