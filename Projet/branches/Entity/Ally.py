import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_
import Entity.EntityGroup as ENT

class allyShip(_ss_.SpaceShip):
    def __init__(self, _dict_Spaceship,width_score,style=1, __speed__ = 5, bullet_type = "single"):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "SpaceShip"
        angle = 45

        self.nb_style = style

        width, dmg, life, shield, __speed__ = self.init_carac(_dict_Spaceship)

        super().__init__(life, dmg ,Type, self.nb_style, __speed__, bullet_type, angle, width, 0)

         
        self.shield = shield
        
        self.reset_pos()

        self.spaceship_speed = self.__speed__
        self.invincible = False
        self.speed_bonus = 0

        self.Group_Bonus = ENT.Entity()

        self.money = 400000

    def reset_pos(self):
        self.rect.x = self.Surf_Width/2 - self.width/2
        self.rect.y = self.Surf_Height*(1-(5/80)) - self.height


    def init_carac(self, _dict_Spaceship):
        width = _dict_Spaceship[str(self.nb_style)]["width"]
        dmg = _dict_Spaceship[str(self.nb_style)]["dmg"]
        life = _dict_Spaceship[str(self.nb_style)]["life"]
        shield = _dict_Spaceship[str(self.nb_style)]["shield"]
        speed = _dict_Spaceship[str(self.nb_style)]["speed"]
        return width, dmg, life, shield, speed

    def upgrade_style_performance(self,style,_dict_Spaceship):
        if style <= len(_dict_Spaceship):
            self.nb_style = style
            self.style = self.type + "_" + str(self.nb_style)
            self.width, self.damage, self.life, self.shield, self.spaceship_speed = self.init_carac(_dict_Spaceship)
            #print(self.spaceship_speed)
            self.full_life = self.life
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

    def hit(self, dmg):
        if not self.invincible:
            if self.shield > 0:
                self.shield -= dmg
                if self.shield < 0:
                    self.shield = 0
            else:
                self.life -= dmg
    
    def update_bonus(self):
        self.__speed__ = self.spaceship_speed + self.speed_bonus
        if len(self.Group_Bonus.sprites()) > 0:
            for Bonus in self.Group_Bonus.sprites():
                now = pygame.time.get_ticks()
                if now - Bonus.time >= Bonus.cd:
                    if self.invincible:
                        self.invincible = False
                    else:
                        self.speed_bonus = 0
                    Bonus.kill()
        

    def add_Bonus(self, BonusObj):

        if (self.life + BonusObj.life) >= self.full_life:
            self.life = self.full_life
        else:
            self.life += BonusObj.life

        if (self.shield + BonusObj.shield) >= self.shield_max:
            self.shield = self.shield_max
        else:
            self.shield += BonusObj.shield

        if BonusObj.cd != 0:
            BonusObj.time = pygame.time.get_ticks()
            if len(self.Group_Bonus.sprites()) > 0:
                for Obj in self.Group_Bonus.sprites():
                    if Obj.type == BonusObj.type:
                        if Obj.type == "Invincible":
                            Obj.cd += BonusObj.cd
                            BonusObj.delable = True
                        else:
                            if Obj.power < BonusObj.power:
                                Obj.power = BonusObj.power
                                Obj.cd += BonusObj.cd
                                self.speed_bonus = BonusObj.speed
                            else:
                                BonusObj.delable = True
            if BonusObj.invincible:
                self.invincible = True
            if BonusObj.type == "Speed":
                self.speed_bonus = BonusObj.speed
            self.Group_Bonus.add(BonusObj)
            if BonusObj.delable:
                BonusObj.kill()



