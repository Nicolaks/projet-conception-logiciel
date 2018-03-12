import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_

class EnnShip(_ss_.SpaceShip):
    def __init__(self,style=1, __speed__ = 5, life=100, dmg=1, bullet_type="single_ennemy"):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "Ennemy_"
        super().__init__(life, dmg ,Type, style, __speed__, bullet_type)
        self.bullet_style = 41
            
    def update(self):
        pass
    
    def shoot(self):
        pass