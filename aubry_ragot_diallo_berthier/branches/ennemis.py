from grille import *
import math
class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0



    def ajoutEnnemis(self, maGrille): #Permet l'ajout du héro.

        ennemis = "0"

        #Permet de mettre les ennemis sur les deux premières lignes de la grille.
        for i in range(2):
            for j in range(maGrille.ligne):
                maGrille.grid[i][j] = ennemis
