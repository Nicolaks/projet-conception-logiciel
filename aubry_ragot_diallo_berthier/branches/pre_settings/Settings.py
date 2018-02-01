#Fichier de sauvegarde de SCORE, changement des touches assignés, récupération des scores et touches
import pygame
def modifier(self):
    return True

def settings():
    try:
        fichier = open("settings.txt","r")
    except:
        fichier = open("settings.txt","w")#on creer et ecrit dans settings.txt les differentes touche du jeux
        fichier.write("-up-=_pygame.KUP_\n")
        fichier.write("-down-=_pygame.KDOWN_\n")
        fichier.write("-left-=_pygame.KLEFT_\n")
        fichier.write("-right-=_pygame.KRIGHT_\n"),
        fichier.write("-tir-=_pygame.KSPACE_\n")
        fichier.write("-scores-=_{}_\n")
    fichier.close()



settings()
