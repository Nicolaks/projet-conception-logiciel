try:
    import os
    import sys
    import time
    import tkinter
    import json
    import pygame
    from pygame.locals import *
    import random as rd
    import sympy as sp
    import threading

    import WavesOBJ as Wvs

    import pre_settings.Settings as Settings

    import Entity.Reactor as Rct
    import Entity.EntityGroup as ENTGroup
    import Entity.SpaceShip as spaceShip
    import Entity.Ally as Ally
    import Entity.Bullet as Blt
    
    import Animation.scrolling as scroll
    import Animation.UI as UI

    import Menu.button as btn
    import Menu.GameOver as Dead

    import Upgrade.Power_ups as PU
    import Upgrade.Shop as SHOP

    import Animation.CollideAnimate as ColAnimate

except ImportError as error:
    print(error.__class__.__name__ + " : " + error.msg)
    sys.exit(0)

def loading_phase(list_images, fps, Window, width, height):
    now = pygame.time.get_ticks()
    t = 0
    t2 = 0
    n = len(list_images)-1
    time = now
    time2 = now

    police = pygame.font.Font(os.path.join("..","Ressources","Police","Adventure","Adventure.otf"), int(25))

    one = "Une jeu créé par"
    two = "Ragot David"
    three = "Aubry Nicolas"
    four = "Bertier Théo"
    five = "En partenariat avec"
    six = "La licence informatique"
    seven = "Dans le cadre de l'UE"
    eight = "Conception Logicielle"
    nine = "Vous présente :"
    ten = "PS : Nous n'avons pas utilisé ce temps pour chargé tout notre contenu"

    listTXT = [one,two,three,four,five,six,seven,eight,nine,ten]

    Color_i = [255,255,255]
    Color = Color_i

    while True:

        now = pygame.time.get_ticks()
        if t == n:
            t=0
        Window.blit(list_images[t],(0,0))

        Color = [x-1 for x in Color]
        if Color == [0,0,0]:
            Color = Color_i
            t2 += 1
        if t2 > len(listTXT)-1:
            return
        else:
            txt = police.render(listTXT[t2],True,(Color[0],Color[1],Color[2]))
            posX = width/2 - txt.get_width()/2
            posY = height/2 - txt.get_height()/2
            Window.blit(txt,(posX,posY))
        if now - time >= fps:
            time = now
            t += 1

        pygame.display.update()

def loading_background(Width,Height):
    global Background
    Background = scroll.Background(0, Width, Height)

def loading_Waves(_dict_Patern, _dict_Ennemy, _dict_Bullet_type, fps):
    global Wave_
    Wave_ = Wvs.Waves(_dict_Patern, _dict_Ennemy, _dict_Bullet_type, fps)

def Jeux(Hht, Wth):
    pygame.init()

    Set = Settings.Settings()
    Set.read()

    sound_ambiance = pygame.mixer.Sound(os.path.join("..","Ressources","Son","Ambiance_2.wav"))
    sound_ambiance2 = pygame.mixer.Sound(os.path.join("..","Ressources","Son","Ambiance_1.wav"))
    sound_shoot = pygame.mixer.Sound(os.path.join("..","Ressources","Son","SpaceShip_Shoot.wav"))
    sound_exploded = pygame.mixer.Sound(os.path.join("..","Ressources","Son","Explosion_2.wav"))
    sound_ambiance_shoot = pygame.mixer.Sound(os.path.join("..","Ressources","Son","Ambiance_tir.wav"))

    Height, Width = Hht, Wth
    if Set.file_here:
        Height = Set._dict_["Height"]  # Hauteur
        Width = Set._dict_["Width"]  # Largeur
    fps = Set._dict_["fps"]

    Window = pygame.display.set_mode((Width, Height), pygame.SRCALPHA)
    pygame.display.set_caption("Manic Shooter : Shot'em up !")
    Clock = pygame.time.Clock()
    FontFPS = pygame.font.Font(None, 30)

    sound_ambiance.play(loops=1, maxtime=0, fade_ms=0)
    
    n = len(os.listdir(os.path.join("..", "Ressources", "Loading_screen","3")))
    listIMG = []

    for i in range(1,n):
        if i<10:
            j = "0"+str(i)
        else:
            j = str(i)
        img = pygame.image.load(os.path.join("..", "Ressources",  "Loading_screen","3","frame-"+j+".gif")).convert_alpha()
        img = pygame.transform.scale(img, (Width,Height))
        listIMG.append(img)

    t1 = threading.Thread(target=loading_phase, args=(listIMG,fps,Window,Width,Height))
    t1.start()

    def load_json_to_dict(path):
        with open(path) as file:  # On récupère le fichier
            _dict_ = json.load(file)
        return _dict_

    _dict_Bullet_type = load_json_to_dict("JSON_File/Bullet_type.json")
    _dict_Bullet_type = Blt.loader_fct_bullet(_dict_Bullet_type)#Permet de creer les fonctions une seules fois, en les remplacant a leur endroit respectif dans le dictionnaire.
    
    _dict_Patern = load_json_to_dict("JSON_File/Patern.json")
    _dict_Patern = Wvs.loader_patern(_dict_Patern)

    _dict_Spaceship = load_json_to_dict("JSON_File/SpaceShip.json")
    _dict_Ennemy = load_json_to_dict("JSON_File/Ennemy.json")
    _dict_Powers_ups = load_json_to_dict("JSON_File/Power_ups.json")

    t2 = threading.Thread(target=loading_Waves, args=(_dict_Patern, _dict_Ennemy, _dict_Bullet_type, fps))
    t3 = threading.Thread(target=loading_background, args=(Width,Height))

    t3.start()
    t2.start()

    __GroupBullet_Ally = ENTGroup.Entity()#A mettre en variables du vaisseau

    UIn = UI.ui()    #UI = User Interface
    Power_UP = PU.Power_ups(_dict_Powers_ups)

    Spaceship = Ally.allyShip(_dict_Spaceship, UIn.width)
    #Spaceship.bullet_type = ""
    Spaceship.Reactor_innit()
    GameOver = Dead.GameOver(Height,Width)

    Shop = SHOP.shop(Window, Spaceship,_dict_Spaceship, _dict_Bullet_type, _dict_Powers_ups)
    GrShop = ENTGroup.Entity()
    GrShop.add(Shop)

    t2.join()

