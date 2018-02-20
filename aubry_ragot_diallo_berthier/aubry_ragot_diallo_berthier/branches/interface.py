import os
import pygame


pygame.init()#Initialise la fenêtre pygame.

fps = 30 #IPS ou Frame per seconds.
Height = 800 #Hauteur.
Width = 500 #Largeur.
largeur_button = 250#C'est la Largeur du boutton.
hauteur_button = 60#C'est la hauteur du boutton.
positionButtonX = (Width/2) - largeur_button/2#C'est la position en X du boutton dans la fenêtre.
positionButtonY = (Height/2) - hauteur_button#C'est la position en Y du boutton dans la fenêtre.

screen = pygame.display.set_mode((Width,Height))#Mets à jour la taille de la fenêtre.
pygame.display.set_caption("menu")#Donne un titre à la fenêtre.

background_color = (220,221,225)#Couleur de fond de la fenêtre.
screen.fill(background_color)#Ajoute la couleur de fond.

color_button = (232,65,24)#C'est la couleur de notre boutton.
color_hover_button = (194,54,22)#Couleur lors du passage de la souris.
texte_Boutton = text_objects("Jouer")#Texte mis dans le boutton.

#Ici on l'intancie.
#quit_button = pygame.draw.rect(screen,color_button, (positionButtonX,positionButtonY + 120,largeur_button,hauteur_button))#Boutton quit permettant de quitter le jeu.



pygame.display.flip()#Mets à jour la totalité de la surface de l'écran pygame.

Pre_game_Menu = True#Variable pour la boucle.
keys = []
while Pre_game_Menu:
    pygame.time.Clock().tick(fps)
    mouse = pygame.mouse.get_pos()#Permet d'avoir la position de la souris.

    if positionButtonX + largeur_button > mouse[0] > positionButtonX and positionButtonY + hauteur_button > mouse[1] > positionButtonY:
        start_button = pygame.draw.rect(screen,color_hover_button,(positionButtonX,positionButtonY,largeur_button,hauteur_button))#Boutton start permettant de lancer le jeu.
    else:
        start_button = pygame.draw.rect(screen,color_button, (positionButtonX,positionButtonY,largeur_button,hauteur_button))#Boutton start permettant de lancer le jeu.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_mods()
            print(key)
            pygame.display.update()
            if event.key == pygame.K_ESCAPE:
                preset = False
    pygame.display.flip()#Mets à jour la totalité de la surface de l'écran pygame.
