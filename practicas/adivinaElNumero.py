import random
print("¿Podras adivinar el numero?, El programa te dara una ayudita sin embargo solo tendras 6 intentos")
usuario = int(input("Ingresa un numero al azar entre 1 al 20: "))

'''
Al pedir el numero por primera vez ya se gasto un intento, por lo tanto la variable debe empezar en 5 pues
el usuario solo tiene 6 intentos
'''
intentosUsuario = 5
''''''

numeroRandom = random.randint(1, 20)
while intentosUsuario > 0:
    intentosUsuario -= 1
    if usuario < numeroRandom:
        print("="*5,"El numero es mayor", "="*5)
    elif usuario > numeroRandom:
        print("="*5, "El numero es menor", "="*5)
    else:
        print("="*5,"Has ganado", "="*5)
        break
    
    usuario = int(input("Vuelve a ingresa un numero entre 1 y 20: "))

if intentosUsuario == 0:
    print("Que pena, el numero era", numeroRandom, " sin embargo no has logrado adivinar el numero")
