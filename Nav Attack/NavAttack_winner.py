from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from NavAttack_config import config
from datetime import date
import sys


def winner(dificulty, score, t):
    resulx, resuly = 1280, 720
    window = Window(resulx, resuly)
    background = Sprite("victory_screen.jpg")

    ranking = open("ranking.txt", "a")

    name = ""
    n = 0

    music_victory = Sound("Winn_music.ogg")
    music_victory.set_volume(30)

    if(t == 1):
        music_victory.play()

    if(dificulty == 0):
        dificulty = "Facil"
    elif(dificulty == 1):
        dificulty = "Medio"
    else:
        dificulty = "Dificil"

    clock = pygame.time.Clock()

    meteor = Sprite("animated_asteroid2.png", 16)
    meteor.set_total_duration(500)
    data = date.today()

    while(True):
        clock.tick(window.delta_time()*1000)

        background.draw()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if(event.key >= 97 and event.key <= 122 and n < 10 or event.key >= 48 and event.key <= 57 and n < 10 ):
                    name += chr(event.key)
                    n += 1
                elif(event.key == K_BACKSPACE and n > 0):
                    name = name[:-1]
                    n -= 1
                elif(event.key == K_RETURN and n > 0):
                    ranking.writelines((name.upper()+" ",  str(score)+" ",  dificulty+" ", data.strftime('%d/%m/%Y')+" ", '\n'))
                    ranking.close()
                    music_victory.stop()
                    return


        window.draw_text(name.upper(), window.width/2-160, window.height/2+25 , 30, (154,205,50), "Arial Black", False, False)
        window.draw_text(str(score), window.width/2-400, window.height/2-180 , 30, (218,165,32), "Arial Black", True, False)
        window.draw_text(dificulty, window.width/2+340, window.height/2-180 , 30, (218,165,32), "Arial Black", True, False)


        meteor.draw()
        meteor.update()
        window.update()


