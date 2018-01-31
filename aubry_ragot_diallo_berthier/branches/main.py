#Fichier de lancement general.
from grille import *
from hero import *
from ennemis import *
from tire import *



def main():
    global colonne
    global ligne
    global val
    val = "-"
    colonne = int(input("La hauteur de votre grille ? \n"))
    ligne = int(input("La largeur de votre grille ? \n"))


    continuer = True

    maGrille = grille(colonne, ligne)
    maGrille.creerGrille(val)
    maGrille.impaire()
    maGrille.affiche()

    monhero = hero()
    monhero.ajoutHero(maGrille)


    monennemis = ennemis()
    monennemis.ajoutEnnemis(maGrille)


    maGrille.affiche()#Permet d'afficher la grille du jeu.
    #A remplacer par un dictionnaire.
    listeTire = []#Liste qui va contenir les instances des tirs.
    #A remplacer par un dictionnaire.
    listeEnnemis = []#Liste qui va contenir les instances des ennemis.

    while continuer:#Boucle pour le jeu.

        rep = input("Que voulez-vous faire ?")#En attente de la réponse du joueur.




        if rep == "t":#Vérifie les touches clavier pour le tir.
            tir = tire(monhero)
            tir.tirer(maGrille)
            listeTire.append(tir)
            maGrille.affiche()

        elif rep == "g":#Vérifie les touches clavier pour aller à gauche.
            if len(listeTire) >= 1:
                monhero.gauche(maGrille)#Fait aller le joueur à gauche.
                maGrille.affiche()
                listeTire[0].tire(maGrille, monennemis)
                if tir.posXTire == monennemis.posX:#Vérifie la collision entre l'ennemie et le tir.
                    maGrille.grid[tir.posXTire][tir.posYTire] = "-"#Remplace le tir par la val de défaut.
                    listeTire.remove(listeTire[0])#Enléve le tir de la liste.
            else:
                monhero.gauche(maGrille)#Fait aller le joueur à gauche.
                maGrille.affiche()

        elif rep == "d":#Vérifie les touches clavier pour aller à droite.
            if len(listeTire) > 0:
                monhero.droite(maGrille)#Fait aller le joueur à droite.
                maGrille.affiche()
                listeTire[0].tire(maGrille, monennemis)#Prend le premier tir de la liste et le fait tirer(défiler).
                if tir.posXTire == monennemis.posX:#Vérifie la collision entre l'ennemie et le tir.
                    maGrille.grid[tir.posXTire][tir.posYTire] = "-"#Remplace le tir par la val de défaut.
                    listeTire.remove(listeTire[0])#Enléve le tir de la liste.
            else:
                monhero.droite(maGrille)#Fait aller le héro à droite.
                maGrille.affiche()#Affiche la grille.

        elif rep == "quitter":#Vérifie les touches clavier pour quitter la partie.
            continuer = False;#Permet de stopper la boucle principal.

        maGrille.affiche()#Affiche la grille.

main()
