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


def menu():#Fonction menu qui sera lancée après avoir cliqué sur le bouton jouer de interface.py
    Set = Settings.Settings()
    Set.read()
    pygame.font.init()

    Height = Set._dict_["Height"] #Hauteur
    Width = Set._dict_["Width"] #Largeur
    fps = Set._dict_["fps"]

    pygame.init()

    Window = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Manic Shooter : Shot'em up !")



    Window.fill((153,77,0))#Donne une couleur de fond a la page.
    police = pygame.font.SysFont("monospace", 50)
    policeCopyright = pygame.font.SysFont("arial", 12)
    textTitre = police.render("Manic Shooter:", True, (255,255,255))


    textCopyright = policeCopyright.render("© Développé par Aubry Nicolas, Ragot David et Berthier Théo", True, (255,255,255))
    placementTexteTitre = (Width/2) - (textTitre.get_width()/2)

    btnJouer = btn.Button(150,60, (144,88,41), "JOUER", 450, Width, Window)#Ajoute un bouton jouer.
    btnJouer.draw()
    btnJouer.afficherTexte(btnJouer.txtPlacement_x,btnJouer.txtPlacement_y)


    btnSettings = btn.Button(240,60, (144,88,41), "SETTINGS", 700, Width, Window)#Ajoute un bouton settings.
    btnSettings.draw()
    btnSettings.afficherTexte(btnSettings.txtPlacement_x,btnSettings.txtPlacement_y)


    btnQuitter = btn.Button(210,60, (144,88,41), "QUITTER", 950, Width, Window)#Ajoute un bouton quitter.
    btnQuitter.draw()
    btnQuitter.afficherTexte(btnQuitter.txtPlacement_x, btnQuitter.txtPlacement_y)



    Window.blit(textTitre, (placementTexteTitre, 30))
    Window.blit(textCopyright, (450,850))

    continuer = True
    while continuer:#Boucle principale du jeux.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    save()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 150/2) and x < (Width/2 + 150/2):
                    save()
                if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                    continuer = False
                if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 240/2) and x < (Width/2 + 240/2):
                    print("ok")
        pygame.display.update()#Update la page.
        pygame.time.Clock().tick(fps)
    pygame.quit()
    quit()
def save():#fonction qui affichera le menu de selection des sauvegardes après avoir cliqué sur jouer
    Set = Settings.Settings()
    Set.read()
    pygame.font.init()

    Height = Set._dict_["Height"] #Hauteur
    Width = Set._dict_["Width"] #Largeur
    fps = Set._dict_["fps"]

    pygame.init()

    Window = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Manic Shooter : Shot'em up !")

    Window.fill((153,77,0))#Donne une couleur de fond a la page.
    police = pygame.font.SysFont("monospace", 50)
    policeCopyright = pygame.font.SysFont("arial", 12)
    textTitre = police.render("CHOIX DE LA SAUVEGARDE", True, (255,255,255))


    textCopyright = policeCopyright.render("© Développé par Aubry Nicolas, Ragot David et Berthier Théo", True, (255,255,255))
    placementTexteTitre = (Width/2) - (textTitre.get_width()/2)

    btnJouer = btn.Button(360,60, (144,88,41), "SAUVEGARDE 1", 450, Width, Window)#Ajoute un bouton pour la Sauvegrade une 
    btnJouer.draw()
    btnJouer.afficherTexte(btnJouer.txtPlacement_x,btnJouer.txtPlacement_y)


    btnSettings = btn.Button(360,60, (144,88,41), "SAUVEGARDE 2", 700, Width, Window)#Ajoute un bouton pour la deuxième sauvegarde
    btnSettings.draw()
    btnSettings.afficherTexte(btnSettings.txtPlacement_x,btnSettings.txtPlacement_y)


    btnQuitter = btn.Button(360,60, (144,88,41), "SAUVEGARDE 3", 950, Width, Window)#Ajoute un bouton pour la troisième sauvegarde
    btnQuitter.draw()
    btnQuitter.afficherTexte(btnQuitter.txtPlacement_x, btnQuitter.txtPlacement_y)

    btnQuitter = btn.Button(210,60, (144,88,41), "QUITTER", 1200, Width, Window)#Ajoute un bouton quitter.
    btnQuitter.draw()
    btnQuitter.afficherTexte(btnQuitter.txtPlacement_x, btnQuitter.txtPlacement_y)

    Window.blit(textTitre, (placementTexteTitre, 30))
    Window.blit(textCopyright, (450,850))

    continuer = True
    while continuer:#Boucle principale du Menu save.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Jeux(Height, Width)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                    Set.save_settings(Set._dict_)
                    difficulté()
                if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                    Set.save_settings(Set._dict_)
                    difficulté()
                    
                if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 360/2) and x < (Width/2 + 360/2):
                    Set.save_settings(Set._dict_)
                    difficulté()
                     
                if y > 1200/2 and y < 1200/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                    menu()
        pygame.display.update()#Update la page.
        pygame.time.Clock().tick(fps)

