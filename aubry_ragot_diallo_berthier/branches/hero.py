from grille import *
import math
class hero:

    def __init__(self):
        self.posX = 0
        self.posY = 0



    def ajoutHero(self, maGrille): #Permet l'ajout du héro.

        hauteurMap = maGrille.colonne - 1
        centre = math.ceil(maGrille.ligne/2) - 1 #placement du hero
        self.posX = hauteurMap
        self.posY = centre
        hero = "1"
        for i in range(len(maGrille.grid)):
            for j in range(maGrille.ligne):
                maGrille.grid[hauteurMap][centre] = hero # ajout du hero dans le centre de la liste
