from enemigo import Enemigo
from player import Player
from time import sleep
from random import choice
import threading
import eventos


class Fase(object):

    def __init__(self, fase, master):
        self.master = master
        self.fase = fase
        self.porta = []
        self.portal = []
        self.itens = []
        self.labels = []
        self.threads = 0
        self.ler_player()
        self.parar_loop = False
        self.enemigos = []
        self.mapa = []

    def getItem(self, item):
        self.itens.append(item.copy())

    def ler_mapa(self):
        path = "fases/"+self.fase+"/mapa.txt"
        mapa_matrix = []
        tmp = []
        with open(path,'r') as text:
            mapa_str = text.readlines()
            for cont, linha in enumerate(mapa_str):
                linha = linha.rstrip()
                for cont2, coluna in enumerate(linha):
                    valor_int = int(coluna)
                    tmp.append(valor_int)
                    if valor_int == 2:
                        self.getItem([cont, cont2])

                    elif valor_int == 3:
                        self.porta.append(cont)
                        self.porta.append(cont2)
                    
                    elif valor_int == 4:
                        self.portal.append(cont)
                        self.portal.append(cont2)

                mapa_matrix.append(tmp.copy())
                tmp.clear()

            text.close()
        self.mapa = mapa_matrix
        return mapa_matrix
    
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
        

    def ler_player(self):
        arquivo = "fases/"+self.fase+"/player.txt"
        with open(arquivo, 'r') as arq:
            player = arq.readlines()
            info = player[0].split(';')
            info[1] = int(info[1])
            info[2] = int(info[2])
            info[3] = int(info[3])
            return self.criar_player(info)

    def criar_player(self, dados):
        self.player = Player(dados[0], dados[1], dados[2], dados[3])

    def ler_enemigos(self):
        arquivo = "fases/"+self.fase+"/enemigos.txt"

        with open(arquivo, 'r') as arq:
            enemigos = arq.readlines()
            for cont in range(0, len(enemigos)):
                enemigos[cont] = enemigos[cont].rstrip()
                print(enemigos[cont])

        return self.criar_enemigos(enemigos)

    def criar_enemigos(self, *enemigos):
      
        enemigos = enemigos[0]
        for enemigo in enemigos:
            attrs = enemigo.split(',')
            generico = Enemigo(attrs[0], attrs[1], attrs[2], 1)

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
        
    