from personagem import Personagem



class Player(Personagem):
    

    def __init__(self, nome: str, velocidade: int, posy: int, posx: int):
        super().__init__(velocidade, posy, posx)
        self.vidas = 3
        self.itens = []
        self.nome = nome
     

    def getIten(self, item):
        self.itens.append(item)

    def mover(self, exp):
        if exp == "w":
            self.posy-=1
        
        elif exp == "s":
            self.posy+=1

        elif exp == "a":
            self.posx-=1
                
        elif exp == "d":
            self.posx+=1
            

    def getX(self):
        return int(self.posx)

    def getY(self):
        return int(self.posy)

