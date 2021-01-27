import tkinter

from tkinter import *

from tkinter import messagebox

vPrincipal = tkinter.Tk()

vPrincipal.geometry("800x600+10+10")

vPrincipal.title("A06 LabelImagen")

img = PhotoImage(file='img/kurisu.png')

lblLogo = Label(vPrincipal, image=img, relief=RAISED)


lblLogo.pack()
# lblLogo.pack(fill=X)
# lblLogo.pack(fill = Y, expand = 1)
# lblLogo.pack(fill = BOTH, expand=1)

def fnLabelClick(e):
    print("Click: ", e, e.type, e.state)
    messagebox.showinfo("Click", "Sobre la imagen")

def fnLabelEnter(e):
    print("Enter:", e, e.type, e.focus, e.state)
    print("Enter:", e)


def fnLabelLeave(e):
    print("Leave:", e, e.type, e.focus, e.state)


lblLogo.bind("<Button-1>", fnLabelClick)
lblLogo.bind("<Enter>", fnLabelEnter)
lblLogo.bind("<Leave>", fnLabelLeave)
vPrincipal.mainloop()
