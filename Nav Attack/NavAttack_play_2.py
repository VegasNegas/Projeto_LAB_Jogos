from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from NavAttack_config import config
from NavAttack_winner import winner
import math
import random
import sys


def play_2(dificulty, life_hero, score, t, choice, som):

    def tiro_boss():
        cooldown = 300

        shot1.append(Sprite("missel_boss.png", 10))
        shot1[0].set_total_duration(600)
        shot1[0].x = boss.x
        shot1[0].y = boss.y + boss.height/2 - shot1[0].height/2

        return cooldown

    def tiro_boss2(cooldown_shot2):
        angle_shot = 0
        if(cooldown_shot2 == 0 and len(shot2) == 0):
            sound_shot_2.play()
            cooldown_shot2 = 60
            for i in range(30):
                shot2.append(Sprite("energy_ball_shot_2.png", 4))
                shot2[i].set_total_duration(120)
                shot2[i].x, shot2[i].y = boss.width/2 + boss.x, boss.height/2 + boss.y

                angle_shotX.append(math.cos(angle_shot/1*math.pi))
                angle_shotY.append(math.sin(angle_shot/10*math.pi))
                angle_shot += random.randint(1,6)
                if(angle_shot == 360):
                    angle_shot = 0
        return cooldown_shot2

    def spawn_trap():
        sort = random.randint(1+dificulty,3+dificulty)
        for i in range(sort):
            traps.append(Sprite("bomb_trap(2).png",18))

        sort_y = random.sample(range(-300, 300), sort)
        i = 0
        for trap in traps:
            trap.x = window.width + trap.width/18 + sort_y[i] + 300
            trap.y = window.height/2 + sort_y[i]
            trap.set_total_duration(800)
            i += 1


    def enemy_spawn():
        sort = random.randint(4,6)
        for i in range(sort):
            enemys.append(Sprite("enemy_level2-1.png", 7))


        sort_y = random.sample(range(-150, 300), sort)
        rand_x = [658,-124,688,410,10,62,-120,-50]
        sort_x = random.sample(rand_x,sort)
        i = 0
        for eney in enemys:
            eney.x = window.width + eney.width + sort_x[i]
            eney.y = window.height/2 + sort_y[i]

            enemys_shot.append(Sprite("shot_enemy_2.png", 5))
            enemys_shot[len(enemys_shot)-1].x = eney.x
            enemys_shot[len(enemys_shot)-1].y = eney.y
            enemys_shot[len(enemys_shot)-1].set_total_duration(800)

            eney.set_total_duration(800)
            i += 1

    def pause(n):
        while(True):
            mouse_sp.x, mouse_sp.y = mouse.get_position()
            if(keyboard.key_pressed("ESC") and n == 0):
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

    def change_sound_efect():
        laser_shot_sound.set_volume(som)
        enemy_explo_sound.set_volume(som)
        menu_pause_sound.set_volume(som)
        sound_shot_2.set_volume(som)
        sound_shot_1.set_volume(som)

        while(True):
            background_victory.draw()
            name = ""
            while(True):
                for evt in pygame.event.get():
                    if evt.type == KEYDOWN:
                        if evt.unicode.isalpha():
                            name += evt.unicode
                        elif evt.key == K_BACKSPACE:
                            name = name[:-1]
                        elif evt.key == K_RETURN:
                            name = ""
                    elif evt.type == QUIT:
                        return

            window.draw_text(name, window.width/2, window.height/2 , 25, (255,0,0), "Arial Black", False, False)

            window.update()


    resulx, resuly = 1280,720
    window = Window(resulx, resuly)
    background = Sprite("background2.jpg")
    background.x = 0
    background.y = 0
    menu_backgroud = GameImage("Menu_pause_backgroud.png")
    game_over_background = GameImage("tela_game_over.png")

    keyboard = Window.get_keyboard()
    mouse = Window.get_mouse()
    mouse_sp = Sprite("Tiro.png")

    level_2_sound = pygame.mixer.Sound("fase2_sound.wav")
    level_2_sound.set_volume(0.2)
    if(t == 1):
        level_2_sound.play()

################################# HERO ########################################
    nave = Sprite("nave-1.png")
    nave.x = 0
    nave.y = window.height/2
    nave_boost = Sprite("nave-2-1.png")
    nave_boost.y = nave.y
    nave_boost.x = nave.x
    laser_shot_sound = Sound("laser_shot.wav")
    laser_shot_sound.set_volume(som)
    velnave = 200
    shots = []
    shot_speed = 500
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
    vel_enemy = 160+(dificulty*10+60)
    enemy_explo_sound = Sound("hit_explos.ogg")
    enemy_explo_sound.set_volume(som)
###############################################################################


################################### Trap ######################################
    traps = []
    #traps_expl = []
###############################################################################


################################## BOSS #######################################
    boss = Sprite("boss2.png", 4)
    boss.set_total_duration(200)
    boss.x = resulx
    boss.y = window.height/2 - boss.height/2
    life_boss = 50 + (dificulty*10)
    vel_boss = 50
    music_boss = Sound("Final_boss_music.ogg")
    music_boss.set_volume(20)

    shot1_ex = Sprite("missel_boss_test.png")
    shot1 = []
    cooldown = 100
    velshot1 = 200 + (50*dificulty)
    shot1_destroy = []
    sound_shot_1 = Sound("sound_shot1_boss_2.wav")
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


    delay = 0
    speed_per_FRAME = 60

    menu_pause_sound = Sound("menu_pause.wav")
    menu_pause_sound.set_volume(som)


    while(True):
        a = 0
        mouse_sp.x, mouse_sp.y = mouse.get_position()


        if(background.x >= -background.width+window.width):
            current = True
        else:
            current = False

        if(current):
            background.x -= 0.5
        background.draw()


        if(keyboard.key_pressed("ESC") and delay == 0):
            delay = speed_per_FRAME
            menu_pause_sound.play()
            menu_backgroud.draw()
            option = pause(delay)

            if(option == 0):
                level_2_sound.stop()
                music_boss.stop()
                break
            if(option == 1):
                level_2_sound, t, dificulty, choice, som = config(level_2_sound, t, dificulty, 1, som)
                change_sound_efect()


