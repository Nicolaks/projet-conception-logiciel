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
        self.liste = []
        for i in range(13):
            img = pygame.image.load(os.path.join("..", "Ressources", "Background","Background"+str(i)+".jpg")).convert()
            img = pygame.transform.scale(img, (self.Width,self.Height))#Charge l'image
            self.liste.append(img)
        self.change(0)
        self.Pause = True

    def change(self,i):
        self.image = self.liste[i]

    def draw(self, Window):
        if not self.Pause:
            Window.blit(self.image,(0,0))
        else:
            Window.blit(self.image,(0,self.pos_y - self.Height))
            self.y += 1
            self.pos_y = self.y % self.Height
            if self.pos_y <= self.Height:
                Window.blit(self.image,(0,self.pos_y))
    def update(self,wave,condition):
        if condition:
            if wave %10==0:
                self.Pause = False
                self.change(12)
            else:
                self.Pause = True
                self.change(wave%12)
