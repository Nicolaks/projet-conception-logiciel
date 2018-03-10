try:
    import os
    import sys
    import time
    import pygame
    import json
    from pygame.locals import *

    import pre_settings.Settings as Settings
    import Entity.Reactor as Rct
    import Entity.EntityGroup as ENTGroup
    import Entity.SpaceShip as spaceShip
    import Entity.Ally as Ally
    import Entity.Bullet as Blt
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
    #Window.fill((255,255,255))
    police = pygame.font.SysFont("monospace", 50)
    policeCopyright = pygame.font.SysFont("arial", 12)
    textTitre = police.render("Manic Shooter:", True, (255,255,255))
    textJouer = police.render("JOUER", True, (255,255,255))
    textSettings = police.render("SETTINGS", True, (255,255,255))
    textQuitter = police.render("QUITTER", True, (255,255,255))

    textCopyright = policeCopyright.render("© Développé par Aubry Nicolas, Ragot David et Berthier Théo", True, (255,255,255))


    placementTexteTitre = (Width/2) - (textTitre.get_width()/2)
    placementTexteJouer = (Width/2) - (textJouer.get_width()/2)
    placementTexteSettings = (Width/2) - (textSettings.get_width()/2)
    placementTexteQuitter = (Width/2) - (textQuitter.get_width()/2)

    rectJouer = pygame.draw.rect(Window, (144,88,41) ,(placementTexteJouer,340,160,70))
    rectSettings = pygame.draw.rect(Window, (144,88,41), (placementTexteSettings, 460, 250, 70))
    rectQuitter = pygame.draw.rect(Window, (144,88,41), (placementTexteQuitter, 580, 220, 70))

    Window.blit(textTitre, (placementTexteTitre, 30))
    Window.blit(textJouer, (placementTexteJouer,350))
    Window.blit(textSettings, (placementTexteSettings,470))
    Window.blit(textQuitter, (placementTexteQuitter,590))
    Window.blit(textCopyright, (540,950))


    continuer = True
    while continuer:#Boucle principale du jeux.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Jeux(Height,Width)

        pygame.display.update()#Update la page.
        pygame.time.Clock().tick(fps)




def Jeux(Hht, Wth):
    Set = Settings.Settings()
    Set.read()

    Height, Width = Hht, Wth
    if Set.file_here:
        Height = Set._dict_["Height"]  # Hauteur
        Width = Set._dict_["Width"]  # Largeur
    fps = Set._dict_["fps"]

    pygame.init()
    # print("DRIVER :",pygame.display.get_driver())
    # input()
    Window = pygame.display.set_mode((Width, Height))
    Clock = pygame.time.Clock()
    FontFPS = pygame.font.Font(None, 30)
    pygame.display.set_caption("Manic Shooter : Shot'em up !")
    Background = pygame.image.load(os.path.join("..", "Ressources", "Background","Background.jpg")).convert()
    Background = pygame.transform.scale(Background, (Width,Height))#Charge l'image

    ###################################
    #def waves(dictEnnemis, nb=5):#Valeur 5 ennemies de bases, on peut la changer en donnant nb=nombre en arguments
    #    for i in range(nb):
    #        print("i=",i)
    #        ennemi = mEnnemis.ennemis()
    #        ennemi.ajoutEnnemis(dictEnnemis, maGrille)
    #        dictEnnemis[i] = ennemi
    #    return dictEnnemis
    ###################################
    # Initialisation de la première vague d'énnemie

    def load_json_to_dict(path):
        with open(path) as file:  # On récupère le fichier
            _dict_ = json.load(file)
        return _dict_

    _dict_Bullet_type = load_json_to_dict("JSON_File/Bullet_type.json")
    _dict_Patern = load_json_to_dict("JSON_File/Patern.json")

    ### Charge un dictionnaire de données sur les differentes "Balles" ###
    # File_path = ['Entity/Bullet/Bullet_type.json', 'Patern.json']

    __GroupBullet_Ennemy = ENTGroup.Entity()
    __GroupSHIP = ENTGroup.Entity()
    __GroupBullet_Ally = ENTGroup.Entity()
    __AllyG = ENTGroup.Entity()

    Spaceship = Ally.allyShip()
    Spaceship.Reactor_innit()
    Spaceship.bullet_type = "quad"
    __AllyG.add(Spaceship)

    BLACK = (0, 0, 0)
    continuer = True
    while continuer:
        Window.blit(Background, (0,0))
        #Window.fill(BLACK)
        delta_time = Clock.tick(fps) * 0.001 #En ms -> x0.001 pour mettre en seconde
        FPS = Clock.get_fps()

        pressed = pygame.key.get_pressed()
        buttons = {pygame.key.name(k) for k,v in enumerate(pressed) if v}#Recupère le nom des touches PRESSE
        #print(buttons)
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
            pass
            #Set.get_key()
            #Set.change_settings("up")
            #Set.save_settings(Set._dict_)
            #print(Set._dict_["up"])
        if 'f' in buttons and 'i' in buttons and 'n' in buttons:
            continuer = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
        #__followPos() A ajouter pour reactualisé les positions de nos objets
        ############################
        ############################
        #__Draw() A ajouter pour tout les BLITs
        ############################
        # 
        #Window.blit(Spaceship.Reactor.reactor_style, (Spaceship.Reactor.reactor_posX, Spaceship.Reactor.reactor_posY))#Affiche le reacteur du vaisseau
        
        __AllyG.draw(Window)
        #print(__GroupBullet_Ally)
        __GroupBullet_Ally.update(_dict_Bullet_type, delta_time)
        __GroupBullet_Ally.draw(Window)
        #__GroupEnnemy.__Draw()  Cette fonction devrais affiché normalement TOUT les énemies qui sont dans le groupe de SPRITE
        #Affiche le vaisseau
        ############################

        fps_render = FontFPS.render("FPS : {}".format(int(FPS)), True, (255, 255, 255))
        nb_sprites = len(__GroupBullet_Ally.sprites())
        counter_render = FontFPS.render("NBs : {}".format(nb_sprites),
            True, (255, 255, 255))
        Window.blit(fps_render, (100, 100))
        Window.blit(counter_render, (100, 150))

        pygame.display.update()
    pygame.quit()
    quit()