################################# HERO ########################################
        if(keyboard.key_pressed("SPACE")):
            if(delay == 0):
                laser_shot_sound.play()
                delay = speed_per_FRAME
                shot = Sprite("tiro_hero.png")
                shot.x = nave.x+nave.width-10
                shot.y = nave.y+nave.height/2-10
                shots.append(shot)

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

        for sh in shots:
            sh.move_x(1 * shot_speed * window.delta_time())
            sh.draw()
            if(sh.x > window.width):
                shots.remove(sh)
            elif(current == False):
                if(boss.collided_perfect(sh)):
                    life_boss -= 1
                    shots.remove(sh)
###############################################################################


################################# TRAP SPAWN ##################################
        if(len(traps) == 0 and current):
            spawn_trap()
        elif(current or len(traps) > 0):
            for trap in traps:
                trap.draw()
                trap.move_x(-1*window.delta_time()*60)
                trap.update()
                if(nave.collided(trap)):
                    life_hero -= 3
                    traps.remove(trap)
                elif(trap.x < 0):
                    traps.remove(trap)
###############################################################################


################################## ENEMY BATTLE ###############################

        if(len(enemys) == 0 and current):
            enemy_spawn()
        elif(current or len(enemys) > 0):
            for eney in enemys:
                eney.draw()
                eney.move_x(-1*window.delta_time()*vel_enemy)
                eney.update()
                if(eney.x + eney.width < 0):
                    enemys.remove(eney)
                for shots_hero in shots:
                    if(eney.collided(shots_hero)):
                        enemy_explo_sound.play()
                        shots.remove(shots_hero)
                        enemys_destroys.append(Sprite("enemy_explosion_level_2.png", 20))
                        enemys_destroys[len(enemys_destroys)-1].x = eney.x
                        enemys_destroys[len(enemys_destroys)-1].y = eney.y - eney.height/2 - 20
                        enemys_destroys[len(enemys_destroys)-1].set_total_duration(1000)
                        enemys.remove(eney)
                        score += 150 + (dificulty * 50)

        for shot_enemy in enemys_shot:
            shot_enemy.draw()
            shot_enemy.move_x(-1*window.delta_time()*vel_shot_enemy)
            shot_enemy.update()
            if(shot_enemy.x < 0):
                enemys_shot.remove(shot_enemy)
            elif(shot_enemy.collided(nave)):
                enemys_shot.remove(shot_enemy)
                life_hero -= 2

        if(len(enemys_destroys) > 0):
            for destroys in enemys_destroys:
                destroys.move_x(-1*window.delta_time()*vel_enemy)
                destroys.draw()
                destroys.update()
                if(destroys.get_curr_frame() == 19):
                    enemys_destroys.remove(destroys)
###############################################################################



################################ BOSS BATTLE ##################################
        boss.draw()

        if(current == False):
            if(t == 1):
                level_2_sound.stop()
                music_boss.play()
            else:
                music_boss.stop()

            if(boss.x != window.width-boss.width):
                boss.x -= 1

            else:

                if(boss.y + boss.height/2 < nave.y + nave.height/2):
                    if(boss.y + boss.height < window.height):
                        boss.move_y(1 * window.delta_time() * vel_boss)
                if(boss.y + boss.height/2 > nave.y + nave.height/2):
                    if(boss.y > 0):
                        boss.move_y(-1 * window.delta_time() * vel_boss)

                if(cooldown > 0 and len(shot1) == 0):
                    cooldown -= 1
                elif(len(shot1) == 0):
                    sound_shot_1.play()
                    cooldown = tiro_boss()
                if(len(shot1) > 0):
                    shot1[0].move_x(-1*window.delta_time()*velshot1)
                    shot1_ex.draw()
                    shot1[0].draw()
                    shot1[0].update()
                    shot1_ex.x = shot1[0].x + 29
                    shot1_ex.y = shot1[0].y

                    if(shot1[0].x + shot1[0].width < 0):
                        shot1.remove(shot1[0])
                        shot1_ex.x = 0
                        shot1_ex.y = 0
                    elif(shot1_ex.collided_perfect(nave)):
                        shot1.remove(shot1[0])
                        shot1_ex.x = 0
                        shot1_ex.y = 0
                        life_hero -= 5



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
                if(nave.collided_perfect(boss)):
                    life_hero -= 5

                window.draw_text("|"*life_boss, boss.x - 130, boss.y - 30, 25, (255,0,0), "Arial Black", False, False)
                if(life_boss <= 0):
                    score += 300+(dificulty * 50)
                    music_boss.stop()
                    winner(dificulty, score, t)
                    break

        boss.update()
###############################################################################


        background_bar_life.draw()
        window.draw_text("|"*life_hero, window.width/2-500, 20, 25, (255,0,0), "Arial Black", False, False)
        window.draw_text(str(score), window.width/2-70, 20, 40, (255,255,225), "Arial Black", True, False)
        window.update()

        if(delay > 0):
            delay -= 1

        if(life_hero <= 0):
            delay = speed_per_FRAME
            game_over_background.draw()
            level_2_sound.stop()
            music_boss.stop()
            gameover()
            return

#dificulty = 2
#life_hero = 30
#score = 0
#t = 0
#som = 5
#
#
#play_2(dificulty,life_hero,score,t,1,som)
