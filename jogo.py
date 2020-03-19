from tkinter import *
import json
import sprites
import popUp
from fase import Fase
from player import Player
import execoes
import eventos
from menu import Menu
from menuPartida import MenuPartida
from config import CORES



class Jogo(Tk):

    def __init__(self):
        super().__init__()
        #variaveis 
        self.mapas = ['fase1', 'fase2', 'fase3']
        self.label_itens = []
        self.labels = []
        self.porta = []
        self.mapa_atual = 0
        self.status = "jogando"
        #fonte
        self.fonte = ('Fixedsys', 14)
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
        self.player_name = Label(self.statusBar, fg="white", bg="#000612", font=self.fonte)
        self.player_vidas = Label(self.statusBar, fg="white", bg="#000612", font=self.fonte)
        self.player_itens = Label(self.statusBar, fg="white", bg="#000612", font=self.fonte)
        
        #labes/sprites
        self.sprites = sprites.Sprites()
        self.sprites.criar_menu(self.menu)
        
        #places
        self.menu.place(x=0, y=0)
        
        self.player_name.place(x=10, y=5)
        self.player_vidas.place(x=400, y=5)
        self.player_itens.place(x=210, y=5)

        #binds
        self.menu.bind('<Return>', self.iniciar_menu)
        self.menu.focus_force()
        self.mapa.bind('<Key>', self.ler_teclado)
        self.mapa.bind('<Escape>', self.menu_partida)
        
        self.mainloop()
    def menu_partida(self, event):
        menu = MenuPartida(self)
        menu.exibir(100, 80)

    def ativar_popUp(self, ev):
        pop_up = popUp.popUp(self, self.status)
        pop_up.exibir()

    def proxima_fase(self):
        self.sair_partida()
        self.mapa_atual+=1
        

    def carregar_jogo(self):
        with open('save/save.json', 'r') as save:
            try:
                data = json.load(save)
                if len(data) == 0:
                    raise execoes.SaveVazio
                else:
                    print(data)
                    self.mapa_atual = data['fase_atual']
                    self.novo_jogo(data=data)
                
                
            except execoes.SaveVazio as error:
                print(f"Erro: {error}")

            finally:
                save.close()

    def sair_partida(self):
        if self.status == "jogando" or self.status == "perdeu":
            print("fase inicial zero")
            self.mapa_atual = 0
        self.fase.parar()
        self.fase.clear()
        print(f" threads: {self.fase.threads}")
        print("Partida  finalizada")

    def iniciar_menu(self, event):
        self.menu.place_forget()
        self.menu_ops = Menu(self)
        self.menu_ops.place(x=0, y=0)
        
    def novo_jogo(self, data=None):
        if self.mapa_atual+1 > len(self.mapas):
            print("Nao a proxima fase")
            self.statusBar.place_forget()
            self.mapa.place_forget()
            self['bg'] = CORES['bg']
            self.status = "zerou"
            self.ativar_popUp(1)
        else:
            self.status = "jogando"
            self.menu_ops.place_forget()
            self.fase = Fase(self.mapas[self.mapa_atual], self, data)
            self.configurar_partida()

            self.render(self.fase.mapa)
            self.fase.getItens()
            self.label_player = self.sprites.criar_player(self.mapa)
            self.posi_obj_dinamicos()

    def ler_teclado(self, event):
        key = str(event.char)
        eventos.colide_mapa(self.fase.player, key, self.fase.mapa)
        eventos.coletarItem(self, self.fase.player, self.fase)
        eventos.verificar(self, self.fase.player, self.fase)
        self.atualizar_player()
   
    def posi_obj_dinamicos(self):
        self.atualizar_player()
        self.criar_enemigos(self.fase.enemigos)

    def atualizar_player(self):
        posGhfX = self.fase.player.posx*31
        posGhfY = self.fase.player.posy*31
        self.label_player.place(x=posGhfX, y=posGhfY)

    def configurar_partida(self):
        self.menu.place_forget()
        self.statusBar.place(x=0, y=0)
        self.atualizar_status_bar(self.fase.player)
        
        self.mapa.place(x=0, y=31)
        self.mapa.focus_force()

    def atualizar_status_bar(self, player):
        self.player_name['text'] = "Player: "+player.nome
        self.player_itens['text'] = "itens: "+str(len(player.itens))+"/"+str(len(self.fase.itens))
        self.player_vidas['text'] = "Vidas: "+str(player.vidas)

    def retirar_item(self, pos):
        self.label_itens[pos]['image'] = self.sprites.img_chao
       
    def abrir_porta(self):
        self.porta[0]['image'] = self.sprites.img_chao

    def ganhou(self):
        self.status = "ganhou"
        self.label_player['image'] = self.sprites.img_player_portal
        self.fase.parar_loop = True
        self.ativar_popUp("event")

    def criar_enemigos(self, *enemigos):
        print("criando objetos")
      
        self.enemigos4 = []
        objts = {}
        for enemigo in enemigos[0]:
            
            enemigoGUI = self.sprites.criar_enemigo(self.mapa)
            posx = enemigo.posx*31
            posy = enemigo.posy*31
            enemigoGUI.place(x=posx, y=posy)
            objts['logico'] =  enemigo
            objts['grafico'] =  enemigoGUI
            self.enemigos4.append(objts.copy())
            objts.clear()
        self.fase.mover_enemigos(self.enemigos4)

    def limpar_mapa(self):
        #self.mapa.destroy()
        self.porta.clear()
        self.limpar_player()
        for label in self.labels:
            label.destroy()
        self.label_itens.clear()
      
        if self.status == "jogando" or self.status == "perdeu":
            self.menu_ops.place(x=0, y=0)
            self.menu_ops.focus_force()

        elif self.status == "ganhou":
            self.novo_jogo()

    def limpar_player(self):
        self.label_player.destroy()
        
    def limpar_enemigos(self):
        for enem in self.enemigos4:
            enem['grafico'].destroy()
            enem.clear()


    def render(self, mapa):
        posx = 0
        posy = 0
       
        for linha in mapa:
            for coluna in linha:

                if coluna == 0:
                    bloco = self.sprites.criar_chao(self.mapa, posx, posy)   
                
                elif coluna == 1:
                    bloco = self.sprites.criar_parede(self.mapa, posx, posy)

                elif coluna == 2:
                    bloco = self.sprites.criar_item(self.mapa, posx, posy)
                    self.label_itens.append(bloco)
                  
                elif coluna == 3:
                    bloco = self.sprites.criar_porta(self.mapa, posx, posy)
                    self.porta.append(bloco)
                    self.porta.append(posx)
                    self.porta.append(posy)

                elif coluna == 4:
                    bloco = self.sprites.criar_portal(self.mapa, posx, posy)      
                    
                posx+=31
                self.labels.append(bloco)
            posy+=31
            posx = 0


    def sair(self):
        self.quit()

Jogo()