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
        self.posX = math.ceil(random.random()*2)-1
        self.posY = math.ceil(random.random()*maGrille.ligne)-1
        maGrille.grid[self.posX][self.posY] = ennemis#Ajoute un ennemis de façon aléatoire dans le haut de la grille.


    def defile(self,maGrille):
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.



    def collision(self):

        return None
