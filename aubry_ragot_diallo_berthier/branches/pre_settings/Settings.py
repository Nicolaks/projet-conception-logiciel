#Fichier de sauvegarde de SCORE, changement des touches assignés, récupération des scores et touches

try:
    fichier = open("settings.txt","r")
except:
    fichier = open("settings.txt","w")#on creer et ecrit dans settings.txt les differentes touche du jeux
    fichier.write("up=pygame.KUP\n")
    fichier.write("down=pygame.KDOWN\n")
    fichier.write("left=pygame.KLEFT\n")
    fichier.write("right=pygame.KRIGHT\n"),
    fichier.write("tir=pygame.KSPACE\n")
    fichier.write("scores={}\n")
fichier.close()


def lecture():

    fichier = open("settings.txt", "r")
    tableau = {}
    for ligne in fichier:
        ligne = ligne.replace("\n", "")
        ligne = ligne.split("=")
        tableau[ligne[0]] = ligne[1]

    print(tableau)


lecture()
