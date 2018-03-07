import time
import os
import pygame
from pygame.locals import *

class bullet(pygame.sprite.Sprite):
    def __init__(self, style = 1):
        super().__init__()

        self.type = "Bullet_"
        self.style = str(style)
        self.image = pygame.image.load(os.path.join("..","Ressources","Graphics","Bullet",self.type + self.style + ".png")).convert_alpha()
        
        coef = (self.style.get_height())/(self.style.get_width())
        self.width = 5
        self.height = int(coef*self.width)

        self.image = pygame.transform.scale(self.style, (self.width,self.height))
        self.rect = self.image.get_rect()

        self.posX = self.rect.x = spaceShip.posX + spaceShip.width/2 - self.reactor_width/2
        self.posY = self.rect.y + spaceShip.height

        self.__speed___bullet = __speed___bullet #vitesse des balles, que l'on définira en Json les paramètres de base

    def hit(self, spaceShip_obj):
        pass
    def update(self):#A chaque frame change la position
        pass
    def Draw(self):
        pass
    
