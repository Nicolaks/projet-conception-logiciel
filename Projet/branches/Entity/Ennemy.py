import time
import os
import pygame
import math
import random as rd
from pygame.locals import * 
import Entity.SpaceShip as _ss_
import Entity.Bullet as Blt

class EnnShip(_ss_.SpaceShip):
    def __init__(self, _dict_Specs, _dict_Bullet, wave,FCTposX, FCTposY, CalcposX, CalcposY, Pobj):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "Ennemy"
        angle = 40

        life, width, __speed__, dmg = _dict_Specs["life"], _dict_Specs["width"], _dict_Specs["speed"], _dict_Specs["dmg"]

        money = _dict_Specs["money"]        

        style = rd.choice(_dict_Specs["style"])
        bullet_type = rd.choice(_dict_Specs["type tir"])

        self.shoot_CD = _dict_Specs["CD"]
        self.last_shoot = pygame.time.get_ticks()

        self.shoot_prob = _dict_Specs["ratio_tir"] + 3/40*(math.log10(wave))
        if self.shoot_prob >= 0.8:
            self.shoot_prob = 0.8

        super().__init__(life, dmg ,Type, style, __speed__,bullet_type, angle, width, money)

        self.bullet_style = 1
        self.phase = 0
        self.position = Pobj
        self.time = 0

        self.score = _dict_Specs["score"] 
        
        self.init_pos(FCTposX, FCTposY)
        self.posX, self.posY = self.rect.x, self.rect.y 

        self.FCTnewposXX = CalcposX
        self.FCTnewposYY = CalcposY

        self.break_btw_phase = None
        self.breaked = None
        self.phase_done = False
        self.passiv = False #Si true ne pourra pas prendre de dégats

    def init_pos(self, FCTposX, FCTposY):
        
        self.rect.x = int(FCTposX(self.width, self.height, self.Surf_Width, self.Surf_Height))
        self.rect.y = int(FCTposY(self.width, self.height, self.Surf_Width, self.Surf_Height))
        #print("POS X = ",self.rect.x, "POS Y =",self.rect.y, "PHASE :", self.phase, "POSITION : ", self.position)
        
    def new_pos(self):

        self.posX = self.FCTnewposXX(self.posX, self.posY, self.width, self.height, self.angle, self.time, self.__speed__)
        self.posY = self.FCTnewposYY(self.posX, self.posY, self.width, self.height, self.angle, self.time, self.__speed__)

        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)

        #print("posX = ",self.rect.x, "posY = ", self.rect.y)

    def patern_executed(self):

        if self.posX <= (-2*self.width)  or self.posX >= (self.Surf_Width + 2*self.width):
            self.phase_done = True
            self.passiv = True
            self.breaked = pygame.time.get_ticks()
        if self.posY <= (-2*self.height) or self.posY >= (self.Surf_Height + 2*self.height):
            self.phase_done = True
            self.passiv = True
            self.breaked = pygame.time.get_ticks()


    def update(self, delta_time):
        self.time += delta_time

        if not self.phase_done:
            self.new_pos()
            #self.shoot()
            self.patern_executed()
        else:
            now = pygame.time.get_ticks()
            if now - self.breaked >= self.break_btw_phase:
                self.phase_done = False
                self.passiv = False

        if self.life <= 0:
            self.kill()
        
