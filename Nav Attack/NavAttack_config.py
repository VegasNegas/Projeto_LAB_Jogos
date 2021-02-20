from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *


def config(sound_menu, t, dificulty, choice, som):

    resulx, resuly = 1280,720
    window = Window(resulx ,resuly)
    background = Sprite("fundo2.jpg")
    Menu_image = GameImage("Menu_configuracao-1.png")

    if(t == 1):
        icon_sound = Sprite("volume-on.png")

    else:
        icon_sound = Sprite("Sound_mute.png")
    icon_sound.x = window.width/2+110
    icon_sound.y = window.height/4+20

    if(som > 0):
        icon_som = Sprite("volume-on.png")
    else:
        icon_som = Sprite("Sound_mute.png")
    icon_som.x = icon_sound.x
    icon_som.y = window.height/2-45

    mouse = Window.get_mouse()
    keyboard = window.get_keyboard()

    mouse_sp = Sprite("Tiro.png")

    stars = Sprite("Stars2.png")
    stars.x = 0
    stars2 = Sprite("Stars2.png")
    stars2.x = resulx

    seta1 = GameImage("Seta.png")
    seta1.x = window.width/2-180
    seta1.y = window.height/4+320
    seta2 = GameImage("Seta2.png")
    seta2.x = window.width/2+120
    seta2.y = seta1.y


    dificulty_easy = GameImage("Dificuldade_facil.png")
    dificulty_easy.x = window.height/2 + dificulty_easy.height + 120
    dificulty_easy.y = seta1.y
    dificulty_medio = GameImage("Dificuldade_medio.png")
    dificulty_medio.x = dificulty_easy.x
    dificulty_medio.y = dificulty_easy.y
    dificulty_dificil = GameImage("Dificuldade_dificil.png")
    dificulty_dificil.x = dificulty_easy.x
    dificulty_dificil.y = dificulty_easy.y

    dificults = ["dificulty_easy", "dificulty_medio", "dificulty_dificil"]

    k = 0
    delay = 0
    speed_per_FRAME = 30

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

        if(keyboard.key_pressed("ESC")):
            return (sound_menu, t, dificulty, choice, som)

        x, y = mouse.get_position()

        mouse_sp.x = x
        mouse_sp.y = y

        if(mouse.is_button_pressed(1) == True and icon_sound.collided(mouse_sp) == True and delay == 0):
            delay = speed_per_FRAME
            if(t == 1):
                t = 0
                sound_menu.stop()
                icon_sound = Sprite("Sound_mute.png")
            else:
                t = 1
                sound_menu.play()
                icon_sound = Sprite("volume-on.png")

            icon_sound.x = window.width/2+110
            icon_sound.y = window.height/4+20

        if(mouse.is_button_pressed(1) == True and icon_som.collided(mouse_sp) == True and delay == 0):
            delay = speed_per_FRAME
            if(som >= 1):
                som = 0
                icon_som = Sprite("Sound_mute.png")
            else:
                som = 5
                icon_som = Sprite("volume-on.png")

            icon_som.x = icon_sound.x
            icon_som.y = window.height/2-45



        if(choice == 0):
            if(mouse.is_button_pressed(1) and seta1.collided(mouse_sp) and delay == 0):
                delay = speed_per_FRAME
                dificulty = dificulty-1
                if(dificulty < 0):
                    dificulty = 2
                if(dificults[dificulty] == "dificulty_easy"):
                    dificulty = 0
                elif(dificults[dificulty] == "dificulty_medio"):
                    dificulty = 1
                else:
                    dificulty = 2

            if(mouse.is_button_pressed(1) and seta2.collided(mouse_sp) and delay == 0):
                delay = speed_per_FRAME
                dificulty = dificulty+1
                if(dificulty > 2):
                    dificulty = 0
                if(dificults[dificulty] == "dificulty_easy"):
                    dificulty = 0
                elif(dificults[dificulty] == "dificulty_medio"):
                    dificulty = 1
                else:
                    dificulty = 2

        Menu_image.draw()
        icon_sound.draw()
        icon_som.draw()
        #window.draw_text("Musica:", window.width/2-150, window.height/4, 38, (0,0,0), "Arial Black", False, False)
        #window.draw_text("Dificuldade:", window.width/2-150, window.height/4+110, 38, (0,0,0), "Arial Black", False, False)
        seta1.draw()
        seta2.draw()

        if(dificulty == 0):
            dificulty_easy.draw()
        elif(dificulty == 1):
            dificulty_medio.draw()
        elif(dificulty == 2):
            dificulty_dificil.draw()

        window.update()

        if(delay > 0):
            delay -= 1
