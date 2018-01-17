#####################################
#h = hauteur
#l = largeur
#
#####################################

import math

global h
global l
global hero
global ennemis
global vide

hero = "1"
ennemis = "0"
vide = "-"

h = int(input("La hauteur de votre grille ? \n"))
l = int(input("La largeur de votre grille ? \n"))

#Créer une grille de hauteur h, de largeur l, remplie de valeur val.
def creerGrille(n,p,val):
    grid = []
    for i in range(n):
        l = [val]*p
        grid.append(l)
    return grid

def affiche(grille):
    #Affiche en mode console
    ch = ""
    for j in range(len(grille)):
        for i in range(len(grille[j])):
            ch += str(grille[j][i]) + (1+4-len(str(grille[j][i])))* " "
        ch += "\n \n"
    print(ch)

def impaire_inf_a_h(l,h):
    while(l%2==0)or(l>=h):
        l = int(input("La largeur de votre grille doit être impaire et inferieur à la hauteur ? \n"))
    return l


def ajoutEnnemis(grid):
    for i in range(2):
        for j in range(l):
            grid[i][j] = ennemis
    return grid


def ajoutHero(grid): # Permet de mettre le joueur a sa place dans la grille.
    hauteurMap = h - 1
    centre = math.ceil(l/2) - 1
    for i in range(h):
        for j in range(l):
            grid[hauteurMap][centre] = hero


l = impaire_inf_a_h(l,h)
grid = creerGrille(h, l, vide)
grid = ajoutEnnemis(grid)
ajoutHero(grid)
affiche(grid)
