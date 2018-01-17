from grille import *
import math
class hero:

    def __init__(self,grid):

        self.grid = grid

    def ajoutHero(grid): # Permet de mettre le joueur a sa place dans la grille.
        hauteurMap = colonne - 1
        centre = math.ceil(ligne/2) - 1 #placement du hero
        for i in range(len(grid)):
            for j in range(ligne):
                self.grid[hauteurMap][centre] = hero # ajout du hero dans le centre de la liste

#ajout déplacement
