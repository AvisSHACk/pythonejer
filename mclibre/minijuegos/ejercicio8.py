import random
print("EL DADO MAS BAJO")

n_jugadores = int(input("Numero de jugadores: "));
ganador = 0
dado_ganador = 7
if(n_jugadores <= 0):
    print("Imposible")
else:
    for i in range(n_jugadores):
        valor_dado = random.randint(1, 6)

        if(valor_dado < dado_ganador):  
            ganador = i + 1
            dado_ganador = valor_dado

        print(f"Jugador {i+1}: ", valor_dado)

    print()
    print(f"El ganador es el jugador {ganador}")
