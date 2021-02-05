from tkinter import *

raiz = Tk();
raiz.title("Datos Personales")

def holamundo():
    print(inputNombre.get())
    print(inputApellidos.get())
    print(inputTelefono.get())
    print(inputDireccion.get())

frame = Frame(raiz, width=500, height=600)
frame.pack()

'''Nombre'''
nombre = Label(frame, text="Nombre: ")
inputNombre = Entry(frame) 
nombre.grid(row=0, column=0)
inputNombre.grid(row=0, column=1)

'''Apellidos'''
apellidos = Label(frame, text="Apellidos: ")
inputApellidos = Entry(frame) 
apellidos.grid(row=1, column=0)
inputApellidos.grid(row=1, column=1)

'''direccion'''
direccion = Label(frame, text="Direccion: ")
inputDireccion = Entry(frame) 
direccion.grid(row=0, column=2)
inputDireccion.grid(row=0, column=3)

'''Telefono'''
telefono = Label(frame, text="Telefono: ")
inputTelefono = Entry(frame) 
telefono.grid(row=1, column=2)
inputTelefono.grid(row=1, column=3)

buttonEnviar = Button(raiz, text="Enviar datos", command=holamundo)
buttonEnviar.pack()

raiz.mainloop()
