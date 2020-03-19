from config import *

def verificar_missao(master, player, fase):
    if  len(player.itens) == len(fase.itens):
        fase.abrir_porta()
        master.abrir_porta()

def colidir(master, player, enemigo):
    if player.vidas > 0:
        if enemigo.posx == player.posx and enemigo.posy == player.posy:
            player.vidas-=1
            master.atualizar_status_bar(player)
    else:
        master.fase.parar_loop = True
        master.status = "perdeu"
        master.ativar_popUp("event")
        
def verificar(master, obj, fase):
    if obj.vidas == 0:
        print("voce perdeu")
        master.status = "perdeu"
        master.ativar_popUp("event")

    elif len(obj.itens) == len(fase.itens) and obj.posy == fase.portal[0] and obj.posx == fase.portal[1]:
        print("no portal")
        master.ganhou()
    else:
        master.label_player['image'] = master.sprites.img_player

def coletarItem(master, obj, fase):
    for indice, item in enumerate(fase.itens):
        if  obj.posy == item[0] and obj.posx == item[1]:
            if not item in obj.itens:
                obj.getIten(item)
                print("coletou")
                master.atualizar_status_bar(obj)
                master.retirar_item(indice)
    verificar_missao(master, obj, fase)


def colide_mapa(obj, key, cenario):
   
    if key == "w":
        if obj.posy > HEIGHT_I:
            if not cenario[obj.posy-1][obj.posx] == 1 and not cenario[obj.posy-1][obj.posx] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                     
    elif key == "s":
        if obj.posy < HEIGHT_F:
            if not cenario[obj.posy+1][obj.posx] == 1 and not cenario[obj.posy+1][obj.posx] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    elif key == "a":
        if obj.posx > WIDTH_I:
            if not cenario[obj.posy][obj.posx-1] == 1 and not cenario[obj.posy][obj.posx-1] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    elif key == "d":
       
        if obj.posx < WIDTH_F:
            if not cenario[obj.posy][obj.posx+1] == 1 and not cenario[obj.posy][obj.posx+1] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    print(f"y = {obj.posy}, x = {obj.posx}")
        #print(f" x  = {self.p1.posPlayerX}, y = {self.p1.posPlayerY}")
        
