#Fichier de lancement general.
from grille import *
from hero import *
#import hero
#import ennemis

def main():
    global colonne
    global ligne
    colonne = int(input("La hauteur de votre grille ? \n"))
    ligne = int(input("La largeur de votre grille ? \n"))
    val = "-"

    maGrille = grille(colonne, ligne)
    maGrille.creerGrille(val)
    maGrille.impaire()
    maGrille.affiche()

    monhero = hero(maGrille)
    monhero.ajoutHero(maGrille.grid)


main()
