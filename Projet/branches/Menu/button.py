import pygame

class Button:#qui gère les boutons..
    def __init__(self, width, height, color, text, placementHauteur, placementLargeur, window, widthtxt = 50):
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.placementHauteur = placementHauteur
        self.placementLargeur = placementLargeur
        self.window = window
        self.police = pygame.font.SysFont("monospace", widthtxt)
        self.TxtButton = self.police.render(self.text, True, (255,255,255))

        self.txtPlacement_x = (self.placementLargeur/2) - (self.TxtButton.get_width()/2)
        self.txtPlacement_y = self.placementHauteur/2

    def afficherTexte(self,txt_x,txt_y):#Place le texte dans le bouton.
        self.window.blit(self.TxtButton,(txt_x,txt_y))

    def draw(self):#Permet de dessiner le rectangle derriere le texte du bouton.
        button = pygame.draw.rect(self.window, self.color, ((self.placementLargeur/2) - (self.TxtButton.get_width()/2), self.placementHauteur/2, self.width, self.height))
