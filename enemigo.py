from personagem import Personagem


class Enemigo(Personagem):

    def __init__(self, posx, posy,  eixo_movimento, velocidade):
        super().__init__(posx, posy, velocidade)
        self.eixo_movimento = eixo_movimento
        self.times = [0.8, 1.2, 0.5, 0.1]
        self.incrementa_eixo = True