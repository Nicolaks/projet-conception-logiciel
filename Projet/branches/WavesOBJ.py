import time
import os
import pygame
import random as rd
from pygame.locals import * 
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.abc import x, y, s, a, t, w, h, c, v

import Entity.EntityGroup as ENTGroup
import Entity.Ennemy as Enn
import Entity.Bullet as Blt
import Entity.Boss as BOSS

import Animation.CollideAnimate as ColAnimate

def loader_patern(_dict_Patern):
    #x = self.rect.x position actuelle de l'objet en x
    #y = self.rect.y position actuelle en y
    #w = self.width largeur de notre objet en pixels #de la balle
    #h = self.height hauteur de notre obj
    #a = self.angle l'angle de rotation de l'image
    #s = self.__speed__ pour la vitesse des ennemis
    #c = largeur de l'objet parent Spaceship
    #v = de même avec la hauteur
    #t = temps
    for i in _dict_Patern["patern"]: 
        for j in _dict_Patern["patern"][i]["position"]:
            for k in _dict_Patern["patern"][i]["position"][j]:

                Fct1 = lambdify((w, h, c, v), sp.sympify(_dict_Patern["patern"][i]["position"][j][k]["x"]), modules=["math"])
                Fct2 = lambdify((w, h, c, v), sp.sympify(_dict_Patern["patern"][i]["position"][j][k]["y"]), modules=["math"])

                _dict_Patern["patern"][i]["position"][j][k]["x"] = Fct1
                _dict_Patern["patern"][i]["position"][j][k]["y"] = Fct2
    
        for j in _dict_Patern["patern"][i]["fonction"]:
            for k in _dict_Patern["patern"][i]["fonction"][j]:

                Fct1 = lambdify((x, y, w, h, a, t, s), sp.sympify(_dict_Patern["patern"][i]["fonction"][j][k]["x"]), modules=["math"])
                Fct2 = lambdify((x, y, w, h, a, t, s), sp.sympify(_dict_Patern["patern"][i]["fonction"][j][k]["y"]), modules=["math"])

                _dict_Patern["patern"][i]["fonction"][j][k]["x"] = Fct1
                _dict_Patern["patern"][i]["fonction"][j][k]["y"] = Fct2
        
    for i in _dict_Patern["ennemy_wave"]["fonction"]:
        Fct = lambdify((v), sp.sympify(_dict_Patern["ennemy_wave"]["fonction"][i]), modules=["math"])
        _dict_Patern["ennemy_wave"]["fonction"][i]= Fct
    return(_dict_Patern)