#########################Police###########################
    police = pygame.font.SysFont("monospace", 50)
    policeCopyright = pygame.font.SysFont("arial", 12)
##########################################################
###################################MENU_ HOME#############
    textTitre = police.render("Manic Shooter:", True, (255,255,255))
    textCopyright = policeCopyright.render("© Développé par Aubry Nicolas, Ragot David et Berthier Théo", True, (255,255,255))
    placementTexteTitre = (Width/2) - (textTitre.get_width()/2)
    btnJouer = btn.Button(150,60, (144,88,41), "JOUER", 450, Width, Window)#Ajoute un bouton jouer.
    btnSettings = btn.Button(240,60, (144,88,41), "SETTINGS", 700, Width, Window)#Ajoute un bouton settings.
    btnQuitter_1 = btn.Button(210,60, (144,88,41), "QUITTER", 950, Width, Window)#Ajoute un bouton quitter.
##########################################################
###########################MENU_SAVE######################
    txtSave = police.render("CHOIX DE LA SAUVEGARDE", True, (255,255,255))
    placementTxtSave = (Width/2) - (txtSave.get_width()/2)
    btnSave1 = btn.Button(360,60, (144,88,41), "SAUVEGARDE 1", 450, Width, Window)#Ajoute un bouton pour la Sauvegrade une 
    btnSave2 = btn.Button(360,60, (144,88,41), "SAUVEGARDE 2", 700, Width, Window)#Ajoute un bouton pour la deuxième sauvegarde
    btnSave3 = btn.Button(360,60, (144,88,41), "SAUVEGARDE 3", 950, Width, Window)#Ajoute un bouton pour la troisième sauvegarde
    btnQuitter_2 = btn.Button(210,60, (144,88,41), "Retour", 1200, Width, Window)#Ajoute un bouton quitter.
##########################################################
##########################MENU_DIFF#######################
    txtDiff = police.render("Choix de la difficulté", True, (255,255,255))
    placementTxtDiff = (Width/2) - (txtDiff.get_width()/2)
    btnFacile = btn.Button(180,60, (144,88,41), "FACILE", 450, Width, Window)#Ajoute un bouton pour la difficulté facile
    btnNormal = btn.Button(180,60, (144,88,41), "NORMAL", 700, Width, Window)#Ajoute un bouton pour la difficulté normal
    btnDiff = btn.Button(270,60, (144,88,41), "DIFFICILE", 950, Width, Window)#Ajoute un bouton pour la difficulté difficile
    btnQuitter_3 = btn.Button(210,60, (144,88,41), "Retour", 1200, Width, Window)#Ajoute un bouton quitter.
