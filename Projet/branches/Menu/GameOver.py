import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *

class GameOver():
    def __init__(self, Height, Width, widthtxt = 25):

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


        self.police = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), widthtxt)
        self.police_am = pygame.font.Font(os.path.join("..","Ressources","Police","Megaten","Megaten 20XX.ttf"), int(widthtxt/2))

        self.window_h = Height
        self.window_w = Width

        self.height_btw_button = 20

        self.lst_txt = []
        self.lst_button = []

        txtOver = self.police.render("Game Over !", True, self.BLACK)
        txtMenu = self.police_am.render("Menu", True, self.BLACK)
        txtRejouer = self.police_am.render("Rejouer", True, self.BLACK)
        txtQuitter = self.police_am.render("Quitter", True, self.BLACK)

        self.height = int(txtOver.get_height()+ txtMenu.get_height() + txtRejouer.get_height() + txtQuitter.get_height())

        self.lst_txt.append(txtOver)
        self.lst_txt.append(txtMenu)
        self.lst_txt.append(txtRejouer)
        self.lst_txt.append(txtQuitter)
        #self.posX relative 

        self.posY = int((self.window_h)/2 - (self.height + (len(self.lst_txt)-1)*self.height_btw_button))

        self.width = txtOver.get_width() + self.height_btw_button
        self.rect_x = int((self.window_w - txtOver.get_width() - self.height_btw_button)/2)
        self.rect_y = self.posY - int(self.height_btw_button/2)

        self.posY = int((self.window_h)/2 - (self.height + (len(self.lst_txt)-1)*self.height_btw_button))
        self.height += (len(self.lst_txt)+1)*self.height_btw_button

    def clic(self,mouse_x,mouse_y):
        if mouse_x>= self.lst_button[1][0] and mouse_x <= self.lst_button[1][0] + self.lst_button[1][2] and mouse_y >= self.lst_button[1][1] and mouse_y <= self.lst_button[1][1] + self.lst_button[1][3]:
            self.menu = True
        elif mouse_x>= self.lst_button[2][0] and mouse_x <= self.lst_button[2][0] + self.lst_button[2][2] and mouse_y >= self.lst_button[2][1] and mouse_y <= self.lst_button[2][1] + self.lst_button[2][3]:
            self.rejouer = True
        elif mouse_x>= self.lst_button[3][0] and mouse_x <= self.lst_button[3][0] + self.lst_button[3][2] and mouse_y >= self.lst_button[3][1] and mouse_y <= self.lst_button[3][1] + self.lst_button[3][3]:
            self.quitter = True
        
    def draw(self, window):
        pygame.draw.rect(window, self.BLACK, [self.rect_x, self.rect_y, self.width, self.height])
        pygame.draw.rect(window, self.WHITE, [self.rect_x-2, self.rect_y-2, self.width-4, self.height-4])

        posY = self.posY
        for txt in self.lst_txt:
            posX = int(((self.window_w)/2) - (txt.get_width()/2))
            window.blit(txt, (int(posX), int(posY)))
            self.lst_button.append([posX,posY,txt.get_width(),txt.get_height()])
            posY += txt.get_height() + self.height_btw_button
