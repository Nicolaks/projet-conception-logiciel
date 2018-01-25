#Fichier de lancement general.
from grille import *
from hero import *
from ennemis import *
from tire import *



def main():
    global colonne
    global ligne
    colonne = int(input("La hauteur de votre grille ? \n"))
    ligne = int(input("La largeur de votre grille ? \n"))
    val = "-"

    continuer = True

    maGrille = grille(colonne, ligne)
    maGrille.creerGrille(val)
    maGrille.impaire()
    maGrille.affiche()

    monhero = hero()
    monhero.ajoutHero(maGrille)


    monennemis = ennemis()
    monennemis.ajoutEnnemis(maGrille)

    maGrille.affiche()

    while continuer:

        rep = input("Que voulez-vous faire ?")

        if rep == "g":
            if isinstance(tire1, tire):
                monhero.gauche(maGrille)
                maGrille.affiche()
                tire1.tire(maGrille, monennemis)
            else:
                monhero.gauche(maGrille)
                maGrille.affiche()

        elif rep == "d":
            if isinstance(tire1, tire):
                monhero.droite(maGrille)
                maGrille.affiche()
                tire1.tire(maGrille, monennemis)
            else:
                monhero.droite(maGrille)
                maGrille.affiche()
        elif rep == "t":
            tire1 = tire(monhero)
            tire1.tirer(maGrille)

        maGrille.affiche()

main()
