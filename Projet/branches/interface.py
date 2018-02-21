from tkinter import *
from main_pygame import *


#from PIL import Image, ImageTK


class App:#Class de type App qui gère la fenêtre graphique de base.
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()

        self.jouer_button = Button(self.frame, text="Jouer", fg="#000000",#
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.lancerPartie).pack()#Ajout d'un boutton pour lancer le jeux et quitter la fenêtre.

        self.settings_button = Button(self.frame, text="Paramètres", fg="#000000",
        relief=RAISED, compound=CENTER,
        width=25, height=5,
        command=self.settings).pack()#Ajout d'un boutton pour l'accès aux paramètres.

        self.quitter_button = Button(self.frame, text="Quitter", fg="#000000",
        relief=RAISED, compound=CENTER,
        width=25, height=5, command=self.quitterPartie).pack()#Ajout d'un boutton pour quitter la fenêtre.




    def lancerPartie(self):#Fonction lancerPartie qui va lancer la partie puis quitter la fenêtre.
        self.master.destroy()
        self.master.quit()
        Jeux()
        
    def settings(self):
        print("Accès aux paramètres")

    def quitterPartie(self):
        self.master.destroy()



root = Tk()
root.title("Le jeu trop bien !!!")
root.geometry("500x400")#Fenètre de 500 par 400

#Mettre en fond d'écran du programme cette image, mais ne fonctionne pas.
#image = Image.open("terre.jpg")#censer ouvrir l'image.
#photo = ImageTK.PhotoImage(image)#cencer appliquer l'image.
app = App(root)
app.frame.quit
root.mainloop()#Boucle principal
