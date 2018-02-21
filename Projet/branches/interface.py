from tkinter import *
#from tkinter import ttk
#from PIL import Image, ImageTk
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


    def lancerPartie(self):#Fonction lancerPartie qui va quitter la fenêtre puis lancer le jeu.
        self.master.destroy()
        self.master.quit()
        Jeux()

    def settings(self):#Fonction qui donneras accès aux paramètres du joueur.
        windows = Toplevel(self.master)
        #self.frame.destroy()

    def quitterPartie(self):#Fonction qui quitte la fenêtre.
        self.master.destroy()



root = Tk()
#canvas = Canvas(root, width =400, height=500, background="blue")
#fond = Image.open(file="terre.gif")
#image = canvas.create_image(0,0, image=fond, anchor = NW)
#canvas.pack()


root.title("Le jeu trop bien !!!")
root.geometry("500x400")#Fenètre de 500 par 400



#Mettre en fond d'écran du programme cette image, mais ne fonctionne pas.
#image = Image.open("terre.jpg")#censer ouvrir l'image.
#photo = ImageTK.PhotoImage(image)#cencer appliquer l'image.
app = App(root)
app.frame.quit
root.mainloop()#Boucle principal
