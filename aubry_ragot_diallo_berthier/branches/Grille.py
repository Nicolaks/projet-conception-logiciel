import math
import os

class grille:

    def __init__(self, ligne, colonne):
        #Constructeur
        self.ligne = ligne#La ligne de notre grille.
        self.colonne = colonne#La colonne de notre grille.
        self.grid = []#Permet de créer grille
    def creerGrille(self, val):
        #grid = []
        for i in range(self.ligne):#On parcours le nombres de ligne
            l = [val]*self.colonne#Ajoute à chaque tour de boucle la valeur à la ligne
            print(l)
            self.grid.append(l)#Ajoute la variable l à la grille.
        return self.grid#Retourne la grille.


    def affiche(self):#Fonction qui affiche la grille.
        os.system("clear")#Vide la console a chaque affichage
        #Affiche en mode console
        ch = ""#Créer une liste vide.

        for liste in self.grid:#Boucle qui recherche dans la grille.
            for c in liste:#Boucle qui recherche dans la liste.
                ch += str(c + 5*" ")
            ch += "\n\n"
        print(ch)#Affiche la grille.

#On peut gerer diféramment la grille où l'on ne référence que les objets TIRS,Ennemies,HERO et où l'on ne référence AUCUNE case vide.
