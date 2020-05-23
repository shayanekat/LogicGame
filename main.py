# Author : Shayane Katchera
# LogicGame Project on tkinter

from tkinter import *

# ====Backend====
#init var
WindowW, WindowH = 500, 500
S = 50


# ====frontend====
root = Tk()
root.title("LogicGame by Shayane Katchera")


main = Canvas(root,width=WindowW,height=WindowH,bg="grey")
main.pack(padx=5,pady=5)

menu = Canvas(root,width=WindowW,height=S,bg="grey")
menu.pack(padx=5,pady=5)


root.mainloop()