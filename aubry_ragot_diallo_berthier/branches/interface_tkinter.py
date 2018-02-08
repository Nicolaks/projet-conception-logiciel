from tkinter import *


class App():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.fenetre = create_window()
        self.qbutton = Button(frame, text="Quitter", fg="#e84118",
        command=frame.quit)
        self.qbutton.pack(side=LEFT)
        self.pbutton = Button(frame, text="Jouer", command=self.lancerPartie)
        self.pbutton.pack(side=LEFT)

    def lancerPartie(self):
        print ("Lancement de la partie")


root = Tk()
app = App(root)
root.mainloop()
