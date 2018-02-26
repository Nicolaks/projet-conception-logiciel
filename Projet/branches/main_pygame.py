import os
import sys
import time
import pygame
from pygame.locals import *
import Entity.Reactor as Rct
import Entity.EntityGroup as ENTGroup
import Entity.SpaceShip as spaceShip
import Entity.Ally as Ally



def Jeux():
    def switch(value):
        if value == 0:
            return "Veuillez entrer des valeurs entières !"
        if value == "titre":
            return "Manic Shooter : Shot'em up !"
        return None


    Height = 900 #Hauteur
    Width = 900 #Largeur
    fps = 60

    pygame.init()

    Window = pygame.display.set_mode((Width,Height), RESIZABLE)
    pygame.display.set_caption(switch("titre"))
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
    def Game():
        __GroupBullet_Ennemy = ENTGroup.Entity()
        __GroupEnnemy = ENTGroup.Entity()
        __GroupBullet_Ally = ENTGroup.Entity()
        Spaceship = Ally.allyShip()
        Spaceship.Reactor_innit()
        continuer = True
        flags = [0,0,0,0,0]
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                    continuer = False
                if event.type == pygame.KEYDOWN:#Si TOUCHE ENFONCE
                    if event.key == pygame.K_ESCAPE:#Touche Echape
                        PAUSE()
                    if event.key == pygame.K_SPACE:#Touche Espace
                        flags[0] = 1
                    if event.key == pygame.K_UP:
                        flags[1] = 1
                    if event.key == pygame.K_DOWN:
                        flags[2] = 1
                    if event.key == pygame.K_LEFT:
                        flags[3] = 1
                    if event.key == pygame.K_RIGHT:
                        flags[4] = 1
                if event.type == pygame.KEYUP:#Si touche RELACHE
                    if event.key == pygame.K_SPACE:#Touche Espace
                        flags[0] = 0
                    if event.key == pygame.K_UP:
                        flags[1] = 0
                    if event.key == pygame.K_DOWN:
                        flags[2] = 0
                    if event.key == pygame.K_LEFT:
                        flags[3] = 0
                    if event.key == pygame.K_RIGHT:
                        flags[4] = 0
            #EN FONCTION DES TOUCHES UTILISE
            #if flags[0] == 1:
                #tir = mTire.tire(monhero,maGrille)
                #dictTire[len(dictTire)] = tir
            if flags[1] == 1:
                Spaceship.up()
            if flags[2] == 1:
                Spaceship.down()
            if flags[3] == 1:
                Spaceship.left()
            if flags[4] == 1:
                Spaceship.right()
            #if len(dictTire) >= 1:
                #mTire.col_tire(dictEnnemis,dictTire)

            #__followPos() A ajouter pour reactualisé les positions de nos objets
            ############################
            ############################
            #__Draw() A ajouter pour tout les BLITs
            ############################
            Window.blit(Background, (0,0))
            #Window.blit(Spaceship.Reactor.reactor_style, (Spaceship.Reactor.reactor_posX, Spaceship.Reactor.reactor_posY))#Affiche le reacteur du vaisseau
            Window.blit(Spaceship.image, (Spaceship.posX, Spaceship.posY))#Affiche le vaisseau
            ############################
            pygame.display.update()
            pygame.time.Clock().tick(fps)
    Game()
    pygame.quit()
    quit()

