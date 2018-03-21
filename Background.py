import time
import os
import pygame
from pygame.locals import * 

class Background():
    def __init__(self, _dict_):
        self._dict_ = _dict_
        self.posX = 0
        self.posY = 0
        self.image = None
        self.change("vague 1")

    def change(self, name)
        param_image = self._dict_[name]["image"]
        self.image = pygame.load.

        self.vitess = self._dict_[name]["vitesse"]
        self.list = 
    def draw(self, window):
        window.blit()
    def update(self, wave):
        if wave%5 == 0:
            self.change("vitess")