def difficulté():
    Set = Settings.Settings()
    Set.read()
    pygame.font.init()

    Height = Set._dict_["Height"] #Hauteur
    Width = Set._dict_["Width"] #Largeur
    fps = Set._dict_["fps"]

    pygame.init()

    Window = pygame.display.set_mode((Width,Height))


    pygame.display.set_caption("Manic Shooter : Shot'em up !")

    Window.fill((153,77,0))#Donne une couleur de fond a la page.
    police = pygame.font.SysFont("monospace", 50)
    policeCopyright = pygame.font.SysFont("arial", 12)
    textTitre = police.render("CHOIX DE LA DIFFICULTER", True, (255,255,255))


    textCopyright = policeCopyright.render("© Développé par Aubry Nicolas, Ragot David et Berthier Théo", True, (255,255,255))
    placementTexteTitre = (Width/2) - (textTitre.get_width()/2)

    btnJouer = btn.Button(180,60, (144,88,41), "FACILE", 450, Width, Window)#Ajoute un bouton pour la difficulté facile
    btnJouer.draw()
    btnJouer.afficherTexte(btnJouer.txtPlacement_x,btnJouer.txtPlacement_y)


    btnSettings = btn.Button(180,60, (144,88,41), "NORMAL", 700, Width, Window)#Ajoute un bouton pour la difficulté normal
    btnSettings.draw()
    btnSettings.afficherTexte(btnSettings.txtPlacement_x,btnSettings.txtPlacement_y)


    btnQuitter = btn.Button(270,60, (144,88,41), "DIFFICILE", 950, Width, Window)#Ajoute un bouton pour la difficulté difficile
    btnQuitter.draw()
    btnQuitter.afficherTexte(btnQuitter.txtPlacement_x, btnQuitter.txtPlacement_y)

    btnQuitter = btn.Button(210,60, (144,88,41), "QUITTER", 1200, Width, Window)#Ajoute un bouton quitter.
    btnQuitter.draw()
    btnQuitter.afficherTexte(btnQuitter.txtPlacement_x, btnQuitter.txtPlacement_y)

    Window.blit(textTitre, (placementTexteTitre, 30))
    Window.blit(textCopyright, (450,850))
    continuer = True
    while continuer:#Boucle principale du Menu save.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Jeux(Height, Width)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 180/2) and x < (Width/2 + 180/2):
                    Jeux(Height, Width,1)
                if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 270/2) and x < (Width/2 + 270/2):
                    Jeux(Height, Width,3)
                if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 180/2) and x < (Width/2 + 180/2):
                    Jeux(Height,Width,2)
                if y > 1200/2 and y < 1200/2 + 60 and x > (Width/2 - 210/2) and x < (Width/2 + 210/2):
                    save()
        pygame.display.update()#Update la page.
        pygame.time.Clock().tick(fps)

def Jeux(Hht, Wth, d):

    diff = d
    pygame.init()

    Set = Settings.Settings()
    Set.read()

    def load_json_to_dict(path):
        with open(path) as file:  # On récupère le fichier
            _dict_ = json.load(file)
        return _dict_ 

    ### Charge un dictionnaire de données sur les differentes "Balles" ###
    # File_path = ['Entity/Bullet/Bullet_type.json', 'Patern.json'] 
    _dict_Bullet_type = load_json_to_dict("JSON_File/Bullet_type.json")
    _dict_Bullet_type = Blt.loader_fct_bullet(_dict_Bullet_type)#Permet de creer les fonctions une seules fois, en les remplacant a leur endroit respectif dans le dictionnaire.
    
    _dict_Patern = load_json_to_dict("JSON_File/Patern.json")
    _dict_Patern = Wvs.loader_patern(_dict_Patern)

    _dict_Spaceship = load_json_to_dict("JSON_File/SpaceShip.json")
    _dict_Ennemy = load_json_to_dict("JSON_File/Ennemy.json")
    _dict_Powers_ups = load_json_to_dict("JSON_File/Power_ups.json")

    Height, Width = Hht, Wth
    if Set.file_here:
        Height = Set._dict_["Height"]  # Hauteur
        Width = Set._dict_["Width"]  # Largeur
    fps = Set._dict_["fps"]

    Window = pygame.display.set_mode((Width, Height), pygame.SRCALPHA)
    Clock = pygame.time.Clock()
    FontFPS = pygame.font.Font(None, 30)
    pygame.display.set_caption("Manic Shooter : Shot'em up !")
    
    #Background = pygame.image.load(os.path.join("..", "Ressources", "Background","Background.jpg")).convert()
    #Background = pygame.transform.scale(Background, (Width,Height))#Charge l'image
    Background = scroll.Background(0, Width, Height)


    #__GroupSHIP = ENTGroup.Entity()
    #__GroupBullet_enn = ENTGroup.Entity()

    Wave_ = Wvs.Waves(_dict_Patern, _dict_Ennemy, _dict_Bullet_type, fps)#On initialise notre objet de Vague
    #print(Wave_.patern)

    #Groupe d'entité ALLIE
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

    BLACK = (0, 0, 0)
    continuer = True
    Temps_ecoule = 0
    while continuer:
        #Window.blit(Background, (0,0))
        
        #Window.fill(BLACK)
        delta_time = Clock.tick(fps) * 0.001 #En ms -> x0.001 pour mettre en seconde et delta time : c'est le temps entre 2 images.
        FPS = Clock.get_fps()

        Temps_ecoule += delta_time

        pressed = pygame.key.get_pressed()
        buttons = {pygame.key.name(k) for k,v in enumerate(pressed) if v}#Recupère le nom des touches PRESSE

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
                    for i in range(_dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["n"]):
                        Bullet = Blt.bullet(Spaceship, _dict_Bullet_type, i)
                        __GroupBullet_Ally.add(Bullet)
                    Spaceship.bullet_last_hit = now


        if 'escape' in buttons:
            menu()

        if 'f' in buttons and 'i' in buttons and 'n' in buttons:
            pygame.quit()
            quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
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
            Shop.update(Spaceship,_dict_Spaceship, _dict_Bullet_type, _dict_Powers_ups,x,y)
            Shop.draw(Window)#Order draw = 5 bis
            x,y = (0,0)
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
                GameOver.draw(Window)
                if GameOver.menu:
                    menu()
                if GameOver.rejouer:
                    Jeux(Height,Width,d)
                if GameOver.quitter:
                    pygame.quit()
                    quit()

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

