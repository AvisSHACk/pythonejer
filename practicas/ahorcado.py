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

guiones = [] 

def mostrar_ahorcado(intentos, palabra_user, letra_user):
    for i in range(len(palabra_user)):
        if letra_user == palabra_user[i]:
            guiones[i] = letra_user
    print(guiones)
    print(IMÁGENES_AHORCADO[intentos])

def verificar_letra(intento, palabra_user):
    letra_user = input("Ingresa una letra: ")
    mostrar_ahorcado(intento, palabra_user, letra_user)


palabra_user = input("Ingrese una palabra: ")
for i in range(len(palabra_user)):
    if i <= len(palabra_user):
        guiones.append("_")

for i in range(len(palabra_user)):
    verificar_letra(i, palabra_user)
