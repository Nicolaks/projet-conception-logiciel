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

    import button as btn

    import Upgrade.Power_ups as PU

except ImportError as error:
    print(error.__class__.__name__ + " : " + error.msg)
    sys.exit(0)

    #https://stackoverflow.com/questions/10168447/how-to-make-buttons-in-python-pygame/10169083 pour les boutons.
    #https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect pour l'interaction entre les boutons.
    #https://stackoverflow.com/questions/47639826/pygame-button-single-click pour les boutons.
    #https://stackoverflow.com/questions/47758248/pygame-button-get-pressed peut aider.


#class Button:
    #def __init__(self, master):
        #self.master = master


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

    btnJouer = btn.Button(170,60, (144,88,41), "JOUER", 450, Width, Window)#Ajoute un bouton jouer.
    btnJouer.draw()
    btnJouer.afficherTexte()


    btnSettings = btn.Button(240,60, (144,88,41), "SETTINGS", 700, Width, Window)#Ajoute un bouton settings.
    btnSettings.draw()
    btnSettings.afficherTexte()


    btnQuitter = btn.Button(220,60, (144,88,41), "QUITTER", 950, Width, Window)#Ajoute un bouton quitter.
    btnQuitter.draw()
    btnQuitter.afficherTexte()



    Window.blit(textTitre, (placementTexteTitre, 30))
    Window.blit(textCopyright, (450,850))

    continuer = True
    while continuer:#Boucle principale du jeux.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Jeux(Height,Width)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if y> 450/2 and y < 450/2 + 60 and x > (Width/2 - 170/2) and x < (Width/2 + 170/2):
                    Jeux(Height,Width)
                if y > 950/2 and y < 950/2 + 60 and x > (Width/2 - 220/2) and x < (Width/2 + 220/2):
                    pygame.quit()
                if y > 700/2 and y < 700/2 + 60 and x > (Width/2 - 240/2) and x < (Width/2 + 240/2):
                    print("ok")
        pygame.display.update()#Update la page.
        pygame.time.Clock().tick(fps)


def Pause():
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False



def Jeux(Hht, Wth):
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

    Wave_ = Wvs.Waves(_dict_Patern, _dict_Ennemy, _dict_Bullet_type)#On initialise notre objet de Vague
    #print(Wave_.patern)

    #Groupe d'entité ALLIE
    __GroupBullet_Ally = ENTGroup.Entity()#A mettre en variables du vaisseau

    UIn = UI.ui()
    Power_UP = PU.Power_ups(_dict_Powers_ups)


    Spaceship = Ally.allyShip(_dict_Spaceship, UIn.width)
    Spaceship.Reactor_innit()
    Spaceship.bullet_type = "pierreM"#Ligne non nécéssaire



    BLACK = (0, 0, 0)
    continuer = True
    Temps_ecoule = 0
    while continuer:
        #Window.blit(Background, (0,0))
        Background.draw(Window)
        Background.update(Wave_.wave,Wave_.Pause)

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


        __GroupBullet_Ally.update(delta_time)
        Wave_.update(delta_time, __GroupBullet_Ally, Spaceship, Power_UP.Group)
        Power_UP.update(Wave_.wave)
        UIn.update(Wave_.score, Wave_.wave, Spaceship.money)

        Power_UP.draw(Window)
        Wave_.draw(Window)
        __GroupBullet_Ally.draw(Window)
        Spaceship.draw(Window)
        UIn.draw(Window, Spaceship)

        fps_render = FontFPS.render("FPS : {}".format(int(FPS)), True, (255, 255, 255))
        nb_sprites = len(Wave_.GroupSHIP.sprites())
        counter_render = FontFPS.render("NBs : {}".format(nb_sprites),
            True, (255, 255, 255))

        Time = FontFPS.render("Time : {0:.2f}".format(float(Temps_ecoule)), True, (255, 255, 255))

        Window.blit(fps_render, (100, 100))
        #Window.blit(counter_render, (100, 150))
        Window.blit(Time, (100, 200))

        pygame.display.update()
