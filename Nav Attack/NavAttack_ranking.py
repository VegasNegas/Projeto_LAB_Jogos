from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from operator import itemgetter
import random

def ranking():

    resulx, resuly = 1280,720
    window = Window(resulx, resuly)
    background = GameImage("fundo2.jpg")
    menu_image = GameImage("Ranking_menu.png")

    keyboard = window.get_keyboard()

    stars = Sprite("Stars2.png")
    stars.x = 0
    stars2 = Sprite("Stars2.png")
    stars2.x = resulx

    ranking_list = open("ranking.txt", "r")

    lst = []

    for linha in ranking_list:
        lst.append(linha.split(" "))
    for elem in lst:
        elem[1] = int(elem[1])
    lst.sort(key=itemgetter(1), reverse=True)

    while(len(lst)>10):
        lst.remove(lst[-1])

    while(True):
        background.draw()
       ############# ANIMAÇÃO BACKGROUND ##########



        if(stars.x >= -window.width*2):
            stars.x -= 2
            if(stars.x == -window.width):
                stars2.x = window.width

        if(stars.x <= -window.width or stars2.x <= -window.width):
            stars2.x -= 2
            if(stars2.x == -window.width):
                stars.x = window.width

        stars2.draw()
        stars.draw()
        #############################################

        menu_image.draw()

        r, g, b = random.randint(100,255), random.randint(100,255), random.randint(100,255)

        posi_y = [window.height/3.2+25, window.height/3.2+65, window.height/3.2+105, window.height/3.2+145, window.height/3.2+185, window.height/3.2+225, window.height/3.2+265, window.height/3.2+305, window.height/3.2+350, window.height/3.2+395]
        i = 0

        for rankings in lst:
            window.draw_text(str(i+1)+" "+str(rankings[0]), window.width/2-360, posi_y[i] , 30, (r, g ,b), "Arial Black", False, False)
            window.draw_text(str(rankings[1]), window.width/2-100, posi_y[i] , 30, (r, g, b), "Arial Black", False, False)
            window.draw_text(str(rankings[2]), window.width/2+50, posi_y[i] , 30, (r, g, b), "Arial Black", False, False)
            window.draw_text(str(rankings[3]), window.width/2+200, posi_y[i] , 30, (r, g, b), "Arial Black", False, False)
            i+=1

        if(keyboard.key_pressed("ESC")):
            ranking_list.close()
            return

        window.update()

#ranking()