##########################################################
    
    t1.join()
    t3.join()

    t1._stop()
    t2._stop()
    t3._stop()

    continuer = True

    Game = False

    Menu_Home = True
    Menu_Profile = False
    Menu_Difficulty = False

    Temps_ecoule = 0
    sound_ambiance.fadeout(250)
    sound_ambiance2.play(loops=1, maxtime=0, fade_ms=0)
    while continuer:
        #Window.blit(Background, (0,0))
        x,y = (0,0)
        #Window.fill(BLACK)
        delta_time = Clock.tick(fps) * 0.001 #En ms -> x0.001 pour mettre en seconde et delta time : c'est le temps entre 2 images.
        FPS = Clock.get_fps()

        pressed = pygame.key.get_pressed()
        buttons = {pygame.key.name(k) for k,v in enumerate(pressed) if v}#Recupère le nom des touches PRESSE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
    
        if Menu_Home:

            Window.fill((153,77,0))#Donne une couleur de fond a la page.
            btnJouer.draw()
            btnJouer.afficherTexte(btnJouer.txtPlacement_x,btnJouer.txtPlacement_y)
            btnSettings.draw()
            btnSettings.afficherTexte(btnSettings.txtPlacement_x,btnSettings.txtPlacement_y)
            btnQuitter_1.draw()
            btnQuitter_1.afficherTexte(btnQuitter_1.txtPlacement_x, btnQuitter_1.txtPlacement_y)
            Window.blit(textTitre, (placementTexteTitre, 30))
            Window.blit(textCopyright, (450,850))

            if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 150/2) and x < (Width/2 + 150/2):
                Menu_Profile = True
                Menu_Home = False
            if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 240/2) and x < (Width/2 + 240/2):
                print("OK")
            if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                continuer = False
            x,y = (0,0)
        if not Menu_Home and Menu_Profile:

            Window.fill((153,77,0))#Donne une couleur de fond a la page.
            btnSave1.draw()
            btnSave1.afficherTexte(btnSave1.txtPlacement_x,btnSave1.txtPlacement_y)
            btnSave2.draw()
            btnSave2.afficherTexte(btnSave2.txtPlacement_x,btnSave2.txtPlacement_y)
            btnSave3.draw()
            btnSave3.afficherTexte(btnSave3.txtPlacement_x, btnSave3.txtPlacement_y)
            btnQuitter_2.draw()
            btnQuitter_2.afficherTexte(btnQuitter_2.txtPlacement_x, btnQuitter_2.txtPlacement_y)
            Window.blit(txtSave, (placementTxtSave, 30))

            if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                Profile = "profile1"
                Menu_Profile = False
                Menu_Difficulty = True
            if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                Profile = "profile2"
                Menu_Profile = False
                Menu_Difficulty = True
            if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                Profile = "profile3"
                Menu_Profile = False
                Menu_Difficulty = True
            if y > 1200/2 and y < 1200/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                Menu_Profile = False
                Menu_Home = True
            x,y = (0,0)
        if not Menu_Home and not Menu_Profile and Menu_Difficulty:

            Window.fill((153,77,0))#Donne une couleur de fond a la page.
            btnFacile.draw()
            btnFacile.afficherTexte(btnFacile.txtPlacement_x,btnFacile.txtPlacement_y)
            btnNormal.draw()
            btnNormal.afficherTexte(btnNormal.txtPlacement_x,btnNormal.txtPlacement_y)
            btnDiff.draw()
            btnDiff.afficherTexte(btnDiff.txtPlacement_x, btnDiff.txtPlacement_y)
            btnQuitter_3.draw()
            btnQuitter_3.afficherTexte(btnQuitter_3.txtPlacement_x, btnQuitter_3.txtPlacement_y)
            Window.blit(txtDiff, (placementTxtDiff, 30))

            if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 180/2) and x < (Width/2 + 180/2):
                Wave_.difficulty = 15
                Game = True
                Menu_Difficulty = False
            if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 180/2) and x < (Width/2 + 180/2):
                Wave_.difficulty = 10
                Game = True
                Menu_Difficulty = False
            if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 270/2) and x < (Width/2 + 270/2):
                Wave_.difficulty = 5
                Game = True
                Menu_Difficulty = False
            if y > 1200/2 and y < 1200/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                Menu_Profile = True
                Menu_Difficulty = False
            x,y = (0,0)
        if Game:
            Temps_ecoule += delta_time
            if len(buttons) >=1 and Wave_.first_press_key != None and Temps_ecoule >= 2:
                Wave_.first_press_key = True
                Wave_.startGame()
            
            if Set._dict_["up"] in buttons:
                Spaceship.up()
            if Set._dict_["down"] in buttons:
                Spaceship.down()
            if Set._dict_["left"] in buttons:
                Spaceship.left()
            if Set._dict_["right"] in buttons:
                Spaceship.right()
            if not Wave_.Pause:
                if Set._dict_["s_shoot"] in buttons:
                    now = pygame.time.get_ticks()
                    if now - Spaceship.bullet_last_hit >= _dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["Cooldown"]:
                        sound_shoot.play()
                        for i in range(_dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["n"]):
                            Bullet = Blt.bullet(Spaceship, _dict_Bullet_type, i)
                            __GroupBullet_Ally.add(Bullet)
                        Spaceship.bullet_last_hit = now

            if 'escape' in buttons:
                Menu_Home=True
                Game=False

            if 'f' in buttons and 'i' in buttons and 'n' in buttons:
                pygame.quit()
                quit()

            if Shop.drawIt:
                Shop.clic(Spaceship,_dict_Spaceship, _dict_Bullet_type, _dict_Powers_ups,x,y, Power_UP)
            if Spaceship.life <= 0 and Wave_.Pause:
                GameOver.clic(x,y)

            Background.update(Wave_.wave,Wave_.Pause)
            Wave_.update(delta_time, __GroupBullet_Ally, Spaceship, Power_UP.Group, Shop)
            if not Wave_.Pause and not Wave_.end_patern:
                Power_UP.update(Wave_.wave, _dict_Powers_ups)
                __GroupBullet_Ally.update(delta_time)
            UIn.update(Wave_.score, Wave_.wave, Spaceship.money)
            Background.draw(Window)#Order draw = 1
            Power_UP.draw(Window)#Order draw = 2
            Wave_.draw(Window)#Order draw = 3
            __GroupBullet_Ally.draw(Window)#Order draw = 4
            
            if Spaceship.life>0:
                Spaceship.draw(Window)
            Wave_.GroupCollide_Bullet.draw(Window)
            Wave_.Group_Explode.draw(Window)

            Shop.update_pos_draw(Window)
            if not Shop.inited:

                collide = pygame.sprite.spritecollide(Spaceship, GrShop, False, pygame.sprite.collide_mask)
                if len(collide) > 0:
                    Shop.drawIt = True
            
            if Shop.drawIt:
                Wave_.Pause = True
                Shop.update(Spaceship,_dict_Spaceship, _dict_Bullet_type, _dict_Powers_ups)
                Shop.draw(Window)#Order draw = 5 bis
                if Shop.done:
                    now = pygame.time.get_ticks()
                    if now - Wave_.begin >= 2000:
                        Shop.done = False
                        Shop.drawIt = False
                        Wave_.Pause = False
                        Wave_.start = 0
            
            if Spaceship.life <= 0:
                Spaceship.life = 0
                Wave_.Pause = True
                Wave_.GroupBullet_Ennemy.empty()
                Wave_.GroupSHIP.empty()
                __GroupBullet_Ally.empty()
                Power_UP.Group.empty()
                if len(Wave_.Group_Explode.sprites()) == 0:
                    pos_mouse = pygame.mouse.get_pos()
                    x_pos, y_pos = pos_mouse[0], pos_mouse[1]
                    GameOver.update(x_pos,y_pos)
                    GameOver.draw(Window)
                    if GameOver.menu:
                        Game = False
                        Menu_Home = True
                    if GameOver.rejouer:
                        Wave_.Pause = False
                        Temps_ecoule = 0
                        Wave_.wave = 1
                        Wave_.numbers_ennemy_init()
                        Wave_.patern_choose()
                        Spaceship.upgrade_style_performance(1,_dict_Spaceship)
                    if GameOver.quitter:
                        pygame.quit()
                        quit()
                    x,y = (0,0)


            UIn.draw(Window, Spaceship, Wave_)#Order draw = 6

            fps_render = FontFPS.render("FPS : {}".format(int(FPS)), True, (255, 255, 255))
            nb_sprites = len(Wave_.GroupSHIP.sprites())
            counter_render = FontFPS.render("NBs : {}".format(nb_sprites),
                True, (255, 255, 255))

            Time = FontFPS.render("Time : {0:.2f}".format(float(Temps_ecoule)), True, (255, 255, 255))
            Speed = FontFPS.render("speed : {}".format(int(Spaceship.__speed__)), True, (255, 255, 255))
            dmg = FontFPS.render("dmg : {}".format(int(Spaceship.damage + _dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["damage"])), True, (255, 255, 255))


            Window.blit(fps_render, (100, 100))
            Window.blit(Speed, (100, 150))
            Window.blit(Time, (100, 200))
            Window.blit(dmg, (100, 250))

        pygame.display.update()
    pygame.quit()
    quit()