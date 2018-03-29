import pygame

class Button:#qui gère les boutons..
    def __init__(self, width, height, color, text, placementHauteur, placementLargeur, window):
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.placementHauteur = placementHauteur
        self.placementLargeur = placementLargeur
        self.window = window
        self.police = pygame.font.SysFont("monospace", 50)
        self.TxtButton = self.police.render(self.text, True, (255,255,255))


    def afficherTexte(self):#Place le texte dans le bouton.
        placementTexte = (self.placementLargeur/2) - (self.TxtButton.get_width()/2)
        self.window.blit(self.TxtButton,(placementTexte,self.placementHauteur/2))

    def draw(self):#Permet de dessiner le rectangle derriere le texte du bouton.
        button = pygame.draw.rect(self.window, self.color, ((self.placementLargeur/2) - (self.TxtButton.get_width()/2), self.placementHauteur/2, self.width, self.height))
