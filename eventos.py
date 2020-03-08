

def verificar_missao(master, obj, fase):
    if  len(obj.itens) == len(fase.itens):
        fase.abrir_porta()
        master.abrir_porta()

def coletarItem(master, obj, fase):
    for indice, item in enumerate(fase.itens):
        if  obj.posy == item[0] and obj.posx == item[1]:
            if not item in obj.itens:
                obj.getIten(item)
                print("coletou")
                master.atualizar_status_bar(obj, fase)
                master.retirar_item(indice)
    verificar_missao(master, obj, fase)


def colide_mapa(obj, key, cenario):
   
    if key == "w":
        if obj.posy > 0:
            if not cenario[obj.posy-1][obj.posx] == 1 and not cenario[obj.posy-1][obj.posx] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                     
    elif key == "s":
        if obj.posy < 15:
            if not cenario[obj.posy+1][obj.posx] == 1 and not cenario[obj.posy+1][obj.posx] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    elif key == "a":
        if obj.posx > 0:
            if not cenario[obj.posy][obj.posx-1] == 1 and not cenario[obj.posy][obj.posx-1] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    elif key == "d":
       
        if obj.posx < 15:
            if not cenario[obj.posy][obj.posx+1] == 1 and not cenario[obj.posy][obj.posx+1] == 3:
                obj.mover(key)
            else:
                print("colidiu")
        else:
            print("distancia maxima")
                
    print(f"y = {obj.posy}, x = {obj.posx}")
        #print(f" x  = {self.p1.posPlayerX}, y = {self.p1.posPlayerY}")
        
