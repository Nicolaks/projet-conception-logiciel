import time
import os
import pygame
import random as rd
from pygame.locals import * 

class ui():
    def __init__(self):
        
        zero = pygame.image.load(os.path.join("..","Ressources","Graphics","UI","numeral0.png")).convert_alpha()
        self.width = zero.get_width()

        self.Surf_width = pygame.display.get_surface().get_width()
        self.Surf_height = pygame.display.get_surface().get_height()

        Surf_Coef = self.Surf_height/self.Surf_width

        rapport = 1.25/Surf_Coef

        self.width = int(self.width*rapport)
        zero = pygame.transform.scale(zero, (self.width,self.width))
  
        one = self.__init_image(1)
        two = self.__init_image(2)
        three = self.__init_image(3)
        four = self.__init_image(4)
        five = self.__init_image(5)
        six = self.__init_image(6)
        seven = self.__init_image(7)
        eight = self.__init_image(8)
        nine = self.__init_image(9)
        x = self.__init_image("X")

        self.list = [zero, one, two, three, four, five, six, seven, eight, nine, x]

        self.origine = int(2*(self.Surf_width/3))
        self.origine += int(1.5*(self.Surf_width-self.origine)/10)
        self.list_image = []

        self.radius = int(1.25*self.Surf_width/20)
        self.number_wave = []
        self.money = []

        self.ratio_rect = 2

        self.height_rect = (self.Surf_height/3)
        self.height_rect = int(self.height_rect - self.height_rect/10)
        self.width_rect = self.width
        self.height_back_rect = self.height_rect
        self.Origin_rect_x = 10
        self.Origin_rect_y = int((self.Surf_height - self.height_rect/10 - self.height_rect))

        self.last_change_color = 0
        self.last_change_color_i = 0

        self.shield_height = int(self.height_rect/2)
        self.shield_back_rect = self.shield_height
        self.shield_origin_x = int(self.Origin_rect_x + self.width_rect + 5*self.ratio_rect)
        self.shield_origin_y = int(self.Surf_height - self.shield_height - self.height_rect/10)

        self.invincible_origin_x = self.Surf_width - self.width_rect - self.Origin_rect_x
        self.invincible_origin_y = self.shield_origin_y

        self.WHITE = (255,255,255)
        self.YELLOW = (255,255,0)
        self.GREY = (112,128,144)
        self.RED = (255,0,0)
        self.RED_a = (156,0,0,0)
        self.GREEN = (0,139,0)

    def __init_image(self, char):
        im = pygame.image.load(os.path.join("..","Ressources","Graphics","UI","numeral"+ str(char) + ".png")).convert_alpha()
        im = pygame.transform.scale(im, (self.width,self.width))
        return im

    def draw(self, window, SpaceShip):
        self.draw_score(window)
        self.draw_wave(window)
        self.draw_life(window, SpaceShip) 
        self.draw_shield(window, SpaceShip)
        self.draw_money(window)
        self.draw_bonus_cd(window, SpaceShip)

    def draw_bonus_cd(self, window, SpaceShip):
        for Bonus in SpaceShip.Group_Bonus.sprites():
            if Bonus.type == "Invincible":#RAJOUTER ET FACTORISER AVEC SPEED
                posX = self.invincible_origin_x
            else:
                posX = self.invincible_origin_x -2* self.width_rect
            
            now = pygame.time.get_ticks()
            height = self.shield_back_rect - (self.shield_back_rect*(now - Bonus.time)/Bonus.cd)
            y_origin = self.invincible_origin_y + self.shield_back_rect - height
            
            x = (now - Bonus.time)/Bonus.cd
            x = 1 - x

            if x >= 0.66:
                color = self.GREEN
            elif x < 0.66 and x >= 0.33:
                color = self.YELLOW
            elif x < 0.33:
                color = self.RED

            pygame.draw.rect(window, color, [posX, y_origin,self.width_rect, height])
            if x <= 0.6 and x > 0.4:
                if now - self.last_change_color_i >= 600:
                    pygame.draw.rect(window, self.WHITE, [posX, y_origin,self.width_rect, height])
                    self.last_change_color_i = now
            if x <= 0.4 and x > 0.2:
                if now - self.last_change_color_i >= 400:
                    pygame.draw.rect(window, self.WHITE, [posX, y_origin,self.width_rect, height])
                    self.last_change_color_i = now
            if x <= 0.2:
                if now - self.last_change_color_i >= 200:
                    pygame.draw.rect(window, self.WHITE, [posX, y_origin,self.width_rect, height])
                    self.last_change_color_i = now


    def draw_money(self, window):
        pos = 0
        n = len(self.money)
        for i in range(9):
            if i < n:
                window.blit(self.list[self.money[i]],(int(1.5*self.width) + self.origine + pos,self.width + 15))
            else:
                window.blit(self.list[10], (int(1.5*self.width) + self.origine + pos,self.width + 15))
            pos += self.width
                   

    def draw_score(self,window):
        pos = 0
        n = len(self.list_image)
        for i in range(11):
            if i < n:
                window.blit(self.list[self.list_image[i]],(self.origine + pos,10))
            else:
                window.blit(self.list[10], (self.origine + pos,10))
            pos += self.width

    def draw_wave(self,window):
        posX = 10
        for i in self.number_wave:
            window.blit(self.list[i],(posX ,10))
            posX += self.width + 5

    def draw_life(self, window,SpaceShip):

        pygame.draw.rect(window, self.GREY, [self.Origin_rect_x, self.Origin_rect_y,self.width_rect, self.height_back_rect])
        pygame.draw.rect(window, self.WHITE, [self.Origin_rect_x+self.ratio_rect, self.Origin_rect_y+self.ratio_rect,self.width_rect-2*self.ratio_rect, self.height_back_rect-2*self.ratio_rect])
        
        self.height_rect = int(((self.height_back_rect-self.ratio_rect)/SpaceShip.full_life)*SpaceShip.life)
        if (SpaceShip.life/SpaceShip.full_life) <= 0.30:
            pygame.draw.rect(window, self.RED_a, [self.Origin_rect_x+self.ratio_rect, self.Origin_rect_y+self.height_back_rect+self.ratio_rect-self.height_rect,self.width_rect-2*self.ratio_rect, self.height_rect-2*self.ratio_rect])        
            now = pygame.time.get_ticks()
            if now - self.last_change_color >= 600:
                pygame.draw.rect(window, self.WHITE, [self.Origin_rect_x+self.ratio_rect, self.Origin_rect_y+self.height_back_rect+self.ratio_rect-self.height_rect,self.width_rect-2*self.ratio_rect, self.height_rect-2*self.ratio_rect])
                self.last_change_color = now
        else:
            pygame.draw.rect(window, self.RED, [self.Origin_rect_x+self.ratio_rect, self.Origin_rect_y+self.height_back_rect+self.ratio_rect-self.height_rect,self.width_rect-2*self.ratio_rect, self.height_rect-2*self.ratio_rect])        


    def draw_shield(self, window, SpaceShip):

        self.shield_height = int(((self.shield_back_rect-self.ratio_rect)/SpaceShip.shield_max)*SpaceShip.shield)
        pygame.draw.rect(window, self.WHITE,[self.shield_origin_x, self.shield_origin_y,self.width_rect, self.shield_back_rect])        
        
        if SpaceShip.shield > 0:
            pygame.draw.rect(window, self.GREY,[self.shield_origin_x+self.ratio_rect, self.shield_origin_y+self.ratio_rect+self.shield_back_rect-self.shield_height,self.width_rect-2*self.ratio_rect, self.shield_height-2*self.ratio_rect])


    def update(self, num, wave, money):
        self.list_image = list(map(int, str(num)))
        self.number_wave = list(map(int, str(wave)))
        self.money = list(map(int, str(money)))