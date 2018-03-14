import pygame

class Button:#qui gère les boutons..
    def __init__(self, width, height, color, text, Hfen, Lfen, window):
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.Hfen = Hfen
        self.Lfen = Lfen
        self.window = window
        self.police = pygame.font.SysFont("monospace", 50)

    def draw(self):
        button = pygame.draw.rect(self.window, self.color, (self.Lfen, self.Hfen, self.width, self.height))
    def afficherTexte(self):
        police = pygame.font.SysFont("monospace", 50)
        textTitre = police.render(self.text, True, (255,255,255))
