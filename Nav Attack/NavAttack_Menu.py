from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from NavAttack_config import config
from NavAttack_play import play
from NavAttack_ranking import ranking
import sys

def main_menu(t, som):

    def mouse_button(x, y, buttons):
        for i in range(4):
            if(buttons["Menu_button_position"][i][0] <= x and buttons["Menu_button_position"][i][0]+start_button.width >= x and buttons["Menu_button_position"][i][1] <= y and buttons["Menu_button_position"][i][1]+start_button.height >= y):
                frame_button.x = buttons["Menu_button_position"][i][0]
                frame_button.y = buttons["Menu_button_position"][i][1]
                frame_button.draw()
                if(mouse.is_button_pressed(1) == True):
                    frame_button_press.x = buttons["Menu_button_position"][i][0]
                    frame_button_press.y = buttons["Menu_button_position"][i][1]
                    frame_button_press.draw()

                    return buttons["Buttons"][i]

    #Config
    resulx, resuly = 1280,720
    window = Window(resulx, resuly)
    window.set_title("NavAttack")
    sound_menu = pygame.mixer.Sound("Menu_music_8bit-adventure.wav")
    sound_menu.set_volume(0.1)
    if(t == 1):
        sound_menu.play(-1)


    #interface
    menu_back = GameImage("Menu_back3.png")
    menu_back.x = window.width/2
    menu_back.y = 0
    background = GameImage("fundo2.jpg")
    logo = GameImage("Logo-navattack.png")
    stars = Sprite("Stars2.png")
    stars.x = 0
    stars2 = Sprite("Stars2.png")
    stars2.x = resulx
    nave = Sprite("nave-2.png")
    nave.y = window.height/2
    nave.x = window.width-1240
    velnave = 50
    #meteor = Sprite("animated_asteroid2.png",16)
    #meteor.set_total_duration(2000)
    planet1 = Sprite("Planet1.png")
    planet1.x = resulx*1.2
    planet2 = Sprite("Planet2-2.png")
    planet2.x = resulx*3
    planet3 = Sprite("Planet3.png")
    planet3.x = resulx*4
    planet3.y = window.height/4

    #input
    keyboard = Window.get_keyboard()
    mouse = Window.get_mouse()

    #menu botton
    start_button = Sprite("Menu_start_button.png")
    start_button.x, start_button.y = int(window.width/2), int(window.height/4)

    config_button = Sprite("Menu_config_button.png")
    config_button.x = start_button.x
    config_button.y = start_button.y + 100

    ranking_button = Sprite("Menu_ranking_button.png")
    ranking_button.x = config_button.x
    ranking_button.y = config_button.y + 100

    exit_button = Sprite("Menu_exit_button.png")
    exit_button.x = ranking_button.x
    exit_button.y = ranking_button.y + 100

    frame_button = Sprite("Menu_Frame_button.png")
    frame_button_press = Sprite("Menu_FramePress_button.png")


    buttons_sprites = {
        "Buttons":["Start", "Config", "Ranking","Exit"],
        "Menu_buttons":["Menu_start_button.png","Menu_config_button.png","Menu_ranking_button.png","Menu_exit_button.png"],
        "Menu_button_position":[(start_button.x, start_button.y), (config_button.x, config_button.y), (ranking_button.x, ranking_button.y), (exit_button.x, exit_button.y)]
    }


    speed_per_FRAME = 30
    delay = 0
    dificulty = 0


    while(True):
        background.draw()
        x, y = mouse.get_position()

        #### Animação background ####
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

        if(planet1.x >= -window.width):
            planet1.x -= 0.5
            planet1.draw()
        elif(planet2.x >= -window.width):
            planet2.x -= 0.5
            planet2.draw()
        elif(planet3.x >= -window.width-planet3.width):
            planet3.x -= 0.5
            planet3.draw()
        else:
            planet1.x = resulx*1.2
            planet2.x = resulx*3
            planet3.x = resulx*4


        if(y < nave.y+nave.height/2):
            if(nave.y > 0):
                nave.y -= velnave*window.delta_time()
        if(y > nave.y+nave.height/2):
            if(nave.y + nave.height < window.height):
                nave.y += velnave*window.delta_time()

         ####################################

        choice = mouse_button(x, y, buttons_sprites)


        if(choice == "Start" and delay == 0):
            sound_menu.stop()
            play(dificulty, t, som)
            if(t == 1):
                sound_menu.play()
            delay = speed_per_FRAME

        if(choice == "Config" and delay == 0):
            sound_menu, t, dificulty, choice, som = config(sound_menu, t, dificulty, 0, som)
            delay = speed_per_FRAME

        if(choice == "Ranking" and delay == 0):
            ranking()
            delay = speed_per_FRAME

        if(choice == "Exit" and delay == 0):
            sys.exit()
            delay = speed_per_FRAME



        #frame_button.draw()
        #meteor.draw()
        nave.draw()
        logo.draw()
        menu_back.draw()
        start_button.draw()
        config_button.draw()
        ranking_button.draw()
        exit_button.draw()

        #meteor.update()
        window.update()
        if(delay > 0):
            delay -= 1
        if(nave.y > window.height):
            nave.y = window.height/2
som = 5
t = 1
main_menu(t, som)
