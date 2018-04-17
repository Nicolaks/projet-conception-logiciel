from tkinter import *
from main_pygame import *


global couleurPrincipale
couleurPrincipale = "#E6DCBF"


class App:#Class de type App qui gère la fenêtre graphique de base.
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.config(bg=couleurPrincipale)
        self.frame.pack()


        self.jouer_button = Button(self.frame, text="Jouer", fg="#000000",#
        relief=RAISED, compound=CENTER,
        width=25, height=5, bg=couleurPrincipale,
        command=self.lancerPartie).pack()#Ajout d'un boutton pour lancer le jeux et quitter la fenêtre.

        self.quitter_button = Button(self.frame, text="Quitter", fg="#000000",
        relief=RAISED, compound=CENTER, bg=couleurPrincipale,
        width=25, height=5, command=self.quitterPartie).pack()#Ajout d'un boutton pour quitter la fenêtre.

        #self.labelWidth = Label(self.master, text="La taille en largeur: ", width=50).pack()
        #self.inputWidth = Entry(self.master, width=50)
        #self.inputWidth.pack()

        #self.labelHeight = Label(self.master, text="La taille en hauteur: ", width=50).pack()
        #self.inputHeight = Entry(master, width=50)
        #self.inputHeight.pack()

        self.labelPlace = Label(self.master, text="", height=5).pack()
        self.label = Label(self.master, text="Résolution", width=11).pack()

        self.listbox = Listbox(self.master, width=11, height=3)
        self.listbox.insert(0, "1920 X 1080")
        self.listbox.insert(1, "1280 X 720")
        self.listbox.insert(2, "1020 X 480")
        self.listbox.pack()

    def lancerPartie(self):#Fonction lancerPartie qui va quitter la fenêtre puis lancer le jeu.
        self.master.destroy()
        self.master.quit()
        Jeux(50,50)


    def quitterPartie(self):#Fonction qui quitte la fenêtre.
        self.master.destroy()


root = Tk()


root.title("Manic shooter")
root.geometry("500x400")#Fenètre de 500 par 400

app = App(root)
app.frame.quit
root.mainloop()#Boucle principal
