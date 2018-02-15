from tkinter import *


#from PIL import Image, ImageTK


class App:#Class de type App qui gère la fenêtre graphique de base.
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.jouer_button = Button(self.frame, text="Jouer", fg="#000000",#
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.frame.quit).pack()#Ajout d'un boutton pour lancer le jeux et quitter la fenêtre.

        self.settings_button = Button(self.frame, text="Paramètres", fg="#000000",
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.settings).pack()#Ajout d'un boutton pour l'accès aux paramètres.

        self.quitter_button = Button(self.frame, text="Quitter", fg="#000000",
        relief=RAISED, compound=CENTER,
        width=25, height=5).pack()#Ajout d'un boutton pour quitter la fenêtre.




    def lancerPartie(self):#Fonction lancerPartie qui va lancer la partie puis quitter la fenêtre.
        self.frame.quit


    def settings(self):
        print("Accès aux paramètres")
