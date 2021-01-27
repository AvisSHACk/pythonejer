import tkinter

vPrincipal = tkinter = tkinter.Tk()

vPrincipal.title("A02 Dimensionando la ventana")

vPrincipal.wm_state('zoomed')

vPrincipal.update()

print("Ancho screen: ", vPrincipal.winfo_screenwidth())
print("Alto screen: ", vPrincipal.winfo_screenheight())
print("Ancho ventana:", vPrincipal.winfo_width())
print("Height ventana:", vPrincipal.winfo_height())
print("x          :", vPrincipal.winfo_x())
print("y          :", vPrincipal.winfo_y())
print(vPrincipal.geometry())

vPrincipal.mainloop()
