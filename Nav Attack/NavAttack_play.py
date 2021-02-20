from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from NavAttack_config import config
from NavAttack_play_2 import play_2
import math
import random
import sys


def play(dificulty, t, som):

    def tiro_boss(cooldown):
        if(cooldown == 0 and len(shot1) == 0):
            sound_shot_1.play()
            cooldown = 60 - (dificulty*10)
            for i in range(3):
                shot1.append(Sprite("tiro_boss1-2.png", 6))
                shot1[i].set_total_duration(300)

            shot1[0].x, shot1[0].y = boss.x, boss.y + boss.height/2
            shot1[1].x, shot1[1].y = shot1[0].x, shot1[0].y + 250
            shot1[2].x, shot1[2].y = shot1[0].x, shot1[0].y - 250
        return cooldown

    def tiro_boss2(cooldown_shot2):
        angle_shot = 0
        if(cooldown_shot2 == 0 and len(shot2) == 0):
            sound_shot_2.play()
            cooldown_shot2 = 60
            for i in range(40):
                shot2.append(Sprite("energy_ball_shot.png", 4))
                shot2[i].set_total_duration(120)
                shot2[i].x, shot2[i].y = boss.width/2 + boss.x, boss.height/2 + boss.y

                angle_shotX.append(math.cos(angle_shot/45*math.pi))
                angle_shotY.append(math.sin(angle_shot/45*math.pi))
                angle_shot += random.randint(1,6)
                if(angle_shot == 360):
                    angle_shot = 0
        return cooldown_shot2

    def tiro_boss3(cooldown_shot3):
        if(cooldown_shot3 == 0 and len(shot3) == 0):
            cooldown_shot3 = 300
            shot3.append(Sprite("lase_shot_boss.png", 8))
            shot3[0].set_total_duration(900)
            shot3[0].x = boss.x - shot3[0].width
            shot3[0].y = boss.height/2 + boss.y
        return cooldown_shot3


    def enemy_spawn():
        n = random.randint(3,6)
        for i in range(n):
            enemys.append(Sprite("enemy-test.png", 25))
            enemys_shot.append(Sprite("shot_enemy.png", 5))

            enemys[i].x = resulx + 100 + random.randint(50,200)
            enemys[i].y = random.randint(-200,200) + resuly/2 + (n * 10)

            enemys_shot[i].x = enemys[i].x
            enemys_shot[i].y = enemys[i].y

            enemys[i].set_total_duration(300)

    def enemy_remove():
        enemys_destroys.append(Sprite("enemy_explosion.png", 20))
        for enemy2 in enemys_destroys:
            enemy2.x = enem.x - enem.width/2 +10
            enemy2.y = enem.y - enem.height - 20
            enemy2.set_total_duration(1000)

    def pause(n):
        while(True):
            mouse_sp.x, mouse_sp.y = mouse.get_position()
            if(keyboard.key_pressed("ESC") and n == 0):
                menu_pause_sound.play()
                break
            if(exit_button.collided(mouse_sp) and n == 0 and mouse.is_button_pressed(1)):
                return 0
            if(config_button_pause.collided(mouse_sp) and n == 0 and mouse.is_button_pressed(1)):
                return 1

            config_button_pause.draw()
            exit_button.draw()
            window.update()
            if(n > 0):
                n -= 1

    def gameover():
        while(True):
            if(keyboard.key_pressed("ESC")):
                break

            window.draw_text("Game Over", window.width/2-250, 20, 80, (255,255,225), "Arial Black", True, False)
            window.update()

    def win():
        level_1_sound.stop()
        background_level_complet = Sprite("Winner.jpg")
        victory_sound.play()
        while(True):
            nave.draw()
            background_level_complet.draw()
            if(keyboard .key_pressed("ENTER")):
                victory_sound.stop()
                play_2(dificulty, life_hero, score, t, choice, som)
                break
            window.update()

    def change_sound_efect():
        laser_shot_sound.set_volume(som)
        enemy_explo_sound.set_volume(som)
        victory_sound.set_volume(som)
        menu_pause_sound.set_volume(som)
        sound_shot_2.set_volume(som)
        sound_shot_1.set_volume(som)

    resulx, resuly = 1280,720
    window = Window(resulx, resuly)
    background = Sprite("fundo_spaceWar2.jpg")
    background.x = 0
    background.y = 0
    menu_backgroud = GameImage("Menu_pause_backgroud.png")
    game_over_background = GameImage("tela_game_over.png")

    level_1_sound = Sound("fase1_sound.wav")
    level_1_sound.set_volume(5)
    if(t == 1):
        level_1_sound.play()


    keyboard = Window.get_keyboard()
    mouse = Window.get_mouse()
    mouse_sp = Sprite("Tiro.png")

