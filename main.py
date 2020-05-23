# Author : Shayane Katchera
# LogicGame Project on tkinter

from tkinter import *
import time

# TODO (23/05/2020): 
# - finish ChangeState method for lever and test it.
# - add mouse binding functions 
# - add others block

# ====Backend====
#init var
WindowW, WindowH = 500, 500
S = 50
selection = ""

#global functions:
def MenuGrid():
    levers = []
    """Fonction qui initialise l'affichage de Menu pour afficher tout les blocks utilisables"""
    l0 = Lever()
    menu.create_rectangle(l0.x, l0.y, l0.x+S, l0.y+S, fill=l0.color)
    menu.create_text(l0.x+int(S//2), l0.y+int(S//2), text=l0.text, font=("Calibri", "12"), fill="white")
    levers.append(l0)
    return(levers)

# POO
class Block():
    """La superclass de tout les blocks de ce jeu \n
     - x,y : position du du coin superieur-gauche \n
     - text : le texte qui sera affiché sur le block \n
     - color : la couleur du block""" 

    def __init__(self, x, y, text="", color="grey"):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.rotation = 0

class Lever(Block):
    def __init__(self, x=0, y=0, text="levier", color="black"):
        Block.__init__(self, x, y, text, color)
        self.state = 0
        self.output = [[self.x+int(S//2), self.y]]
    
    def Place(self):
        main.create_rectangle(self.x, self.y, self.x+S, self.y+S, fill=self.color)
        main.create_text(self.x+int(S//2), self.y+int(S//2), text=self.text, font=("Calibri", "12"), fill="white")

    def ChangeState(self):
        if self.state:
            self.state = 0
            self.color="white"
            main.

# ====frontend====
root = Tk()
root.title("LogicGame by Shayane Katchera")


main = Canvas(root, width=WindowW, height=WindowH, bg="grey")
main.pack(padx=5, pady=5)

menu = Canvas(root, width=WindowW, height=2*S, bg="grey")
menu.pack(padx=5, pady=5)

levers = MenuGrid()
l1 = Lever(100, 200)
l1.Place()

root.mainloop()