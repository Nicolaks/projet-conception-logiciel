from tkinter import *
from PIL import Image, ImageTK




class App():#Class de type App qui gère la fenêtre graphique de base.
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.jouer_button = Button(frame, text="Jouer", fg="#ff1122",
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.lancerPartie).pack()#Ajout d'un boutton pour lancer le jeux.

        self.settings_button = Button(frame, text="Paramètres", fg="#aa5500",
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.settings).pack()#Ajout d'un boutton pour l'accès aux paramètres.

        self.quitter_button = Button(frame, text="Quitter", fg="#e84118",
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=frame.quit).pack()#Ajout d'un boutton pour quitter la fenêtre.




    def lancerPartie(self):
        print ("Lancement de la partie")

    def settings(self):
        print("Accès aux paramètres")

root = Tk()
root.title("Le jeu trop bien !!!")
root.geometry("500x400")#Fenètre de 500 par 400
image = Image.open("terre.jpg")
photo = ImageTK.PhotoImage(image)
app = App(root)
root.mainloop()#Boucle principal
print(root.grid_size())
