#####LE CHANGER EN JSON FILE, Utilisation plus simple
try:#On regarde si le file existe ou non.
    file = open("settings.txt","r")#Si il existe on le regarde à l'intérieur.
except:#Sinon.
    file = open("settings.txt","w")#on creer et ecrit dans settings.txt les differentes touches du jeux
    file.write("up=up\n")#Mets les valeurs.
    file.write("down=down\n")#Mets les valeurs.
    file.write("left=left\n")#Mets les valeurs.
    file.write("right=right\n"),#Mets les valeurs.
    file.write("tir=space\n")#Mets les valeurs.
    file.write("scores={}\n")#Mets les valeurs.
file.close()#Ferme le file.


def lecture():#Fonction qui va faire une lecture du file pour en extraire des informations.

    file = open("settings.txt", "r")#Ouvre le file.
    tableau = {}#Initialise un dictionnaire vide.

    for ligne in file:#On regarde chaque ligne du file.
        ligne = ligne.replace("\n", "")#On enlève les retours à la ligne.
        ligne = ligne.split("=")#On split par rapport au signe "=".
        tableau[ligne[0]] = ligne[1]#On ajoute dans le dictionnaire les nouvelles valeurs.

    print(tableau)#On affiche pour le vérifier.


lecture()#On lance la fonction.
