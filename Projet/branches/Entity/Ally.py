import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_

class allyShip(_ss_.SpaceShip):
    def __init__(self, _dict_Spaceship,style=1, __speed__ = 5, bullet_type = "single"):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "SpaceShip"
        angle = 45

        self.style = style

        width, dmg, life = self.init_carac(_dict_Spaceship)

        super().__init__(life, dmg ,Type, self.style, __speed__, bullet_type, angle, width)

        self.bullet_style = 1
        self.money = 0
        
        self.rect.x = self.Surf_Width/2 - self.width/2
        self.rect.y = self.Surf_Height*(1-(5/80)) - self.height

    def init_carac(self, _dict_Spaceship):
        width = _dict_Spaceship[str(self.style)]["width"]
        dmg = _dict_Spaceship[str(self.style)]["dmg"]
        life = _dict_Spaceship[str(self.style)]["life"]
        return width, dmg, life

    def upgrade_style_performance(self,style,_dict_Spaceship):
        if style <= len(_dict_Spaceship):
            self.style = style
            self.width, self.damage, self.life = self.init_carac(_dict_Spaceship)
            self.upgrade_style()


    def up(self):#Permet de faire déplacer le héro vers la gauche.
        if self.rect.y != 0:
            if self.rect.y - self.__speed__ < 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.__speed__
            #self.Reactor.follow(self)
                       

    def down(self):#Permet de faire se déplacer le héro sur la droite.
        if self.rect.y != self.Surf_Height - self.height:
            if self.rect.y + self.__speed__ > self.Surf_Height - self.height:
                self.rect.y = self.Surf_Height - self.height
            else:
                self.rect.y += self.__speed__
            #self.Reactor.follow(self)


    def left(self):
        if self.rect.x != 0:
            if self.rect.x - self.__speed__ < 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.__speed__
            #self.Reactor.follow(self)

    def right(self):
        if self.rect.x != self.Surf_Width - self.width:
            if self.rect.x + self.__speed__ > self.Surf_Width - self.width:
                self.rect.x = self.Surf_Width - self.width
            else:
                self.rect.x += self.__speed__
            #self.Reactor.follow(self)

    def draw(self, window):
        window.blit(self.image, self.rect)
