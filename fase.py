from enemigo import Enemigo
from player import Player
from time import sleep
from random import choice
import threading
import eventos
import json


class Fase(object):

    def __init__(self, fase, master, data):
        self.data = data
        self.master = master
        self.fase = fase
        self.mapa = []
        self.enemigos = []
        self.porta = []
        self.carregar_fase()
        self.portal = []
        self.itens = []
        self.labels = []
        self.threads = 0
        self.parar_loop = False
        self.pegar_objs_sp()

    def getItem(self, item):
        self.itens.append(item.copy())

    def getItens(self):
        cont = 0
        for item in self.itens:
            if item in self.player.itens:
                self.master.retirar_item(cont)
            cont+=1

    def pegar_objs_sp(self):
        for cont, linha in enumerate(self.mapa):
            for cont2, coluna in enumerate(linha):
                if coluna == 2:
                    self.getItem([cont, cont2])

                elif coluna == 3:
                    self.porta.append(cont)
                    self.porta.append(cont2)
                
                elif coluna == 4:
                    self.portal.append(cont)
                    self.portal.append(cont2)
        
    
    def parar(self):
        self.parar_loop = True
        print(self.threads)
        thread = threading.Thread(target=self.teste, args=()).start()
    
    def teste(self):
        while True:
            if self.threads == 0:
                break
            print(self.threads)
        print("acabou")
        self.apagar_labels()
        self.master.limpar_mapa()
        
    def apagar_labels(self):
        for label in self.labels:
            label.destroy()
        self.labels.clear()
        print(self.labels)
        

    def criar_player(self, dados: dict):
        if self.data:
            self.player = Player(dados["nome"], dados["velocidade"], self.data["posy"], self.data["posx"])
            self.player.vidas = self.data['vidas']
            self.player.itens = self.data['itens']
            
        else:
            self.player = Player(dados["nome"], dados["velocidade"], dados["posy"], dados["posx"])
        

    def criar_enemigos(self, *enemigos):
        for enemigo in enemigos[0]:
            generico = Enemigo(enemigo[0], enemigo[1], enemigo[2], 1)
            self.enemigos.append(generico)
        return self.enemigos

    def abrir_porta(self):
        self.mapa[self.porta[0]][self.porta[1]] = 0

    def pos_objts_nao_staticos(self):
        pass

    def mover_enemigos(self,  *args):
        
        for dic in args[0]:
            self.labels.append(dic['grafico'])
            thd = threading.Thread(target=self.loop_enemigos, kwargs=(dic))
            thd.start()
            
            self.threads+=1
        print(f"quantidade de threads: {self.threads}")
            
    def loop_enemigos(self, **kwargs):
        
        
        enemigo = kwargs['logico']
        label_enemigo = kwargs['grafico']
        #obj1 instancia de enemigo
        #obj2 instancia de Label
        enemigo.posx = int(enemigo.posx)
        enemigo.posy = int(enemigo.posy)

        posx_inicial = enemigo.posx
        posx_final = enemigo.posx+(2*enemigo.velocidade)

        posy_inicial = enemigo.posy
        posy_final = enemigo.posy+(2*enemigo.velocidade)

        if enemigo.eixo_movimento == "y":
            while not self.parar_loop:
                sleep(choice(enemigo.times))
                if enemigo.incrementa_eixo == True:
                    enemigo.posy+=enemigo.velocidade

                    if enemigo.posy == posy_final:
                        enemigo.incrementa_eixo = False
                else:
                    enemigo.posy-=enemigo.velocidade

                    if enemigo.posy == posy_inicial:
                        enemigo.incrementa_eixo = True

                eventos.colidir(self.master, self.player, enemigo)
                posx = enemigo.posx*31
                posy = enemigo.posy*31
                label_enemigo.place(x=posx, y=posy)

        elif enemigo.eixo_movimento == "x":
            while not self.parar_loop:
                sleep(choice(enemigo.times))
                if enemigo.incrementa_eixo == True:
                    enemigo.posx+=enemigo.velocidade

                    if enemigo.posx == posx_final:
                        enemigo.incrementa_eixo = False
                else:
                    enemigo.posx-=enemigo.velocidade

                    if enemigo.posx == posx_inicial:
                        enemigo.incrementa_eixo = True
                eventos.colidir(self.master, self.player, enemigo)
                posx = enemigo.posx*31
                posy = enemigo.posy*31
                label_enemigo.place(x=posx, y=posy)
        self.threads-=1
        print(self.threads)
        
    def clear(self):
        self.porta.clear()
        self.itens.clear()
        self.enemigos.clear()
        self.mapa.clear()

    def carregar_fase(self):
        fase = "fases/"+self.fase+".json"
        try:
            with open(fase, 'r') as arq:
                dados = json.load(arq)
                arq.close()
            
            self.criar_player(dados['player'])
            self.criar_enemigos(dados['enemigos'])
            self.mapa = dados['mapa']
            
        except FileNotFoundError:
            print("Caminho nao encontrado")
   
    def salvar_jogo(self):
        
        info = {
            "fase_atual": self.master.mapa_atual,
            "posx": self.player.posx,
            "posy": self.player.posy,
            "vidas": self.player.vidas,
            "itens": self.player.itens.copy()
        }
        try:
            with open('save/save.json', 'w') as arq:
                json.dump(info, arq, indent=4)
                arq.close()
            return True
        except:
            return False
