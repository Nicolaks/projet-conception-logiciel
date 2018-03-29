import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *
import Upgrade.Sprite_Power_ups as Obj
import Entity.EntityGroup as ENT


class Power_ups():
    def __init__(self, _dict):
        self.Group = ENT.Entity()
        self.dict = _dict

        self.last_drop = 0
        self.CD = 10000
        self.tmp = None

        self.load_images()

    def load_images(self):
        for i in self.dict["type"]:
            self.dict["type"][i]["image"] = pygame.image.load(os.path.join("..","Ressources","Graphics","Power_ups", i +".png")).convert_alpha()

    def add_Bonus(self, typ, power):

        Sprite = Obj.Sprite_upgrade(self.dict, typ, power)
        self.Group.add(Sprite)

    def random_add_sprite(self, wave):
        now = pygame.time.get_ticks()
        if now - self.last_drop >= self.CD:
            x = rd.random()
            if x <= 0.10:
                typ = rd.choice(list(self.dict["List"].keys()))

                p = rd.randint(0,100)
                for i in self.dict["List"][typ]["Chance"]:
                    j = 0
                    p -= i
                    if p <= 0:
                        tmp = j
                        break
                    j += 1     
                power = tmp
                if wave >= self.dict["List"][typ]["Unlocked"][power]:
                    self.add_Bonus(typ,power+1) 
                    self.last_drop = now

    def update(self, wave):
        self.random_add_sprite(wave)
        self.Group.update()
    def draw(self, Window):
        self.Group.draw(Window)