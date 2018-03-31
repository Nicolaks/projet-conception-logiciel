import time
import os
import pygame
import math
import random as rd
import pygame
from pygame.locals import *
import Menu.button as btn


class shop():
    def __init__(self,dict_spaceship, dict_bullet, dict_power_ups):

        self.dict_spaceship = dict_spaceship
        self.dict_bullet = dict_bullet
        self.dict_power_ups = dict_power_ups

        self.done = False

    def statement(self,spaceship, dict):
        pass

    def update(self, spaceship, dict_spaceship, dict_bullet, dict_power_ups):
        pass

    def draw(self, window):
        pass