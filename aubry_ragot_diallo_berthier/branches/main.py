#Fichier de lancement general.
from grille import *
from hero import *
from ennemis import *


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



    monhero = hero()
    monhero.ajoutHero(maGrille)

    monennemis = ennemis()
    monennemis.ajoutEnnemis(maGrille)

    maGrille.affiche()

    #monhero.gauche(maGrille)

    #monhero.droite(maGrille)




    maGrille.affiche()



main()
