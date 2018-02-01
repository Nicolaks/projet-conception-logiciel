import math
import random as rd




class ennemis:#Class qui définit un ennemi.

    def __init__(self):#Constructeur de la class.
        self.posX = 0#Position X de départ.
        self.posY = 0#Position Y de départ.

    def rd_POS(self,colonneGrille):#Ajoute une position random à un ennemis.
        return rd.randint(0,1),rd.randint(0,(colonneGrille - 1))#Utilise la fonction randint permettant de mettre aléatoire.

    def ajoutEnnemis(self, listeEnnemis, maGrille): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        caractereEnnemis = "0"# Le caractère d'un ennemi.

        if len(listeEnnemis) >= 1:#Regarde si la liste des ennemis est supérieur ou égale à 1.
            lPosEnnemis = []
            for enn in listeEnnemis:
                lPosEnnemis.append([enn.posX, enn.posY])

            posX, posY = self.rd_POS(maGrille.colonne)  #Initialisation de position potentiel d'un nouvel ennemi.

            while [posX,posY] in lPosEnnemis:   #Vérification s'il en existe pas un de present sur les positions générés
                posX, posY = self.rd_POS(maGrille.colonne)
        else:
            posX, posY = self.rd_POS(maGrille.colonne)

        print(posX,posY)#Affiche la position de l'ennemi.
        print(maGrille.grid[posX][posY])#Affiche dnas la grille la position de l'ennemi.

        self.posX = posX#Définit la position de l'ennemi en X par rapport à la variable posX.
        self.posY = posY#Définit la position de l'ennemi en Y par rapport à la variable posY.

        maGrille.grid[self.posX][self.posY] = caractereEnnemis #Ajoute un ennemis de façon aléatoire dans le haut de la grille.

    def defile(self,maGrille):#Fait défiler un ennemi vers le bas.
    #A COMPLETER
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.
