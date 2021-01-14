import random

print("TIRADA DE DADOS")

n_jugadores = int(input("Numero de jugadores: "));
dado = 0

if(n_jugadores <= 0):
    print("Imposible")
else:
    for i in range(n_jugadores):
        print(f"Jugador {i + 1}: ", random.randint(1, 6))


