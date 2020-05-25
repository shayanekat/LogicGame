# Author : Shayane Katchera
# LogicGame Project on tkinter

from tkinter import *
import time

# TODO (25/05/2020): 
# - finish clock
# - add display for classes (print(l0) for example)
# - add middle mouse click to delete object
# - add middle mouse wheel to change menu selection

# =========================BACKEND=========================
#init var
WindowW, WindowH = 500, 500     # taille canvas (pixel)
S = 50                          # taille block
selection = ""                  # variable pour savoir block selected

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

    def Place(self):
        """ Methode qui sert a placer le block dans la fenetre. Va encore changer car doit inclure le click de souris"""
        self.id = main.create_rectangle(self.x, self.y, self.x+S, self.y+S, fill=self.color, outline="black")
        self.idt = main.create_text(self.x+int(S//2), self.y+int(S//2), text=self.text, font=("Calibri", "12"), fill="white")

class Lever(Block):
    """Class Levier qui descent de Block \n
     - input \n
     - etat 0 : la sortie est a 0 \n
     - etat 1 : la sortie est a 1 
     """
    def __init__(self, x=0, y=0, text="levier", color="black"):
        Block.__init__(self, x, y, text, color)
        self.state = 0
        self.output = [[self.x+int(S//2), self.y]]

    def ChangeState(self):
        """ Methode principale : le changement d'etat du levier entre 0 et 1. va encore changer """
        self.state = not(self.state)
        if self.state:
            self.color="white"
            main.itemconfig(self.idt, fill="black")
        else:
            self.color="black"
            main.itemconfig(self.idt, fill="white")
        main.itemconfig(self.id, fill=self.color)


class Boutton(Block):
    """Class Bouton qui descent de Block \n
     - input \n 
     - etat 0 : la sortie est a 0 \n
     - etat 1 : la sortie est a 1 pendant une seconde \n
     - la sortie repasse à 0
     """
    def __init__(self, x=0, y=0, text="boutton", color="black"):
        Block.__init__(self, x, y, text, color)
        self.state = 0
        self.output = [[self.x+int(S//2), self.y]]

    def Use(self):
        """ Methode principale : le boutton passe a 1 pendant une seconde """
        self.state = 1
        self.color="white"
        main.itemconfig(self.idt, fill="black")
        main.itemconfig(self.id, fill=self.color)
        main.update()

        time.sleep(1)

        self.state = 0
        self.color="black"
        main.itemconfig(self.idt, fill="white")
        main.itemconfig(self.id, fill=self.color)
        main.update()


class Clock(Block):
    """Class Bouton qui descent de Block \n
     - input \n
     - oscille entre 0 et 1 à une frequence de 1hz, 2hz si rc
     """
    def __init__(self, x=0, y=0, text="clock", color="black"):
        Block.__init__(self, x, y, text, color)
        self.state = 0
        self.output = [[self.x+int(S//2), self.y]]
        self.period = 1
        # self.Use()
    
    def Use(self):
        """ Methode principale : le bouton oscille entre 0 et 1 a une certaine frequence"""
        self.state = 1
        self.color="white"
        main.itemconfig(self.idt, fill="black")
        main.itemconfig(self.id, fill=self.color)
        main.update()

        time.sleep(self.period/2)

        self.state = 0
        self.color="black"
        main.itemconfig(self.idt, fill="white")
        main.itemconfig(self.id, fill=self.color)
        main.update()

        time.sleep(self.period/2)
        self.Use()
    
    

# fonctions globales
def MenuGrid():
    """Fonction qui initialise l'affichage de Menu pour afficher tout les blocks utilisables"""
    levers = []
    bouttons = []
    clocks = []

    l0 = Lever()
    b0 = Boutton(x = S)
    c0 = Clock(x = 2*S)

    l0.id = menu.create_rectangle(l0.x, l0.y, l0.x+S, l0.y+S, fill=l0.color, outline="black")
    l0.idt = menu.create_text(l0.x+int(S//2), l0.y+int(S//2), text=l0.text, font=("Calibri", "12"), fill="white")
    b0.id = menu.create_rectangle(b0.x, b0.y, b0.x+S, b0.y+S, fill=b0.color, outline="black")
    b0.idt = menu.create_text(b0.x+int(S//2), b0.y+int(S//2), text=b0.text, font=("Calibri", "12"), fill="white")
    c0.id = menu.create_rectangle(c0.x, c0.y, c0.x+S, c0.y+S, fill=c0.color, outline="black")
    c0.idt = menu.create_text(c0.x+int(S//2), c0.y+int(S//2), text=c0.text, font=("Calibri", "12"), fill="white")

    levers.append(l0)
    bouttons.append(b0)
    clocks.append(c0)

    return(levers, bouttons, clocks)


def test():
    """ Fonction temporaire de bouton pour tester le code"""
    pass


def menuMLC(event):
    """Fonction de click gauche de souris dans le menu : selection du block"""
    global selection
    unselect()
    if event.y // S == 0:
        if event.x // S == 0 :
            selection = "lever"
            menu.itemconfig(levers[0].id, outline="blue", width=3)

        elif event.x // S == 1:
            selection = "boutton"
            menu.itemconfig(bouttons[0].id, outline="blue", width=3)
        
        elif event.x // S == 2:
            selection = "clock"
            menu.itemconfig(clocks[0].id, outline="blue", width=3)

def mainMLC(event):
    """ Fonction de click gauche de souris dans main : placer block selectionné | selection pour le wire"""
    if selection == "lever":
        l = Lever(x=event.x-S//2,y=event.y-S//2)
        l.Place()
        levers.append(l)
    
    elif selection == "boutton":
        btn = Boutton(x=event.x-S//2,y=event.y-S//2)
        btn.Place()
        bouttons.append(btn)
    
    elif selection == "clock":
        clk = Clock(x=event.x-S//2,y=event.y-S//2)
        clk.Place()
        clocks.append(clk)


def mainMRC(event):
    """ Fonction de click droit de souris dans main : utiliser l'input """
    for l in levers:
        if l.x <= event.x <= l.x+S and l.y <= event.y <= l.y+S:
            l.ChangeState()
            break
    
    for btn in bouttons:
        if btn.x <= event.x <= btn.x+S and btn.y <= event.y <= btn.y+S:
            btn.Use()
            break
    
    for clk in clocks:
        if clk.x <= event.x <= clk.x+S and clk.y <= event.y <= clk.y+S:
            if clk.period == 1:
                clk.period = 0.5
            else:
                clk.period = 1
            break


def unselect():
    if selection == "lever":
        menu.itemconfig(levers[0].id, outline="black", width=1)
    elif selection == "boutton":
        menu.itemconfig(bouttons[0].id, outline="black", width=1)
    elif selection == "clock":
        menu.itemconfig(clocks[0].id, outline="black", width=1)


# =========================FRONTEND=========================
root = Tk()
root.title("LogicGame by Shayane Katchera")

# canevas
main = Canvas(root, width=WindowW, height=WindowH, bg="grey")
main.pack(padx=5, pady=5)

menu = Canvas(root, width=WindowW, height=2*S, bg="grey")
menu.pack(padx=5, pady=5)

# init
levers, bouttons, clocks = MenuGrid()
menu.bind("<Button-1>", menuMLC)
main.bind("<Button-1>", mainMLC)
main.bind("<Button-3>", mainMRC)

# test
b = Button(root,text="test",command=test)
b.pack()


root.mainloop()