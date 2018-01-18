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
        posHero = "1"
        for i in range(len(maGrille.grid)):
            for j in range(maGrille.ligne):
                maGrille.grid[hauteurMap][centre] = posHero # ajout du hero dans le centre de la liste


    def gauche(self, maGrille):#Permet de faire déplacer le héro vers la gauche.

        hauteurMap = maGrille.colonne - 1
        centre = math.ceil(maGrille.ligne/2) - 2 #placement du hero

        if self.posY - 1 > -1:
            maGrille.grid[self.posX][self.posY] = "-"
            self.posY -= 1
            posHero = "1"
            maGrille.grid[self.posX][self.posY] = posHero

    def droite(self, maGrille):#Permet de faire se déplacer le héro sur la droite.

        hauteurMap = maGrille.colonne - 1
        centre = math.ceil(maGrille.ligne/2) - 2 #placement du hero

        if self.posY + 1 < maGrille.ligne:#Vérifie que la position ne dépasse pas 
            maGrille.grid[self.posX][self.posY] = "-"
            self.posY += 1
            posHero = "1"
            maGrille.grid[self.posX][self.posY] = posHero
