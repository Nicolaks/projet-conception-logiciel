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

        listeTire = []


        if rep == "t":
            tir = tire(monhero)
            tir.tirer(maGrille)
            listeTire.append(tir)
            print(listeTire)

        elif rep == "g":
            print(len(listeTire))
            if len(listeTire) >= 1:
                monhero.gauche(maGrille)
                maGrille.affiche()
                print("text")
                #tire1.tire(maGrille, monennemis)
                listeTire[0].tire(maGrille, monennemis)
                print(listeTire[0].posXTire)
            else:
                monhero.gauche(maGrille)
                maGrille.affiche()
                print("else")

        elif rep == "d":
            if len(listeTire) > 0:
                monhero.droite(maGrille)
                maGrille.affiche()
                listeTire[0].tire(maGrille, monennemis)
            else:
                monhero.droite(maGrille)
                maGrille.affiche()

        elif rep == "q" or rep == "quitter":
            continuer = False;

        maGrille.affiche()

main()
