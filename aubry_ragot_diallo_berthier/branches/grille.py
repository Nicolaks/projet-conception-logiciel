import math

class grille:

    def __init__(self, x, y):
        #Constructeur

        self.colonne = x
        self.ligne = y
        self.grid = []

    def creerGrille(self, val):
        #grid = []
        for i in range(self.colonne):
            l = [val]*self.ligne
            self.grid.append(l)
        return self.grid



    #Ne fonctionne pas encore, en utilsant les objets.
    def affiche(self):
        #Affiche en mode console
        ch = ""
        ligne = self.ligne
        colonne = self.colonne
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                ch += str(self.grid[j][i]) + (1+4-len(str(self.grid[j][i])))* " "
            ch += "\n \n"
        print(ch)

    #Verifie si la largeur de la grille est inférieure est impair.
    def impaire(self):
        while(self.ligne%2 == 0) or (self.ligne>= self.colonne):
            self.ligne = int(input("La largeur de votre grille doit être impaire et inferieur à la hauteur ? \n"))
        return self.ligne


def main():
    colonne = int(input("La hauteur de votre grille ? \n"))
    ligne = int(input("La largeur de votre grille ? \n"))
    val = "-"

    maGrille = grille(colonne, ligne)
    maGrille.creerGrille(val)
    maGrille.impaire()
    maGrille.affiche()


main()
