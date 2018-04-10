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

        self.last_drop = 0
        self.CD = 6000
        self.tmp = None

        self.load_images(_dict)

    def load_images(self, _dict):
        for i in _dict["type"]:
            _dict["type"][i]["image"] = pygame.image.load(os.path.join("..","Ressources","Graphics","Power_ups", i +".png")).convert_alpha()

    def add_Bonus(self, typ, power, _dict):

        Sprite = Obj.Sprite_upgrade(_dict, typ, power)
        self.Group.add(Sprite)

    def random_add_sprite(self, wave, _dict):
        now = pygame.time.get_ticks()
        if now - self.last_drop >= self.CD:
            x = rd.random()
            if x <= 0.10:
                typ = rd.choice(list(_dict["List"].keys()))

                p = rd.randint(0,100)
                for i in _dict["List"][typ]["Chance"]:
                    j = 0
                    p -= i
                    if p <= 0:
                        tmp = j
                        break
                    j += 1     
                power = tmp
                if wave >= _dict["List"][typ]["Unlocked"][power]:
                    self.add_Bonus(typ,power+1, _dict) 
                    self.last_drop = now

    def update(self, wave, _dict_power_ups):
        self.random_add_sprite(wave, _dict_power_ups)
        self.Group.update()
    def draw(self, Window):
        self.Group.draw(Window)