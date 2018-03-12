import time
import os
import pygame
from pygame.locals import * 
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.abc import x, y, s, a, t, w, h, c, v

import Entity.EntityGroup as ENTGroup
import Entity.Ennemy as Enn

def loader_patern(_dict_Patern):

    for i in _dict_Patern["typ_bullet"]: 
        for j in _dict_Patern["typ_bullet"][i]["position"]:
        
            Fct1 = lambdify((x, y, w, h, c, v), sp.sympify(_dict_Patern["typ_bullet"][i]["position"][j]["x"]), modules=["math"])
            Fct2 = lambdify((x, y, w, h, c, v), sp.sympify(_dict_Patern["typ_bullet"][i]["position"][j]["y"]), modules=["math"])

            _dict_Patern["typ_bullet"][i]["position"][j]["x"]= Fct1
            _dict_Patern["typ_bullet"][i]["position"][j]["y"]= Fct2
        
        for j in _dict_Patern["typ_bullet"][i]["fonction"]:
            
            Fct1 = lambdify((x, y, s, a, t), sp.sympify(_dict_Patern["typ_bullet"][i]["fonction"][j]["x"]), modules=["math"])
            Fct2 = lambdify((x, y, s, a, t), sp.sympify(_dict_Patern["typ_bullet"][i]["fonction"][j]["y"]), modules=["math"])

            _dict_Patern["typ_bullet"][i]["fonction"][j]["x"]= Fct1
            _dict_Patern["typ_bullet"][i]["fonction"][j]["y"]= Fct2

    return _dict_Patern

class Waves():
    def __init__(self):

        self.wave = 0
        self.__GroupBullet_Ennemy = ENTGroup.Entity()
        self.__GroupSHIP = ENTGroup.Entity()
        
        self.position = 0
        self.numbers_ennemy = 0
        self.last_ennemy_spawn = 0

    def init_ennemy(self):
        pass

    def patern_choose(self):
        pass

    def update(self):

        self.__GroupBullet_Ennemy.update()
        self.__GroupSHIP.update()

    def draw(self, window):
        __GroupBullet_Ennemy.draw(window)
        __GroupSHIP.draw(window)

    