from grille import *
import math
import random
class ennemis:

    def __init__(self):
        self.posX = 0#Position X de base de ennemis.
        self.posY = 0#Position Y de base de ennemis.



    def ajoutEnnemis(self, maGrille): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        #Que les ennemis ne puissent pas apparaitre sur des autres ennemis ou sur un tire en cours
        ennemis = "0"#Valeur d'un ennemi.
        self.posX = math.ceil(random.random()*2)-1#Apporte une position X aléatoire pour un ennemi.
        self.posY = math.ceil(random.random()*maGrille.ligne)-1#Apporte une position Y aléatoire pour un ennemi.
        maGrille.grid[self.posX][self.posY] = ennemis#Ajoute un ennemis de façon aléatoire dans le haut de la grille.


    def defile(self,maGrille):#Fonction qui fait défiler vers le bas un ennemi.
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.



    def collision(self):#Fonction gérant les collisions.

        return None
