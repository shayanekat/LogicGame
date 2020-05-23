# Author : Shayane Katchera
# LogicGame Project on tkinter

from tkinter import *
import time

# TODO (23/05/2020): 
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
    l0.id = menu.create_rectangle(l0.x, l0.y, l0.x+S, l0.y+S, fill=l0.color, outline="black")
    l0.idt = menu.create_text(l0.x+int(S//2), l0.y+int(S//2), text=l0.text, font=("Calibri", "12"), fill="white")
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
        self.id = 0
        self.idt = 0

class Lever(Block):
    """Class Levier qui descent de Block \n
     - input
     - etat 0 : la sortie est a 0
     - etat 1 : la sortie est a 1
     """
    def __init__(self, x=0, y=0, text="levier", color="black"):
        Block.__init__(self, x, y, text, color)
        self.state = 0
        self.output = [[self.x+int(S//2), self.y]]
    
    def Place(self):
        """ Methode qui sert a placer le block dans la fenetre. Va encore changer car doit inclure le click de souris"""
        self.id = main.create_rectangle(self.x, self.y, self.x+S, self.y+S, fill=self.color, outline="black")
        self.idt = main.create_text(self.x+int(S//2), self.y+int(S//2), text=self.text, font=("Calibri", "12"), fill="white")

    def ChangeState(self):
        """ Methode principale : le changement d'etat du levier entre 0 et 1. va encore changer """
        self.state = not(self.state)
        main.delete(self.idt)
        if self.state:
            self.color="black"
            self.idt = main.create_text(self.x+int(S//2), self.y+int(S//2), text=self.text, font=("Calibri", "12"), fill="white")
        else:
            self.color="white"
            self.idt = main.create_text(self.x+int(S//2), self.y+int(S//2), text=self.text, font=("Calibri", "12"), fill="black")
        main.itemconfig(self.id, fill=self.color)


# fonctions globales
def test():
    """ Fonction temporaire de bouton pour tester le code"""
    l1.ChangeState()

def menuMLC(event):
    """Fonction deu click gauche de souris dans le menu : selection du block"""
    global selection
    if event.x // S == 0 and event.y // S == 0:
        selection = "lever"
        menu.itemconfig(levers[0].id, outline="blue", width=3)

# ====frontend====
root = Tk()
root.title("LogicGame by Shayane Katchera")

# canevas
main = Canvas(root, width=WindowW, height=WindowH, bg="grey")
main.pack(padx=5, pady=5)

menu = Canvas(root, width=WindowW, height=2*S, bg="grey")
menu.bind("<Button-1>", menuMLC)
menu.pack(padx=5, pady=5)

# test
levers = MenuGrid()
l1 = Lever(100, 200)
l1.Place()

b = Button(root,text="test",command=test)
b.pack()


root.mainloop()