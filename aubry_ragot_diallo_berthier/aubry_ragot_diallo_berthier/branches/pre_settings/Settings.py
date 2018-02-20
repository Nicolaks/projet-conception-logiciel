
try:#On regarde si le fichier existe ou non.
    fichier = open("settings.txt","r")#Si il existe on le regarde à l'intérieur.
except:#Sinon.
    fichier = open("settings.txt","w")#on creer et ecrit dans settings.txt les differentes touches du jeux
    fichier.write("up=pygame.KUP\n")#Mets les valeurs.
    fichier.write("down=pygame.KDOWN\n")#Mets les valeurs.
    fichier.write("left=pygame.KLEFT\n")#Mets les valeurs.
    fichier.write("right=pygame.KRIGHT\n"),#Mets les valeurs.
    fichier.write("tir=pygame.KSPACE\n")#Mets les valeurs.
    fichier.write("scores={}\n")#Mets les valeurs.
fichier.close()#Ferme le fichier


def lecture():#Fonction qui va faire une lecture du fichier pour en extraire des informations.

    fichier = open("settings.txt", "r")#Ouvre le fichier.
    tableau = {}#Initialise un dictionnaire vide.
    for ligne in fichier:#On regarde chaque ligne du fichier.
        ligne = ligne.replace("\n", "")#On enlève les retours à la ligne.
        ligne = ligne.split("=")#On split par rapport au signe "=".
        tableau[ligne[0]] = ligne[1]#On ajoute dans le dictionnaire les nouvelles valeurs.

    print(tableau)#On affiche pour le vérifier.


lecture()#On lance la fonction.
