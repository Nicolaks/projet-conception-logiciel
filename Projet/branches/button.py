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


        global textBtn
        global police
        police = pygame.font.SysFont("monospace", 50)
        textBtn = police.render(self.text, True, (255,255,255))


    def afficherTexte(self):
        placementTexte = (self.Lfen/2) - (textBtn.get_width()/2)
        self.window.blit(textBtn,(placementTexte,self.Hfen/2))

    def draw(self):
        button = pygame.draw.rect(self.window, self.color, ((self.Lfen/2) - (textBtn.get_width()/2), self.Hfen/2, self.width, self.height))

    def commande(self):
        if self.width+self.height > mouse[0] > self.width and self.width + self.height > mouse[1] > self.height:
            pygame.draw.rect(self.window, (0,0,0),((self.Lfen/2) - (textBtn.get_width()/2), self.Hfen/2, self.width, self.height))
            if click[0] == 1 and action != None:
                print("coucou")
