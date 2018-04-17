import time
import os
import random as rd
import pygame
import math

from pygame.locals import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, fps=60):

        super().__init__()
        Surface = pygame.display.get_surface()
        self.Surf_Height, self.Surf_Width = Surface.get_height(), Surface.get_width()

        self.full_life = None
        self.life = None

        self.width = int(self.Surf_Width/3)
        self.dict_boss = {}
        self.fps = fps

        self.lst_bullet = ["double_ennemy", "double_boss", "triple_boss"]
        self.bullet_type = rd.choice(self.lst_bullet)
        self.damage = 15
        self.last_shoot = 0
        self.shoot_prob = 35
        self.shoot_CD = 300

        self.load_ressources()

    def i_boss(self, WaveObj):

        self.boss = rd.choice(list(self.dict_boss.keys()))
        self.image = self.dict_boss[str(self.boss)][0]

        self.height = self.image.get_height()

        self.rect = self.image.get_rect()

        self.life = 500*WaveObj.wave
        self.full_life = self.life

        self.money = 2000 + int(500*math.log10((WaveObj.wave%WaveObj.difficulty)+1))
        self.score = 10000

        self.rect.x =  int((self.Surf_Width - self.width)/2)
        self.rect.y = 0

        self.posX, self.posY = self.rect.x, self.rect.y

        self.cmpt_image = 0
        self.len_list = len(self.dict_boss[str(self.boss)])
        self.last_img = pygame.time.get_ticks()

        self.time = 1.5

    def draw_(self, window):
        self.draw(window)

    def update_img(self):
        now = pygame.time.get_ticks()
        if now - self.last_img >= self.fps:
            if self.cmpt_image + 1 == self.len_list:
                self.cmpt_image = 0
            else:
                self.cmpt_image += 1
            self.image = self.dict_boss[str(self.boss)][self.cmpt_image]
            x,y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x,y
            self.last_img = now

    def update_pos(self):

        self.posX += 4*math.sin(self.time)
        self.posY += 0

        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)

    def update(self, time):
        self.bullet_type = rd.choice(self.lst_bullet)
        self.time += time

        if self.life <= 0:
            self.kill()

        self.update_img()
        self.update_pos()

    def load_ressources(self):
        n = len(os.listdir(os.path.join("..", "Ressources", "Graphics","Boss")))
        for boss in range(n):
            self.dict_boss[str(boss+1)] = []
            j = len(os.listdir(os.path.join("..", "Ressources", "Graphics","Boss",str(boss+1))))

            image = pygame.image.load(os.path.join("..", "Ressources", "Graphics", "Boss", str(boss+1),"frame-01.gif")).convert_alpha()
            coef = (image.get_height())/(image.get_width())

            for nb_frame in range(j-1):
                if nb_frame+1<10:
                    nb_frame = "0"+str(nb_frame+1)
                else:
                    nb_frame = str(nb_frame+1)
                img = pygame.image.load(os.path.join("..", "Ressources", "Graphics", "Boss", str(boss+1),"frame-"+nb_frame+".gif")).convert_alpha()#Charge l'image

                height = int(coef * self.width)
                img = pygame.transform.scale(img, (self.width,height))
                self.dict_boss[str(boss+1)].append(img)
