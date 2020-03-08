from enemigo import Enemigo



class Fase(object):

    def __init__(self, player):
        
        self.porta = []
        self.itens = []
        self.player = player
     
        self.enemigos = []
        self.mapa = []

    def getItem(self, item):
        self.itens.append(item.copy())

    def ler_mapa(self, mapa):
        path = "mapas/"+mapa+".txt"
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

                mapa_matrix.append(tmp.copy())
                tmp.clear()

            text.close()
        self.mapa = mapa_matrix
        return mapa_matrix

    def ler_enemigos(self, mapa):
        arquivo = "mapas/"+mapa+"_ents.txt"

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
            generico = Enemigo(attrs[0], attrs[1], attrs[2], 31)

            self.enemigos.append(generico)
        return self.enemigos

    def abrir_porta(self):
        self.mapa[self.porta[0]][self.porta[1]] = 0

    def pos_objts_nao_staticos(self):
        pass