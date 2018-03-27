import os
import sys
import time
import pygame
import json
from pygame.locals import *

class Background():
    def __init__(self,bckg_dict, Width,Height):
        self.dict = bckg_dict
        self.image = None
        self.Width, self.Height = Width,Height
        self.y = 0
        self.pos_y = 0

        self.change(str("Background"))
        self.Pause = False

    def change(self,name):
        self.image = pygame.image.load(os.path.join("..", "Ressources", "Background",name+".jpg")).convert()
        self.image = pygame.transform.scale(self.image, (self.Width,self.Height))#Charge l'image

    def draw(self, Window):
        if not self.Pause:
            Window.blit(self.image,(0,self.pos_y - self.Height))
            self.y += 1
            self.pos_y = self.y % self.Height
            if self.pos_y <= self.Height:
                Window.blit(self.image,(0,self.pos_y))
