try:
    import os
    import sys
    import time
    import pygame
    import json
    from pygame.locals import *

    import pre_settings.Settings as Settings
    import Entity.Reactor as Rct
    import Entity.EntityGroup as ENTGroup
    import Entity.SpaceShip as spaceShip
    import Entity.Ally as Ally
    import Entity.Bullet as Blt
except ImportError as error:
    print(error.__class__.__name__ + " : " + error.msg)
    sys.exit(0)

pygame.init()
Width = 800
Height = 600
fps = 60
BLACK = (255,255,255)
Window = pygame.display.set_mode((Width, Height))
Background = pygame.image.load(os.path.join("..", "Ressources", "Background","Background.jpg")).convert()
Background = pygame.transform.scale(Background, (Width,Height))#Charge l'image
y = 0
Clock = pygame.time.Clock()
pygame.display.set_caption("Manic Shooter : Shot'em up !")
condition = True
while condition:
    delta_time = Clock.tick(fps) * 0.001
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
            condition = False
    Window.fill(BLACK)
    pos_y = y % Background.get_rect().height
    Window.blit(Background,(0,pos_y - Background.get_rect().height))
    y -= 1 #vitesse scroling
    if pos_y < Height:
        Window.blit(Background,(0,pos_y))

    pygame.display.update()


pygame.quit()
quit()
