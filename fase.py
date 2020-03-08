


class Fase(object):

    def __init__(self, player, *enemigos):
        self.porta = []
        self.itens = []
        self.player = player
        self.enemigos = enemigos
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

    def abrir_porta(self):
        self.mapa[self.porta[0]][self.porta[1]] = 0

    def pos_objts_nao_staticos(self):
        pass