################################## HERO #######################################
    nave = Sprite("nave-1.png")
    nave.x = 0
    nave.y = window.height/2
    nave_boost = Sprite("nave-2-1.png")
    nave_boost.y = nave.y
    nave_boost.x = nave.x
    velnave = 200
    shots = []
    shot_speed = 500
    laser_shot_sound = Sound("laser_shot.wav")
    laser_shot_sound.set_volume(som)
    life_hero = 30-(dificulty*(dificulty+5))
###############################################################################


################################### HUD #######################################
    background_bar_life = Sprite("barra2.png")
    background_bar_life.x = window.width/2-509
    background_bar_life.y = 23.7
###############################################################################


############################## MENU PAUSE #####################################
    config_button_pause = Sprite("button_pause_config.png")
    config_button_pause.x = window.width/2-100
    config_button_pause.y = window.height/2-100

    exit_button = Sprite("Button_pause_sair.png")
    exit_button.x = window.width/2-150
    exit_button.y = window.height/2+100
###############################################################################


################################# ENEMYS ######################################
    enemys = []
    enemys_destroys = []
    enemys_shot = []
    vel_shot_enemy = 220+(dificulty*10+60)
    vel_enemy = 150+(dificulty*10+60)
    enemy_explo_sound = Sound("hit_explos.ogg")
    enemy_explo_sound.set_volume(som)
###############################################################################


################################## BOSS #######################################
    boss = Sprite("boss1.png")
    boss.x = resulx
    boss.y = window.height/2 - boss.height/2
    life_boss = 30 + (dificulty*10)
    vel_boss = 50


    shot1 = []
    cooldown = 60
    velshot1 = 200 + (50*dificulty)
    sound_shot_1 = Sound("sound_shot1_boss_1.wav")
    sound_shot_1.set_volume(som)

    shot2 = []
    cooldown_shot2 = 60
    velshot2 = 350 + (50*dificulty)
    angle_shotX = []
    angle_shotY = []
    sound_shot_2 = Sound("sound_shot2_boss_1.wav")
    sound_shot_2.set_volume(som)

    #shot3 = []
    #cooldown_shot3 = 120
################################################################################

    victory_sound = Sound("victory.ogg")
    victory_sound.set_volume(som)

    menu_pause_sound = Sound("menu_pause.wav")
    menu_pause_sound.set_volume(som)

    delay = 0
    speed_per_FRAME = 60
    score = 0
    choice = 1

    while(True):
        a = 0

        mouse_sp.x, mouse_sp.y = mouse.get_position()

        if(background.x >= -background.width+1280):
            background.x -= 0.5
        background.draw()

        if(keyboard.key_pressed("UP")):
            if(nave.y > 100):
                nave.y -= velnave * window.delta_time()
                nave_boost.y = nave.y
        if(keyboard.key_pressed("DOWN")):
            if(nave.y+nave.height < window.height):
                nave.y += velnave * window.delta_time()
                nave_boost.y = nave.y
        if(keyboard.key_pressed("LEFT")):
            if(nave.x > 0):
                nave.x -= velnave *window.delta_time()
                nave_boost.x = nave.x-38
        if(keyboard.key_pressed("RIGHT")):
            if(nave.x + nave.width < window.width):
                nave.x += velnave * window.delta_time()
                nave_boost.x = nave.x-38
                nave_boost.draw()
                a = 1

        if(a == 0):
            nave.draw()

        if(keyboard.key_pressed("ESC") and delay == 0):
            delay = speed_per_FRAME
            menu_pause_sound.play()
            menu_backgroud.draw()
            option = pause(delay)

            if(option == 0):
                level_1_sound.stop()
                return t
            if(option == 1):
                level_1_sound, t, dificulty, choice, som = config(level_1_sound, t, dificulty, choice, som)
                change_sound_efect()

        if(keyboard.key_pressed("SPACE")):
            if(delay == 0):
                laser_shot_sound.play()
                delay = speed_per_FRAME
                shot = Sprite("tiro_hero.png")
                shot.x = nave.x+nave.width-10
                shot.y = nave.y+nave.height/2-10

                shots.append(shot)

        for sh in shots:
            sh.move_x(1 * shot_speed * window.delta_time())
            if(sh.x > window.width):
                shots.remove(sh)
            elif(boss.collided_perfect(sh)):
                life_boss -= 1
                shots.remove(sh)

        for tiros2 in shots:
            tiros2.draw()


