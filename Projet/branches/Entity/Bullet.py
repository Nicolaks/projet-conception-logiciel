import time
import os
import pygame
from pygame.locals import *

class bullet:
    def __init__(self, style = "Bullet_", __vect_v = 5, bullet_type = 1):

        self.style = pygame.image.load(os.path.join("..","Ressources","Graphics","Reactor",style + bullet_type + ".png")).convert_alpha()
        self.width, self.height = self.style.get_width(), self.style.get_height()
        
        coef = (self.height)/(self.width)
        self.width = int(6/12)
        self.height = int(coef*self.width)

        self.style = pygame.transform.scale(self.style, (self.width,self.height))
        self.posX = spaceShip.posX + spaceShip.width/2 - self.reactor_width/2
        self.posY = spaceShip.posY + spaceShip.height
