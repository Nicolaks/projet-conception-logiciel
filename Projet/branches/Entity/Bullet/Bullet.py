import time
import os
import pygame
from pygame.locals import *

class bullet:
    def __init__(self, dictBullet):
        typ = "Bullet_"
        self.type = typ
        self.style = str(style)
        self.image = pygame.image.load(os.path.join("..","Ressources","Graphics","Reactor",self.type + style + ".png")).convert_alpha()
        
        coef = (self.style.get_height())/(self.style.get_width())
        self.width = int(1/2)
        self.height = int(coef*self.width)

        self.image = pygame.transform.scale(self.style, (self.width,self.height))
        self.image_rect = self.image.get_rect()

        self.posX = spaceShip.posX + spaceShip.width/2 - self.reactor_width/2
        self.posY = spaceShip.posY + spaceShip.height

        self.__speed___bullet = __speed___bullet #vitesse des balles, que l'on définira en Json les paramètres de base
        self.cooldown = None

    def hit(self, spaceShip_obj):
        pass
    def update(self):#A chaque frame change la position
        pass
    