class Waves():
    def __init__(self, _dict_Patern, _dict_Ennemy, _dict_Bullet, fps):
        self._dict_ = _dict_Patern

        self._proba_l = {}
        self.items = []
        self.patern = None
        self.patern_duration = None

        self.wave = 1#On commence par la première wave
        self.wave_i = 0#Incrementeur pour changer la fonction du nombre d'ennemies par waves
        self.wave_FCT = self._dict_["ennemy_wave"]["fonction"][str(self.wave_i)]
        self.wave_change = None

        self.phase = 0

        self.end_patern = False
        self.Pause = False

        self.first_press_key = False
        self.start = 0
        self.begin = None

        self.Boss = BOSS.Boss()
        self.BOSS_init = False
        self.difficulty = 5#Facile par défault 15 Facile -> 2 pour TEST

        self.GroupBullet_Ennemy = ENTGroup.Entity()
        self.GroupSHIP = ENTGroup.Entity()
        self.GroupCollide_Bullet = ENTGroup.Entity()
        self.Group_Explode = ENTGroup.Entity()
        
        self.numbers_ennemy = 0
        self.Cooldown_ennemy = 0
        self.last_ennemy_spawn = 0

        self._dict_Ennemy = _dict_Ennemy
        self._dict_Bullet = _dict_Bullet

        self.score = 0
        
        self.patern_choose()
        self.numbers_ennemy_init()

    def innit_prob(self):

        j = 0
        self.items = []
        self._proba_l = {}
        for i in self._dict_["patern"]:
            p = self._dict_["patern"][i]["Appears"]["Chance"]
            if p != 0:
                self.items.append(i)
                self._proba_l[str(j)]=p
                j+=1

    def proba_up_low(self):
        self._dict_["patern"][self.patern]["Appears"]["Chance"] += self._dict_["patern"][self.patern]["Appears"]["lower"]

        for i in self._dict_["patern"]:
            if i != self.patern:
                self._dict_["patern"][i]["Appears"]["Chance"] += self._dict_["patern"][i]["Appears"]["upgrade"]

    def patern_choose(self):
        self.innit_prob()
        
        somme = 0
        for i in self._proba_l:#On fait la somme de toute les probabilité
            somme += self._proba_l[str(i)]
            #print("puis içi")
        x = rd.uniform(0,somme)
        print(x, self._proba_l, self.items)
        for i in range(len(self._proba_l)):#On calcule retiens le patern qui va annuler le x choisi entre 0 et la somme
            x -= self._proba_l[str(i)]
            if x<=0:
                tmp = i
                break
                #print("et enfin la")
        
        self.patern = self.items[tmp]#Le patern choisi aura sa probabilité réduite, les autres auront leur probabilité augmenté
        
        #self.patern = ""
        
        self.proba_up_low()


        self.patern_duration = len(self._dict_["patern"][self.patern]["position"])
        self.patern_PO = self._dict_["patern"][self.patern]["Appears"]["PO"]

        print(self.patern, self.patern_duration)
        

    def init_one_ennemy(self, pos):

        FCTposX = self._dict_["patern"][self.patern]["position"][str(self.phase)][str(pos)]["x"]
        FCTposY = self._dict_["patern"][self.patern]["position"][str(self.phase)][str(pos)]["y"]


        CalcposX = self._dict_["patern"][self.patern]["fonction"][str(self.phase)][str(pos)]["x"]
        CalcposY = self._dict_["patern"][self.patern]["fonction"][str(self.phase)][str(pos)]["y"]

        Type, i = self.choose_ennemy_type()
        self.change_chance_ennemy(i)

        Ennemy = Enn.EnnShip(self._dict_Ennemy["Ennemies"][Type], self._dict_Bullet, self.wave,FCTposX,FCTposY,CalcposX,CalcposY,pos)
        self.GroupSHIP.add(Ennemy)

        self.numbers_ennemy -= 1
        #print("Ennemy restant =",self.numbers_ennemy)

    def change_chance_ennemy(self, j):
        for i in range(len(self._dict_Ennemy["Chance"])):
            if i == j:
                self._dict_Ennemy["Chance"][i] += self._dict_Ennemy["LOW"][i]
            if i != j:
                self._dict_Ennemy["Chance"][i] += self._dict_Ennemy["UP"][i]


    def choose_ennemy_type(self):
        somme = 0
        for i in self._dict_Ennemy["Chance"]:
            somme += i
        
        p = rd.uniform(0,somme)
        for i,j in zip(self._dict_Ennemy["Chance"], range(len(self._dict_Ennemy["Chance"]))):#On calcule retiens le patern qui va annuler le x choisi entre 0 et la somme
            p -= i
            if p<=0:
                if self._dict_Ennemy["Chance"][j] == i:
                    return self._dict_Ennemy["Type"][j], j       

    def wave_change_init(self):
       
        if len(self._dict_["ennemy_wave"]["fonction"]) >= 1:
            self.wave_change = self._dict_["ennemy_wave"]["Wave change"][self.wave_i]
            #print("if", self.wave_change)

    def numbers_ennemy_init(self):
        
        if self.wave_change != None:
            self.wave_change_init()

        #print(self._dict_["ennemy_wave"]["fonction"])
        if self.wave == self.wave_change and self.wave_change != None:
            if len(self._dict_["ennemy_wave"]["fonction"]) > len(self._dict_["ennemy_wave"]["Wave change"]):
                self.wave_i += 1
                self.wave_FCT = self._dict_["ennemy_wave"]["fonction"][str(self.wave_change)]
        
        self.numbers_ennemy = int(self.wave_FCT(self.wave))
        if self.numbers_ennemy%self.patern_PO != 0:
            while self.numbers_ennemy%self.patern_PO != 0:
                self.numbers_ennemy -= 1
            if self.numbers_ennemy <=0:
                self.numbers_ennemy = int(self.wave_FCT(self.wave))                
                while self.numbers_ennemy%self.patern_PO != 0:
                    self.numbers_ennemy += 1
                    
    def ennemy_init(self):

        for i in range(int(self._dict_["patern"][self.patern]["Appears"]["PO"])):
            #print(i)
            self.init_one_ennemy(i)
        self.last_ennemy_spawn = pygame.time.get_ticks()

    def phase_statement(self):

        for Sprite_obj in self.GroupSHIP.sprites():
            if Sprite_obj.phase_done:
                Sprite_obj.break_btw_phase = self._dict_["patern"][str(self.patern)]["times_break"][str(Sprite_obj.position)][Sprite_obj.phase]
                if Sprite_obj.phase <= self.patern_duration-1:
                    if Sprite_obj.phase < self.patern_duration-1:
                        Sprite_obj.phase += 1
                    if Sprite_obj.phase == self.patern_duration-1:
                        Sprite_obj.phase = 0
                    Sprite_obj.time = 0
                    self.position_phase_actualisation(Sprite_obj)
                    self.FCT_phase_actualisation(Sprite_obj)

    def position_phase_actualisation(self, sprite):

        FCTposX = self._dict_["patern"][str(self.patern)]["position"][str(sprite.phase)][str(sprite.position)]["x"]
        FCTposY = self._dict_["patern"][str(self.patern)]["position"][str(sprite.phase)][str(sprite.position)]["y"]
        sprite.init_pos(FCTposX, FCTposY)
        sprite.posX, sprite.posY = sprite.rect.x, sprite.rect.y

        #print("PRE PHASE POS : ",sprite.posX," + ",sprite.posY)

    def FCT_phase_actualisation(self, sprite):

        FCTnewPosX = self._dict_["patern"][self.patern]["fonction"][str(sprite.phase)][str(sprite.position)]["x"]
        FCTnewPosY = self._dict_["patern"][self.patern]["fonction"][str(sprite.phase)][str(sprite.position)]["y"]

        sprite.FCTnewposXX = FCTnewPosX
        sprite.FCTnewposYY = FCTnewPosY

        #print("NEXT PHASE : ",sprite.posX," + ",sprite.posY)

    def startGame(self):

        if self.first_press_key:
            self.begin = pygame.time.get_ticks()
            self.first_press_key = None

                 
    def collide_bulletA_Ennemy(self, GroupBulletAlly, SpaceShip):

        colision = pygame.sprite.groupcollide(GroupBulletAlly, self.GroupSHIP, True, False, pygame.sprite.collide_mask)
        for bullet in colision:
            ImpactAnimation = ColAnimate.impact(bullet.rect.x,bullet.rect.y,bullet.width)
            self.GroupCollide_Bullet.add(ImpactAnimation)
            for ennemy in colision[bullet]:
                ennemy.life -= bullet.dmg
                if ennemy.life <= 0:
                    Explode = ColAnimate.impact(ennemy.rect.x,ennemy.rect.y,ennemy.width,statement=2)
                    self.Group_Explode.add(Explode)
                    self.score += ennemy.score
                    SpaceShip.money += ennemy.money

    def collide_bulletE_SpaceShip(self, SpaceShip):
        colision = pygame.sprite.spritecollide(SpaceShip, self.GroupBullet_Ennemy, True, pygame.sprite.collide_mask)
        for bullet in colision:
            ImpactAnimation = ColAnimate.impact(bullet.rect.x,bullet.rect.y,bullet.width)
            self.GroupCollide_Bullet.add(ImpactAnimation)
            SpaceShip.hit(bullet.dmg)

    def collide_bonus_SpaceShip(self, SpaceShip, BonusGroup):
        colision = pygame.sprite.spritecollide(SpaceShip, BonusGroup, True, pygame.sprite.collide_mask)
        for Bonus in colision:
            if Bonus.type == "Random":
                print(Bonus.dict["type"], Bonus.type, Bonus.power)
                NewType = rd.choice(Bonus.dict["type"][Bonus.type+"_"+str(Bonus.power)]["type"])
                Bonus.stats(Bonus.dict,str(NewType))
            SpaceShip.add_Bonus(Bonus)

    def collide_Spaceship_Ennemy(self, SpaceShip):
        colision = pygame.sprite.spritecollide(SpaceShip, self.GroupSHIP, True, pygame.sprite.collide_mask)
        for Ennemie in colision:
            Explode = ColAnimate.impact(Ennemie.rect.x,Ennemie.rect.y,Ennemie.width,statement=2)
            self.Group_Explode.add(Explode)
            SpaceShip.hit(2*Ennemie.damage)


    def draw(self, window):
          
        self.GroupBullet_Ennemy.draw(window)
        self.GroupSHIP.draw(window)

    def ennemy_bullet(self):
        
        for ennemy in self.GroupSHIP.sprites():
            now = pygame.time.get_ticks()
            p = rd.randint(0,100)
            #print(now - ennemy.last_shoot, ennemy.shoot_CD)
            if p <= ennemy.shoot_prob and now - ennemy.last_shoot >= ennemy.shoot_CD:
                for i in range(self._dict_Bullet["typ_bullet"][ennemy.bullet_type]["n"]):
                    Bullet = Blt.bullet(ennemy, self._dict_Bullet, i)
                    self.GroupBullet_Ennemy.add(Bullet)
                ennemy.last_shoot = now

    def update(self, Delta_time, GroupBulletAlly, SpaceShip, BonusGroup, Shop):  
        #print(self.numbers_ennemy, len(self.GroupSHIP.sprites()))       
        if self.begin != None:
            now = pygame.time.get_ticks()
            if self.Pause and self.end_patern:
                if now - self.begin >= 500:
                    GroupBulletAlly.empty()
                    BonusGroup.empty()
                    self.GroupBullet_Ennemy.empty()
                    self.start = 0
                    self.patern_choose()
                    self.numbers_ennemy_init()
                    self.Pause = False
                    self.end_patern = False


            self.GroupCollide_Bullet.update()
            self.Group_Explode.update()
            print(self.numbers_ennemy)

            if not self.Pause and not self.end_patern and (now - self.begin) >= self.start:
                self.Cooldown_ennemy = self._dict_["patern"][self.patern]["Appears"]["Cooldown"]

                if self.wave > 0 and self.wave%self.difficulty == 0 and not self.BOSS_init:
                    self.Boss.i_boss(self)
                    self.GroupSHIP.add(self.Boss)
                    self.BOSS_init = True
                elif now - self.last_ennemy_spawn >= self.Cooldown_ennemy and self.numbers_ennemy >=  self.patern_PO and not self.BOSS_init:
                    self.ennemy_init()
                
                if not self.BOSS_init:
                    self.phase_statement()
                    self.collide_Spaceship_Ennemy(SpaceShip)

                elif self.Boss.life <=0:
                    self.BOSS_init = False
                    self.wave+=1
                    self.Pause = True
                    self.end_patern = True
                    self.begin = now
                
                print(self._dict_Ennemy["Chance"])

                self.ennemy_bullet()


                self.collide_bulletA_Ennemy(GroupBulletAlly, SpaceShip)
                self.collide_bulletE_SpaceShip(SpaceShip)
                self.collide_bonus_SpaceShip(SpaceShip, BonusGroup)

                SpaceShip.update_bonus()
                self.GroupBullet_Ennemy.update(Delta_time)
                self.GroupSHIP.update(Delta_time)
                

                if SpaceShip.life <= 0:
                    Explode = ColAnimate.impact(SpaceShip.rect.x,SpaceShip.rect.y,SpaceShip.width,statement=2)
                    self.Group_Explode.add(Explode)

                if len(self.GroupSHIP.sprites())==0 and self.numbers_ennemy <= 0:
                    self.wave += 1
                    Shop.CD += 250
                    self.Pause = True
                    self.end_patern = True
                    self.begin = now

                    #print("WAVE END -> PAUSE -> NEXT WAVE")