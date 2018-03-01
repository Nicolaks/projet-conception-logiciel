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
    import Entity.Bullet.Bullet as Blt
except ImportError as error:
    print(error.__class__.__name__ + " : " + error.msg)
    sys.exit(0)



def Jeux():
    Height = 900 #Hauteur
    Width = 900 #Largeur
    fps = 60

    pygame.init()

    Window = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Manic Shooter : Shot'em up !")
    Background = pygame.image.load(os.path.join("..","Ressources","Background","Background.jpg")).convert()
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

    #dictEnnemis = waves(dictEnnemis)
    ###################################
     #Liste qui va contenir les instances des tirs.
     #Liste qui va contenir les instances des ennemis.
    ###################################
    
    
    ### Charge un dictionnaire de données sur les differentes "Balles" ###
    #lFile_path = ['Entity/Bullet/Bullet_type.json', 'Patern.json']
    #__dict_Bullet_type = Settings.load_json_to_dict(lFile_path[0])
    #__dict_Patern = Settings.load_json_to_dict(lFile_path[1])

    Set = Settings.Settings()

    __GroupBullet_Ennemy = ENTGroup.Entity()
    __GroupEnnemy = ENTGroup.Entity()
    __GroupBullet_Ally = ENTGroup.Entity()
    Spaceship = Ally.allyShip()
    Spaceship.Reactor_innit()

    continuer = True
    while continuer:
        pressed = pygame.key.get_pressed() # already familiar with that
        buttons = {pygame.key.name(k) for k,v in enumerate(pressed) if v}#Recupère le nom des touches PRESSE
        print(buttons)
        if Set._dict_["up"] in buttons:
            Spaceship.up()
        if Set._dict_["down"] in buttons:
            Spaceship.down()
        if Set._dict_["left"] in buttons:
            Spaceship.left()
        if Set._dict_["right"] in buttons:
            Spaceship.right()
        if Set._dict_["s_shoot"] in buttons:
            pass
        if 'escape' in buttons:
            Set.get_key()
            Set.change_settings("up")
            print(Set._dict_["up"])
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
        Window.blit(Background, (0,0))
        #Window.blit(Spaceship.Reactor.reactor_style, (Spaceship.Reactor.reactor_posX, Spaceship.Reactor.reactor_posY))#Affiche le reacteur du vaisseau
        Window.blit(Spaceship.image, (Spaceship.posX, Spaceship.posY))
        #__GroupEnnemy.__Draw()  Cette fonction devrais affiché normalement TOUT les énemies qui sont dans le groupe de SPRITE
        #Affiche le vaisseau
        ############################
        pygame.display.update()
        pygame.time.Clock().tick(fps)
    pygame.quit()
    quit()

