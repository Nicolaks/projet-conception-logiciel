from grille import *
import math
import random
class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0



    def ajoutEnnemis(self, maGrille): #Permet l'ajout du héro.

        ennemis = "0"


        #Faire en sorte que a chaque instance, un ennemis apparaissent de manière aléatoire entre les deux premières lignes.
        #Permet de mettre les ennemis sur les deux premières lignes de la grille
        for i in range(2):
            for j in range(math.ceil(random.random()*maGrille.ligne)):
                maGrille.grid[i][j] = ennemis
