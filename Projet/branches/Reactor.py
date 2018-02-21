import time
import os
import pygame
from pygame.locals import *

class Reactor:
    def __init__(self, spaceShip, style = "spaceShip1.png", spaceShip_type = 1):
        self.spaceShip_type = spaceShip_type

        self.reactor_style = pygame.image.load(os.path.join("..","Ressources","Graphics","SpaceShip","Reactor_" + style)).convert_alpha()
        self.reactor_width, self.reactor_height = self.reactor_style.get_width(), self.reactor_style.get_height()
        
        self.reactor_coef = (self.reactor_height)/(self.reactor_width)
        self.reactor_width = int(6/23*spaceShip.width)
        self.reactor_height = int(self.reactor_coef*self.reactor_width)

        self.reactor_style = pygame.transform.scale(self.reactor_style, (self.reactor_width,self.reactor_height))

        self.reactor_posX = spaceShip.posX + spaceShip.width/2
        self.reactor_posY = spaceShip.poxY + spaceShip.height

    def follow(self, spaceShip):
        self.reactor_posX = spaceShip.posX + spaceShip.width/2
        self.reactor_posY = spaceShip.poxY + spaceShip.height

