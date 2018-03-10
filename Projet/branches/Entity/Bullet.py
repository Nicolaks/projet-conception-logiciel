import time
import os
import pygame
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.abc import x, y, w, h, s, a, d

from pygame.locals import *

class bullet(pygame.sprite.Sprite):
    def __init__(self, spaceShip, __dict_bullet, i):
        super().__init__()

        self.type = "Bullet_"
        self.style = str(spaceShip.bullet_style)
        self.image = pygame.image.load(os.path.join("..","Ressources","Graphics","Bullet",self.type + self.style + ".png")).convert_alpha()

        coef = (self.image.get_height())/(self.image.get_width())
        self.width = 5
        self.height = int(coef*self.width)

        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()

        self.position = i
        self.bullet_type = spaceShip.bullet_type

        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["position"][str(i)]

        self.angle = dict_file["angle"]
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.init_pos(dict_file, spaceShip)

        # TRAJECTOIRE
        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["fonction"][str(self.position)]

        self.FCTnewposXX = lambdify((x, y, w, h, s, a, d), sp.sympify(dict_file["x"]), modules=["math"])
        self.FCTnewposYY = lambdify((x, y, w, h, s, a, d), sp.sympify(dict_file["y"]), modules=["math"])
        
        self.speed___bullet = __dict_bullet["typ_bullet"][spaceShip.bullet_type]["speed"] #vitesse des balles, que l'on définira en Json les paramètres de base
        self.time = 0

    def init_pos(self, dict_file, spaceShip):
        FCTposX = sp.sympify(dict_file["x"])
        FCTposY = sp.sympify(dict_file["y"])
        x, y, w, h, sw, sh, s, a = sp.symbols("x, y, w, h, sw, sw, s, a")
        self.rect.x = FCTposX.subs({x:spaceShip.rect.x, y:spaceShip.rect.y, sw:spaceShip.width, sh:spaceShip.height, w:self.width, h:self.height})
        self.rect.y = FCTposY.subs({x:spaceShip.rect.x, y:spaceShip.rect.y, sw:spaceShip.width, sh:spaceShip.height,w:self.width, h:self.height})

    def update(self, __dict_bullet, delta_time):  # A chaque frame change la position
        self.time += delta_time
        self.update_pos(__dict_bullet)
        self.auto_kill()

    def update_pos(self, __dict_bullet):

        self.rect.x = self.FCTnewposXX(self.rect.x, self.rect.y, self.width,
                                       self.height, self.speed___bullet,
                                       self.angle, self.time)

        self.rect.y = self.FCTnewposYY(self.rect.x, self.rect.y, self.width,
                                       self.height, self.speed___bullet,
                                       self.angle, self.time)

    def auto_kill(self):

        Surface = pygame.display.get_surface()
        Height, Width = Surface.get_height(), Surface.get_width()

        if self.rect.x >= Width + self.width or self.rect.x <= 0 - self.width:
            self.kill()
        if self.rect.y <= 0 - self.height or self.rect.y >= Height + self.height:
            self.kill()