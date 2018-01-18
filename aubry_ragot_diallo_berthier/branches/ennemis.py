from grille import *
import math
class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0



    def ajoutEnnemis(self, maGrille): #Permet l'ajout du héro.

        ennemis = "0"

        for i in range(2):
            for j in range(maGrille.ligne):
                maGrille.grid[i][j] = ennemis

"""

        hauteurMap = maGrille.colonne - 1
        centre = math.ceil(maGrille.ligne/2) - 1 #placement du hero
        self.posX = hauteurMap
        self.posY = centre
        hero = "1"
        for i in range(len(maGrille.grid)):
            for j in range(maGrille.ligne):
                maGrille.grid[hauteurMap][centre] = hero # ajout du hero dans le centre de la liste

"""
