import time
import os
import pygame
from pygame.locals import * 
import Entity.Reactor as Rct

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, typ, style, __speed__):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        pygame.sprite.Sprite.__init__(self)

        Surface = pygame.display.get_surface()#Recupere la surface de la fenetre
        self.Surf_Width, self.Surf_Height = Surface.get_width(), Surface.get_height()#Recupere sa longeur et largeur
        self.area = Surface.get_rect()

        ####################################
        self.type = typ
        ### CHARGEMENT DU STYLE VAISSEAU ###
        self.style = self.type + "_" + str(style)
        #fullpath = os.path.join("..", "Ressources", "Graphics", self.type, style)
        self.image = pygame.image.load(os.path.join("..", "Ressources", "Graphics", self.type, self.style + ".png")).convert_alpha()#Charge l'image
        self.width, self.height = self.image.get_width(), self.image.get_height()#Défini la Résolution affiché de notre objet

        self.coef = (self.height)/(self.width)#Calcul le coef de proportion de l'objet
        self.width = 50#On les tailles de la résolution de l'image
        self.height = int(self.coef * self.width)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))#Puis on appliques les nouvelles proportion

        self.image_rect = self.image.get_rect()
        ####################################

        self.__speed__ = __speed__

        self.posX = self.Surf_Width/2 - self.width/2
        self.posY = self.Surf_Height*(1-(5/80)) - self.height

        self.Reactor = None

    def Reactor_innit(self):
        if self.Reactor == None:
            pass
            #self.Reactor = Rct.reactor_f(self)

