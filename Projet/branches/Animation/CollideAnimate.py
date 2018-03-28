import time
import os
import random as rd
import pygame
from pygame.locals import *

class impact(pygame.sprite.Sprite):
    def __init__(self,posX,posY, Bullet_Width):
        super().__init__()

        type_images = ["Blue_","Red_","Green_"]
        self.type = rd.choice(type_images)

        self.width = None
        self.height = None
        self.rect = None
        self.CD = 60
        self.list_images = []

        self.load_images()
        self.cmpt_image = 0
        self.image = self.list_images[self.cmpt_image]
        
        self.rect.x = posX + int(Bullet_Width/2)
        self.rect.y = posY

        self.posX, self.posY = self.rect.x, self.rect.y

        self.last_change = pygame.time.get_ticks()

        
    def load_images(self):

        self.list_images.append(pygame.image.load(os.path.join("..","Ressources","Graphics",
                                                            "Collision","Bullet_Ennemy",
                                                             self.type + str(1) + ".png")).convert_alpha())
        coef = (self.list_images[0].get_height())/(self.list_images[0].get_width())

        self.width = 20
        self.height = int(coef*self.width)
        self.rect = self.list_images[0].get_rect()
        self.list_images[0] = pygame.transform.scale(self.list_images[0], (self.width,self.height))

        for i in range(3):
            self.list_images.append(pygame.image.load(os.path.join("..","Ressources","Graphics",
                                                            "Collision","Bullet_Ennemy",
                                                             self.type + str(i+2) + ".png")).convert_alpha())
            self.list_images[i+1] = pygame.transform.scale(self.list_images[i+1], (self.width,self.height))
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_change >= self.CD:
            if self.cmpt_image < len(self.list_images):
                self.cmpt_image += 1
                self.image = self.list_images[self.cmpt_image]
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = self.posX, self.posY
                self.last_change = now
            if self.cmpt_image+1 == len(self.list_images):
                self.kill()

#class exploded(pygame.sprite.Sprite):
#    def __init__(self):
#        super().__init__()
