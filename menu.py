from tkinter import Canvas, Tk, CENTER


class Menu(Canvas):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self['width'] = 496
        self['height'] = 527
        self['highlightthickness'] = 0
        self['bg'] = '#000612'
        self.fonte = ('Arial bold', 20)
        self.posicao_cursor = 180
        self.focus_force()
        self.bind('<Key>', self.mover_cursor)
        self.bind('<Return>', self.select)
        self.desenhar_texto()
        self.criar_borda()
    
        
    def desenhar_texto(self):
        #for op in self.ops:
        op1 = self.create_text(255, 160, justify=CENTER, text="Continuar", font=self.fonte, fill="white")
        op2 = self.create_text(255, 205, justify=CENTER, text="Novo Jogo", font=self.fonte, fill="white")
        op3 = self.create_text(255, 250, justify=CENTER, text="Sair", font=self.fonte, fill="white")
    
    def criar_borda(self):
        self.borda = self.create_polygon(
            245,180, 
            255, 190,
            265, 180,
            width=3, fill="#773300"
        )
    
    def mover_cursor(self, ev):
        
        if str(ev.char) == 'w':
            self.up()
        elif str(ev.char) == 's':
            self.down()


    def up(self):
        
        self.move( self.borda, 0, -45)
        self.posicao_cursor-=45
        if self.posicao_cursor < 180:
            self.move( self.borda, 0, 135)
            self.posicao_cursor+=135
        print(self.posicao_cursor)


    def down(self):
        
        self.move( self.borda, 0, 45)
        self.posicao_cursor+=45
        if self.posicao_cursor > 270:
            self.move( self.borda, 0, -135)
            self.posicao_cursor-=135
        print(self.posicao_cursor)

    def select(self, event):
        if self.posicao_cursor == 180:
            self.master.carregar_jogo()

        elif self.posicao_cursor == 225:
            self.master.novo_jogo()

        elif self.posicao_cursor == 270:
            self.master.sair()
'''
test = Tk()
test.geometry("496x527")
test['bg'] = "red"
menu = Menu(test)
menu.place(x=0, y=0)

test.mainloop()
'''

