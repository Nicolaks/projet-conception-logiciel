import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *

class Sprite_upgrade(pygame.sprite.Sprite):
    def __init__(self, _dict, typ, power):

        self.type = typ
        self.power = power
        
        super().__init__()

        typ = typ + "_" + str(power)

        if self.type == "Random":
            self.dict = _dict

        self.image = _dict["type"][typ]["image"]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.life = self.shield = self.speed = self.cd = 0
        self.invincible = False        

        self.stats(_dict,typ)

        Surface = pygame.display.get_surface()
        self.Surf_Height, self.Surf_Width = Surface.get_height(), Surface.get_width()
        self.rect.x = rd.randint(0,self.Surf_Width-self.image.get_width())
        self.rect.y = -2*self.image.get_height()

        if self.cd != 0:
            self.time = None
            self.previous_speed = None
        
        self.delable = False
        
    def stats(self,_dict,typ):

        if "life" in _dict["type"][typ]:
            self.life = _dict["type"][typ]["life"]
        if "shield" in _dict["type"][typ]:
            self.shield = _dict["type"][typ]["shield"]
        if "speed" in _dict["type"][typ]:
            self.speed = _dict["type"][typ]["speed"]
        if "Invincible" in _dict["type"][typ]:
            self.invincible = _dict["type"][typ]["Invincible"]
        if "cooldown" in _dict["type"][typ]:
            self.cd = _dict["type"][typ]["cooldown"]

    def update(self):
        self.rect.y += 3

        if self.rect.y >= (self.Surf_Height + self.image.get_height()):
            self.kill()
