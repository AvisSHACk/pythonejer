import random

print("TIRADA DE DADOS")

n_jugadores = int(input("Numero de jugadores: "));
valor_conseguir = int(input("Valor a conseguir: "))

if(n_jugadores <= 0):
    print("Imposible")
else:
    for i in range(n_jugadores):
        valor_dado = random.randint(1, 6)
        if(valor_dado == valor_conseguir):
            print(f"Jugador {i + 1}: {valor_dado} Conseguido")
        else:
            print(f"Jugador {i + 1}: {valor_dado}")
