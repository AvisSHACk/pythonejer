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

def verificar_letra(palabra_user):
    global guiones
    global intento
    
    acerto = False
    intento += 1
    letra_user = input("Ingresa una letra: ")
    
    if(letra_user in guiones):
        return  "La letra ingresa ya ha sido adivinada" + "\n" + guiones 
    else:
        for i in range(len(palabra_user)):
            if(letra_user == palabra_user[i]):
                guiones = guiones.split(" ")
                guiones[i] = letra_user
                guiones = ' '.join(guiones)
                acerto = True
    
    print(intento)
    if acerto :
        intento-=1

    print("Intento: ", intento )
    print(guiones)



palabra_user = input("Ingrese una palabra: ")
for i in range(len(palabra_user)):
    if i <= len(palabra_user):
        guiones += "_ "

intento = 0
while intento < 6:
    palabra = guiones
    palabra = palabra.split(" ")
    palabra = "".join(palabra)

    if(palabra == palabra_user):
        print(f"Felicidades, la palabra secreta es {palabra}, has adivinado")
        break
    verificar_letra(palabra_user)
    print(IMÁGENES_AHORCADO[intento])
else:
    print("Se te acabaron los intentos, una lastima")

   
