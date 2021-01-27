import tkinter
from tkinter import messagebox

vPrincipal = tkinter.Tk()

vPrincipal.title("A04 Control teclado")

def fnCerrar():
    if messagebox.askokcancel("Salir", "Desea salir de la aplicacion"):
        vPrincipal.destroy()

def fnShowInfo(evento):
    print("ShowInfo:", evento)
    messagebox.showinfo("Show info", "04 NessageBox")

def fnShowError(evento):
    print("ShowError:", evento)
    messagebox.showerror("Show Error", "04 MessageBox")

def fnShowWarning(evento):
    print("showWargning:", evento)
    messagebox.showwarning("Show warning",  "04 Message Box ")

def fnAskYesNo(evento):
    print("AskYesNo", evento)
    messagebox.askyesno("Salir con return", "¿Desea Salir de la aplicacion?")

def fnAskRetryCancel(evento):
    print("AskRetyCancel:", evento)
    messagebox.askretrycancel("Salir con escape", "¿Desa salir de la aplicacion?")

vPrincipal.protocol("WM_DELETE_WINDOW", fnCerrar)

vPrincipal.bind("<Control-Key-1>", fnShowInfo)
vPrincipal.bind("<Control-Key-2>", fnShowError)
vPrincipal.bind("<F1>", fnShowWarning)
vPrincipal.bind("<Return>", fnAskYesNo)
vPrincipal.bind("<Escape>", fnAskRetryCancel)

vPrincipal.mainloop()
