import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *


class shop():
    def __init__(self, window, spaceship, dict_spaceship, dict_bullet, dict_power_ups, widthtxt=25):

        self.window_h, self.window_w = window.get_height(), window.get_width()

        self.dict_spaceship = dict_spaceship
        self.dict_bullet = dict_bullet
        self.dict_power_ups = dict_power_ups

        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.YELLOW = (255,255,0)
        self.GREY = (112,128,144)
        self.RED = (255,0,0)
        self.RED_a = (156,0,0,0)
        self.GREEN = (0,139,0)

        self.nb_button = 7
        self.police = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), widthtxt)
        self.police_am = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), 10)
        
        self.txtShop = self.police.render("SHOP", True, (255,255,255))

        self.lst_text = ["Amilioration de vaisseau :", "Amilioration de vies :", "Amilioration de dégats :", "Amilioration des balles :", "+ 15 shield :", "Shield MAX :", "Augmentation taux de drop Bonus :", "Continuer"]

        self.height_btw_btn = int(1.5*self.police_am.render(self.lst_text[0], True, self.WHITE).get_height())
        
        self.rect_shop = [self.window_w/2,0,self.window_w/2,self.window_h]

        self.posX_first_btn = int(self.window_w/2 + 3*(self.window_w/40)) # = self.window_w/2 + 1.5*(self.window_w/2)/10
        self.posY_first_btn = int(self.window_h/6)

        self.width_btn = int((self.window_w/2) - 6*(self.window_w/40))
        self.height_btn = int((self.window_h - 2*self.posY_first_btn -self.height_btw_btn*self.nb_button)/self.nb_button)  #70 = 7*10px soit l'écart total entre chaque bouton

        self.lst_btn = []

        self.max_width = None
        self.max_width_txt()
        self.decal_x = int(((self.window_w/2) - self.max_width)/2)


        self.Continue_w_txt = None
        self.Continue_h_txt = None
        self.Continue_decal_y = None

        self.create_button_upgrade(window)

        self.price_style = 2500

        self.act_life_upgrade = 0
        self.life_nb_upgrade = 5
        self.price_life_o = 300
        self.price_life = self.price_life_o#le "o" pour d'origine
        
        self.act_damage_upgrade = 0
        self.damage_nb_upgrade = 5
        self.price_damage_o = 300
        self.price_damage = self.price_damage_o
        
        self.shield_nb_upgrade = 5
        self.act_shield_upgrade = 0
        self.shield_bonus = 10
        self.price_shield = 300
        self.price_shield_o = self.price_shield

        self.shield_max_nb_upgrade = 5
        self.act_shield_max_upgrade = 0
        self.price_max_shield = 1200
        self.price_max_shield_o = self.price_max_shield
        
        self.price_Bullet = 3000
        
        self.drop_nb_upgrade = 6
        self.act_Drop_upgrade = 0
        self.price_Drop = 4000
        self.facteur_upgrade = 3

        self.statement(spaceship, dict_spaceship, dict_bullet, dict_power_ups)

        self.done = False

    def max_width_txt(self):
        
        width = self.police_am.render(self.lst_text[0], True, self.WHITE).get_width()
        for txt in self.lst_text:
            tmp = self.police_am.render(txt, True, self.WHITE).get_width()
            if tmp >= width:
                width = tmp

        self.max_width = width

    def create_button_upgrade(self, window):
        posY = self.posY_first_btn
        for i in range(self.nb_button):
            button = [self.WHITE,self.posX_first_btn, posY, self.width_btn, self.height_btn, self.police_am.render(self.lst_text[i], True, self.BLACK)]
            self.lst_btn.append(button)
            posY += self.height_btn + self.height_btw_btn

        txt = self.police.render(self.lst_text[len(self.lst_text)-1], True, self.WHITE)
        button = [self.GREEN,int(self.window_w/2),int(self.window_h-self.window_h/6), int(self.window_w/2),int(self.window_h-(self.window_h-self.window_h/6)), txt]

        self.Continue_w_txt = txt.get_width()
        self.Continue_h_txt = txt.get_height()
        self.Continue_decal_y = (button[4] - self.Continue_h_txt)/2 - self.Continue_h_txt/2
        self.lst_btn.append(button)

    def draw(self, window):
        pygame.draw.rect(window, self.GREY, self.rect_shop)
        window.blit(self.txtShop,((self.window_w/2) + 5,0))

        for i in range(len(self.lst_btn)-1):
            pygame.draw.rect(window, self.lst_btn[i][0], [self.lst_btn[i][1], self.lst_btn[i][2], self.lst_btn[i][3], self.lst_btn[i][4]])
            window.blit(self.lst_btn[i][5], (self.lst_btn[i][1] - self.decal_x, int(self.lst_btn[i][2] - 1.5*self.lst_btn[i][5].get_height())))
        
        i = len(self.lst_btn) -1
        
        w_txt = self.lst_btn[i][5].get_width()
        h_txt = self.lst_btn[i][5].get_height()
        decal_y = (self.lst_btn[i][4] - h_txt)/2 - h_txt/2

        pygame.draw.rect(window, self.lst_btn[i][0], [self.lst_btn[i][1], self.lst_btn[i][2], self.lst_btn[i][3], self.lst_btn[i][4]])
        window.blit(self.lst_btn[i][5], (int(self.lst_btn[i][1] + (self.window_w/2 - self.Continue_w_txt)/2), int(self.lst_btn[i][2] + self.Continue_decal_y)))

        self.draw_statement(window)

    def statement(self,spaceship, dict_spaceship, dict_bullet, dict_power_ups):
        #Status amilioration vaisseau
        self.style = spaceship.nb_style
        self.len_style = len(dict_spaceship)
        if self.style+1 <= self.len_style:
            self.next_style = self.style+1
        else:
            self.next_style = "No More !"

        self.life = spaceship.life
                
        self.damage = spaceship.damage

        self.shield = spaceship.shield

        bullet_type = spaceship.bullet_type

        self.len_pos_bullet = len(dict_bullet["Order_typ_bullet"])
        for i in range(self.len_pos_bullet):
            if bullet_type == dict_bullet["Order_typ_bullet"][i]:
                self.pos_bullet_type = i

        if self.pos_bullet_type +1 < self.len_pos_bullet:
            self.next_bullet_upgrade = dict_bullet["Order_typ_bullet"][self.pos_bullet_type+1]
        else:
            self.next_bullet_upgrade = "No More !"

        self.lst_bullet = dict_bullet["Order_typ_bullet"]

        self.drop = {}
        for i in dict_power_ups["List"]:
            self.drop[i] = dict_power_ups["List"][i]["Chance"]

    def draw_statement(self, window):
        specs_button = self.lst_btn[0]       
        w_upgrade = int(2*(specs_button[3] - 20)/3)

        #Statement Vaisseau:

        posX = specs_button[1] + 10 
        posX_o = posX
        
        posY = specs_button[2]

        w_button = w_upgrade
        h_button = specs_button[4]

        w_btw_stats = 5

        Rect_w = int(w_button/(self.len_style)) - w_btw_stats
        Rect_h = h_button - 10
        posY += (h_button - Rect_h)

        posY_o = posY

        Rect_h -= 10

        for i in range(self.len_style):
            if (i+1) <= self.style:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w

        if self.style == self.next_style:
            txt = self.police_am.render(self.next_style, True, self.BLACK)
        else:
            txt = self.police_am.render(str(self.price_style), True, self.BLACK)
        posY = int(posY_o + (Rect_h - txt.get_height())/2)
        posX += 5
        window.blit(txt, (int(posX), int(posY)))

        #Statement Life 
        specs_button = self.lst_btn[1]

        posY = specs_button[2] + (h_button - Rect_h - 10)
        posX = posX_o

        Rect_w = int(w_button/(self.life_nb_upgrade)) - w_btw_stats
        for i in range(self.life_nb_upgrade):
            if i+1 <= self.act_life_upgrade:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w

        txt = self.police_am.render(str(self.price_life), True, self.BLACK)
        window.blit(txt, (int(posX), int(posY)))

        #Statement Damage:
        specs_button = self.lst_btn[2]

        posY = specs_button[2] + (h_button - Rect_h - 10)
        posX = posX_o

        Rect_w = int(w_button/(self.damage_nb_upgrade)) - w_btw_stats
        for i in range(self.damage_nb_upgrade):
            if i+1 <= self.act_damage_upgrade:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w
        txt = self.police_am.render(str(self.price_damage), True, self.BLACK)
        window.blit(txt, (int(posX), int(posY)))


        #Statement Bullet upGrade:
        specs_button = self.lst_btn[3]
        
        txt = self.police_am.render(str(self.next_bullet_upgrade)+str(self.price_Bullet), True, self.BLACK)
        posX = int(specs_button[1] + ((specs_button[3] - txt.get_width())/2))
        posY = int(specs_button[2] + ((specs_button[4] - txt.get_height())/2) - txt.get_height()/2)
        window.blit(txt,(posX,posY))


        #Statement Shield +15:
        specs_button = self.lst_btn[4]

        posY = specs_button[2] + (h_button - Rect_h - 10)
        posX = posX_o

        Rect_w = int(w_button/(self.shield_nb_upgrade)) - w_btw_stats
        for i in range(self.shield_nb_upgrade):
            if i+1 <= self.act_shield_upgrade:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w
        
        txt = self.police_am.render(str(self.price_shield), True, self.BLACK)
        window.blit(txt, (int(posX), int(posY)))

        #Statement shiled max:
        specs_button = self.lst_btn[5]

        posY = specs_button[2] + (h_button - Rect_h - 10)
        posX = posX_o

        Rect_w = int(w_button/(self.shield_max_nb_upgrade)) - w_btw_stats
        for i in range(self.shield_max_nb_upgrade):
            if i+1 <= self.act_shield_max_upgrade:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w

        txt = self.police_am.render(str(self.price_max_shield), True, self.BLACK)
        window.blit(txt, (int(posX), int(posY)))


        #Statement upgrade drop:
        specs_button = self.lst_btn[6]

        posY = specs_button[2] + (h_button - Rect_h - 10)
        posX = posX_o

        Rect_w = int(w_button/(self.drop_nb_upgrade)) - w_btw_stats
        for i in range(self.drop_nb_upgrade):
            if i+1 <= self.act_Drop_upgrade:
                pygame.draw.rect(window, self.YELLOW, [posX, posY, Rect_w, Rect_h])
            else:
                pygame.draw.rect(window, self.BLACK, [posX, posY, Rect_w, Rect_h])
            posX += w_btw_stats + Rect_w
        
        txt = self.police_am.render(str(self.price_Drop), True, self.BLACK)
        window.blit(txt, (int(posX), int(posY)))
        
    def see_new_upgrade_before(self):
        pass

    def clic(self,spaceship, dict_spaceship, dict_bullet, dict_power_ups, mouse_x, mouse_y):
        Width = 1
        if mouse_x>= self.lst_btn[0][1] and mouse_x <= self.lst_btn[0][1] + self.lst_btn[0][3] and mouse_y >= self.lst_btn[0][2] and mouse_y <= self.lst_btn[0][2] + self.lst_btn[0][4]:
            if spaceship.money >= self.price_style and self.next_style != "No More !":
                spaceship.upgrade_style_performance(self.next_style,dict_spaceship)
                spaceship.money -= self.price_style

                self.price_style += 1000

                self.act_damage_upgrade = 0
                self.price_damage = self.price_damage_o = self.price_damage_o + 500

                self.act_life_upgrade = 0
                self.price_life = self.price_life_o = 300 + self.price_life_o

                self.price_max_shield = self.price_max_shield_o = self.price_max_shield_o + 500
                self.act_shield_max_upgrade = 0

                self.price_shield = self.price_shield_o = self.price_shield_o + 200
                self.act_shield_upgrade = 0
            else:
                pass
                #DRAW_flash money
        elif mouse_x>= self.lst_btn[1][1] and mouse_x <= self.lst_btn[1][1] + self.lst_btn[1][3] and mouse_y >= self.lst_btn[1][2] and mouse_y <= self.lst_btn[1][2] + self.lst_btn[1][4]:
            if spaceship.money >= self.price_life:
                if self.act_life_upgrade <= self.life_nb_upgrade:
                    if spaceship.life + 10 >= spaceship.full_life:
                        spaceship.life = spaceship.full_life
                    else:
                        spaceship.life += 10
                    spaceship.money -= self.price_life
                    self.price_life += 100
                    self.act_life_upgrade += 1
                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money
        elif mouse_x>= self.lst_btn[2][1] and mouse_x <= self.lst_btn[2][1] + self.lst_btn[2][3] and mouse_y >= self.lst_btn[2][2] and mouse_y <= self.lst_btn[2][2] + self.lst_btn[2][4]:
            if spaceship.money >= self.price_damage:
                if self.act_damage_upgrade <= self.damage_nb_upgrade:
                    self.act_damage_upgrade += 1
                    spaceship.money -= self.price_damage
                    spaceship.damage += 5#Paramètre arbidraire pour le moment
                    self.price_damage += 250
                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money

        elif mouse_x>= self.lst_btn[3][1] and mouse_x <= self.lst_btn[3][1] + self.lst_btn[3][3] and mouse_y >= self.lst_btn[3][2] and mouse_y <= self.lst_btn[3][2] + self.lst_btn[3][4]:
            if spaceship.money >= self.price_Bullet:
                if self.next_bullet_upgrade != "No More !":
                    spaceship.money -= self.price_Bullet
                    spaceship.bullet_type = self.next_bullet_upgrade
                    self.price_Bullet += 1000
                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money 
        elif mouse_x>= self.lst_btn[4][1] and mouse_x <= self.lst_btn[4][1] + self.lst_btn[4][3] and mouse_y >= self.lst_btn[4][2] and mouse_y <= self.lst_btn[4][2] + self.lst_btn[4][4]:
            if spaceship.money >= self.price_shield:
                if self.act_shield_upgrade <=  self.shield_nb_upgrade and spaceship.shield < 100:
                    spaceship.money -= self.price_shield
                    self.act_shield_upgrade += 1
                    if spaceship.shield + self.shield_bonus >= 100:
                        spaceship.shield = 100
                    else:
                        spaceship.shield += self.shield_bonus

                    self.price_shield += 250
                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money
        elif mouse_x>= self.lst_btn[5][1] and mouse_x <= self.lst_btn[5][1] + self.lst_btn[5][3] and mouse_y >= self.lst_btn[5][2] and mouse_y <= self.lst_btn[5][2] + self.lst_btn[5][4]:
            if spaceship.money >= self.price_max_shield:
                if self.act_shield_max_upgrade <=  self.shield_nb_upgrade and spaceship.shield < 100:
                    spaceship.money -= self.price_max_shield
                    spaceship.shield = 100
                    self.act_shield_max_upgrade += 1
                    self.price_max_shield += 1000
                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money
        
        elif mouse_x>= self.lst_btn[6][1] and mouse_x <= self.lst_btn[6][1] + self.lst_btn[6][3] and mouse_y >= self.lst_btn[6][2] and mouse_y <= self.lst_btn[6][2] + self.lst_btn[6][4]:
            if spaceship.money >= self.price_Drop:
                if self.act_Drop_upgrade <= self.drop_nb_upgrade:
                    spaceship.money -= self.price_Drop
                    self.price_Drop += 1000
                    self.act_Drop_upgrade += 1
                    
                    for Bonus_type in dict_power_ups["List"]:
                        len_chance = len(dict_power_ups["List"][Bonus_type]["Chance"])
                        for j in range(len_chance-1):
                            dict_power_ups["List"][Bonus_type]["Chance"][i] -= self.facteur_upgrade
                        dict_power_ups["List"][Bonus_type]["Chance"][len_chance-1] += self.facteur_upgrade*(len_chance-1)

                else:
                    pass
                    #Draw button flash
            else:
                pass
                #DRAW flash money
        elif mouse_x>= self.lst_btn[7][1] and mouse_x <= self.lst_btn[7][1] + self.lst_btn[7][3] and mouse_y >= self.lst_btn[7][2] and mouse_y <= self.lst_btn[7][2] + self.lst_btn[7][4]:
            self.done = True

    def update(self, spaceship, dict_spaceship, dict_bullet, dict_power_ups, mouse_x, mouse_y):
        self.statement(spaceship, dict_spaceship, dict_bullet, dict_power_ups)

        #Içi on vérifiera les zones de CLIC en hover ou pas
        
        
        