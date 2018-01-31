import math

class grille:

    def __init__(self, x, y):
        #Constructeur

        self.colonne = x
        self.ligne = y
        self.grid = []

    def creerGrille(self, val):#Fonction qui crée la grille
        #grid = []
        for i in range(self.colonne):#Parcours la taille de la colonne
            l = [val]*self.ligne#Ajoute à chaque tour de boucle la valeur à la ligne
            self.grid.append(l)#Ajoute la variable l à la grille.
        return self.grid#Retourne la grille.


    def affiche(self):#Fonction permettant d'afficher la grille.
        #Affiche en mode console
        ch = ""#Créer une liste vide.
        ligne = self.ligne
        colonne = self.colonne
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                ch += str(self.grid[j][i]) + (1+4-len(str(self.grid[j][i])))* " "
            ch += "\n \n"
        print(ch)

    #Verifie si la largeur de la grille est inférieure est impair.
    #Si c'est le cas alors une boucle while se charge de redemmander une réponse.
    def impaire(self):
        while(self.ligne%2 == 0) or (self.ligne>= self.colonne):
            self.ligne = int(input("La largeur de votre grille doit être impaire et inferieur à la hauteur ? \n"))#Demande une valeur inférieure et impaire.
        return self.ligne
