from abc import ABC, abstractclassmethod


class Personagem(ABC):

    def __init__(self, posx, posy, velocidade):
        self.posx = posx
        self.posy = posy
        self.velocidade = velocidade