IMÁGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

guiones = ""
import threading

def mostrar_ahorcado():
    for i in range(7):
        print(IMÁGENES_AHORCADO[i])

def verificar_letra(intento, palabra_user):
    global guiones
    letra_user = input("Ingresa una letra: ")
    
    if(letra_user in guiones):
        return  "La letra ingresa ya ha sido adivinada" + "\n" + guiones 
    else:
        for i in range(len(palabra_user)):
            if(letra_user == palabra_user[i]):
                guiones = guiones.split(" ")
                guiones[i] = letra_user
                guiones = ' '.join(guiones)

        return guiones


palabra_user = input("Ingrese una palabra: ")
for i in range(len(palabra_user)):
    if i <= len(palabra_user):
        guiones += "_ "

for i in range(len(palabra_user)):
    print(verificar_letra(i, palabra_user))
