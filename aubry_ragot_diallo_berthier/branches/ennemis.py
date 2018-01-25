from grille import *
import math
import random
class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0



    def ajoutEnnemis(self, maGrille): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        #Que les ennemis ne puissent pas apparaitre sur des autres ennemis ou sur un tire en cours
        ennemis = "0"
        maGrille.grid[math.ceil(random.random()*2)-1][math.ceil(random.random()*maGrille.ligne)-1] = ennemis#Ajoute un ennemis de façon aléatoire dans le haut de la grille.


    def defile(self):

        return None

    def collision(self):

        return None
