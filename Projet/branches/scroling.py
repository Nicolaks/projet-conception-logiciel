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
            self.y -= 1
            self.pos_y = self.y % self.Height
            if self.pos_y <= self.Height:
                Window.blit(self.image,(0,self.pos_y))

















"""
pygame.init()
Width = 800
Height = 600
fps = 60
BLACK = (255,255,255)
Window = pygame.display.set_mode((Width, Height))
Background = pygame.image.load(os.path.join("..", "Ressources", "Background","Background.jpg")).convert()
Background = pygame.transform.scale(Background, (Width,Height))#Charge l'image
y = 0
Clock = pygame.time.Clock()
pygame.display.set_caption("Manic Shooter : Shot'em up !")
condition = True
while condition:
    delta_time = Clock.tick(fps) * 0.001
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
            condition = False
    Window.fill(BLACK)
    pos_y = y % Background.get_rect().height
    Window.blit(Background,(0,pos_y - Background.get_rect().height))#difference de pos
    y -= 1 #vitesse scroling
    if pos_y < Height:
        Window.blit(Background,(0,pos_y))

    pygame.display.update()


pygame.quit()
quit()
"""
