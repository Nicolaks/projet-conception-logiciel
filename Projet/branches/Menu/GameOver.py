import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *

class GameOver():
    def __init__(self, Height, Width, coef = 1):

        self.WHITE = (238, 239, 255)
        self.BLACK = (0,0,0)
        self.YELLOW = (255,255,0)
        self.GREY = (112,128,144)
        self.RED = (255,0,0)
        self.RED_a = (156,0,0,0)
        self.GREEN = (0,139,0)

        self.menu = False
        self.rejouer = False
        self.quitter = False

        widthtxt = 40*coef

        self.police = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), widthtxt)
        self.police_am = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), int(widthtxt/2))

        self.window_h = Height
        self.window_w = Width

        self.height_btw_button = 20

        self.lst_txt = []
        self.lst_button = []

        txtOver = "Game Over !"
        txtMenu = "Menu"
        txtRejouer = "Rejouer"
        txtQuitter = "Quitter"

        txtOver_p = self.police.render(txtOver,True,self.BLACK)
        txtMenu_p = self.police_am.render(txtMenu,True,self.BLACK)
        txtRejouer_p = self.police_am.render(txtRejouer,True,self.BLACK)
        txtQuitter_p = self.police_am.render(txtQuitter,True,self.BLACK)

        self.height = int(txtOver_p.get_height()+ txtMenu_p.get_height() + txtRejouer_p.get_height() + txtQuitter_p.get_height())

        self.lst_txt.append([txtOver,False])
        self.lst_txt.append([txtMenu,False])
        self.lst_txt.append([txtRejouer,False])
        self.lst_txt.append([txtQuitter,False])
        #self.posX relative 

        self.posY = int((self.window_h)/2 - (self.height + (len(self.lst_txt)-1)*self.height_btw_button))

        self.width = txtOver_p.get_width() + self.height_btw_button
        self.rect_x = int((self.window_w - txtOver_p.get_width() - self.height_btw_button)/2)
        self.rect_y = self.posY - int(self.height_btw_button/2)

        self.posY = int((self.window_h)/2 - (self.height + (len(self.lst_txt)-1)*self.height_btw_button))
        self.height += (len(self.lst_txt)+1)*self.height_btw_button

        posY = self.posY
        posX = int(((self.window_w)/2) - (txtOver_p.get_width()/2))
        self.lst_button.append([posX,posY,txtOver_p.get_width(),txtOver_p.get_height()])
        posY += self.height_btw_button
        for i in range(1,len(self.lst_txt)):
            txt = self.police_am.render(self.lst_txt[i][0],True,self.BLACK)
            posY += txt.get_height() + self.height_btw_button
            posX = int(((self.window_w)/2) - (txt.get_width()/2))
            self.lst_button.append([posX,posY,txt.get_width(),txt.get_height()])
            

    def clic(self,mouse_x,mouse_y):
        if mouse_x>= self.lst_button[1][0] and mouse_x <= self.lst_button[1][0] + self.lst_button[1][2] and mouse_y >= self.lst_button[1][1] and mouse_y <= self.lst_button[1][1] + self.lst_button[1][3]:
            self.menu = True
        elif mouse_x>= self.lst_button[2][0] and mouse_x <= self.lst_button[2][0] + self.lst_button[2][2] and mouse_y >= self.lst_button[2][1] and mouse_y <= self.lst_button[2][1] + self.lst_button[2][3]:
            self.rejouer = True
        elif mouse_x>= self.lst_button[3][0] and mouse_x <= self.lst_button[3][0] + self.lst_button[3][2] and mouse_y >= self.lst_button[3][1] and mouse_y <= self.lst_button[3][1] + self.lst_button[3][3]:
            self.quitter = True
        
    def update(self,mouse_x,mouse_y):
        if mouse_x>= self.lst_button[1][0] and mouse_x <= self.lst_button[1][0] + self.lst_button[1][2] and mouse_y >= self.lst_button[1][1] and mouse_y <= self.lst_button[1][1] + self.lst_button[1][3]:
            self.lst_txt[1][1] = True
        else:
            self.lst_txt[1][1] = False
        if mouse_x>= self.lst_button[2][0] and mouse_x <= self.lst_button[2][0] + self.lst_button[2][2] and mouse_y >= self.lst_button[2][1] and mouse_y <= self.lst_button[2][1] + self.lst_button[2][3]:
            self.lst_txt[2][1] = True
        else:
            self.lst_txt[2][1] = False
        if mouse_x>= self.lst_button[3][0] and mouse_x <= self.lst_button[3][0] + self.lst_button[3][2] and mouse_y >= self.lst_button[3][1] and mouse_y <= self.lst_button[3][1] + self.lst_button[3][3]:
            self.lst_txt[3][1] = True
        else:
            self.lst_txt[3][1] = False


    def draw(self, window):
        pygame.draw.rect(window, self.BLACK, [self.rect_x, self.rect_y, self.width, self.height])
        pygame.draw.rect(window, self.WHITE, [self.rect_x-2, self.rect_y-2, self.width-4, self.height-4])

        txt = self.police.render(self.lst_txt[0][0],True,self.BLACK)
        window.blit(txt, (int(self.lst_button[0][0]), int(self.lst_button[0][1])))

        for i in range(1,len(self.lst_txt)):
            if self.lst_txt[i][1]:
                txt = self.police_am.render(self.lst_txt[i][0],True,self.GREEN)
            else:
                txt = self.police_am.render(self.lst_txt[i][0],True,self.BLACK)
            window.blit(txt, (int(self.lst_button[i][0]), int(self.lst_button[i][1])))


