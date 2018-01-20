from grille import *
import math
class hero:

    def __init__(self):
        #Constructeur
        self.posX = 0
        self.posY = 0



    def ajoutHero(self, maGrille): #Permet l'ajout du héro.

        hauteurMap = maGrille.colonne - 1
        centre = math.ceil(maGrille.ligne/2) - 1 #placement du hero
        self.posX = hauteurMap #On obtient les coordonnees X
        self.posY = centre#On obtient les coordonnees Y du hero.
        posHero = "1"#Un hero vaut le chiffre 1.
        for i in range(len(maGrille.grid)):#Parcours la longueur de la grille
            for j in range(maGrille.ligne):#Parcours la longueur de la ligne
                maGrille.grid[hauteurMap][centre] = posHero # ajout du hero dans le centre de la liste


    def gauche(self, maGrille):#Permet de faire déplacer le héro vers la gauche.

        hauteurMap = maGrille.colonne - 1 #La hauteur de la grille (-1 parce que l'on est en python).
        centre = math.ceil(maGrille.ligne/2) - 2 #placement du hero

        if self.posY - 1 > -1: #Vérifie que la position ne depasse pas la grille de gauche
            maGrille.grid[self.posX][self.posY] = "-"#Remplace la position precedente
            self.posY -= 1#Lui donne une nouvelle direction
            posHero = "1"#Un hero vaut le chiffre 1.
            maGrille.grid[self.posX][self.posY] = posHero#Applique la direction

    def droite(self, maGrille):#Permet de faire se déplacer le héro sur la droite.

        hauteurMap = maGrille.colonne - 1 #La hauteur de la grille (-1 parce que l'on est en python).
        centre = math.ceil(maGrille.ligne/2) - 2 #placement du hero

        if self.posY + 1 < maGrille.ligne:#Vérifie que la position ne dépasse pas la grille sur la droite.
            maGrille.grid[self.posX][self.posY] = "-"#Remplace la position precedente
            self.posY += 1#Lui donne une nouvelle direction
            posHero = "1"#Un hero vaut le chiffre 1.
            maGrille.grid[self.posX][self.posY] = posHero#Applique la direction

#Arriver à ajouter le tire sur la grille en jouant avec les position de celle-ci.
    def tirer(self, maGrille):

        if self.posX -1 > -1 and self.posX + 1 < maGrille.colonne:
            posXTire = self.posX
            posYTire = self.posY + 1
            maGrille.grid[posXTire][posYTire] = "|"
