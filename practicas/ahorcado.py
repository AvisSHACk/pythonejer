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

#verifica si la letra ingresa pertenece a la palabra secreta
def verificar_letra(palabra_user):
    global guiones
    global intento
    
    acerto = False
    intento += 1
    letra_user = input("Ingresa una letra: ")
   
   #verifica si la letra ya ha sido adivinada
    if(letra_user in guiones):
        acerto = True
        return  "La letra ingresa ya ha sido adivinada" + "\n" + guiones 
    else:
        #agrega a la cadena de guiones la letra adivinada
        for i in range(len(palabra_user)):
            #agrega a la cadena de guiones la letra adivinada
            if(letra_user == palabra_user[i]):
                guiones = guiones.split(" ")
                guiones[i] = letra_user
                guiones = ' '.join(guiones)
                acerto = True
    
    #si ha acertado una letra el programa lo sabra y mantendra la variable intento en su mismo valor -1
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
    
    #si la palabra ha sido acertada entonces entrara a este if y rompera el blucle
    if(palabra == palabra_user):
        print(f"Felicidades, la palabra secreta es {palabra}, has adivinado")
        break
    verificar_letra(palabra_user)
    print(IMÁGENES_AHORCADO[intento])
else:
    print("Se te acabaron los intentos, una lastima")

   