################################## ENEMY BATTLE ##################################
        if(len(enemys) == 0 and background.x >= -background.width+1280):
            enemy_spawn()
        else:
            for enem in enemys:
                enem.move_x(-1*window.delta_time()*vel_enemy)
                enem.draw()
                enem.update()
                if(enem.x < 0-enem.width):
                    enemys.remove(enem)
                for shotss in shots:
                    if(shotss.collided(enem)):
                        enemy_explo_sound.play()
                        enemy_remove()
                        enemys.remove(enem)
                        shots.remove(shotss)
                        score += 100 +(dificulty * 50)

            for shts in enemys_shot:
                shts.set_total_duration(1000)
                shts.move_x(-1*window.delta_time()*vel_shot_enemy)
                shts.draw()
                shts.update()
                if(shts.x < 0):
                    enemys_shot.remove(shts)
                if(nave.collided(shts)):
                    life_hero -= 1
                    enemys_shot.remove(shts)

            for enem in enemys_destroys:
                enem.move_x(-1*window.delta_time()*vel_enemy)
                enem.draw()
                enem.update()
                if(enem.get_curr_frame() == 19):
                    enemys_destroys.remove(enem)
#####################################################################################


################################## BOSS BATTLE ######################################
        boss.draw()

        if(background.x <= -background.width+1280):
            if(boss.x != window.width-boss.width):
                boss.x -= 1.5
            else:
                if(boss.y + boss.height/2 < nave.y):
                    if(boss.y + boss.height < window.height):
                        boss.move_y(1 * window.delta_time() * vel_boss)
                if(boss.y + boss.height/2 > nave.y):
                    if(boss.y > 0):
                        boss.move_y(-1 * window.delta_time() * vel_boss)

                if(cooldown > 0 and len(shot1) == 0):
                    cooldown -= 1
                cooldown = tiro_boss(cooldown)
                for shots_boss1 in shot1:
                    shots_boss1.move_x(-1*window.delta_time()*velshot1)
                    shots_boss1.draw()
                    shots_boss1.update()
                    if(shots_boss1.collided(nave)):
                        shot1.remove(shots_boss1)
                        life_hero -= 5

                    elif(shots_boss1.x < 0-shots_boss1.width):
                        shot1.remove(shots_boss1)

                if(cooldown_shot2 > 0 and len(shot2) == 0):
                    cooldown_shot2 -= 1
                cooldown_shot2 = tiro_boss2(cooldown_shot2)

                for shots_boss2 in shot2:
                    shots_boss2.move_x(angle_shotX[shot2.index(shots_boss2)]*window.delta_time()*velshot2)
                    shots_boss2.move_y(angle_shotY[shot2.index(shots_boss2)]*window.delta_time()*velshot2)
                    shots_boss2.draw()
                    shots_boss2.update()
                    if(shots_boss2.x < 0 or shots_boss2.y < 0 or shots_boss2.x > window.width or shots_boss2.y > window.height):
                        angle_shotX.remove(angle_shotX[shot2.index(shots_boss2)])
                        angle_shotY.remove(angle_shotY[shot2.index(shots_boss2)])
                        shot2.remove(shots_boss2)
                    elif(shots_boss2.collided_perfect(nave)):
                        angle_shotX.remove(angle_shotX[shot2.index(shots_boss2)])
                        angle_shotY.remove(angle_shotY[shot2.index(shots_boss2)])
                        shot2.remove(shots_boss2)
                        life_hero -= 1

                #if(cooldown_shot3 > 0 and len(shot3) == 0):
                    #cooldown_shot3 -= 1
                #cooldown_shot3 = tiro_boss3(cooldown_shot3)
                #if(len(shot3) > 0):
                   #shot3[0].y = boss.y/2
                    #shot3[0].draw()
                    #shot3[0].update()
                    #if(cooldown_shot3 > 230):
                        #cooldown_shot3 -= 1
                    #else:
                        #shot3.remove(shot3[0])
                if(nave.collided_perfect(boss)):
                    life_hero -= 5

                window.draw_text("|"*life_boss, boss.x + 20, boss.y - 30, 25, (255,0,0), "Arial Black", False, False)
                if(life_boss <= 0):
                    score +=100 +(dificulty * 50)
                    win()
                    break

#####################################################################################


        background_bar_life.draw()
        window.draw_text("|"*life_hero, window.width/2-500, 20, 25, (255,0,0), "Arial Black", False, False)
        window.draw_text(str(score), window.width/2-70, 20, 40, (255,255,225), "Arial Black", True, False)

        window.update()

        if(life_hero <= 0):
            delay = speed_per_FRAME
            game_over_background.draw()
            level_1_sound.stop()
            music_boss.stop()
            gameover()
            return

        if(delay > 0):
            delay -= 1
