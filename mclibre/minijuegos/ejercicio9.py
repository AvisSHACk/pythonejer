import random

print("EL DADO MAS ALTO")

n_dados = int(input("Numero de dados: "));
jugador1, jugador2 = 0, 0
if(n_dados <= 0):
    print("Imposible")
else:
    bajo, alto = 7, 0
    print("Jugador 1: ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        if valor_dado < bajo:
            bajo = valor_dado 

        if valor_dado > alto:
            alto = valor_dado

        print(valor_dado, end=" ")

    jugador1 = bajo + alto
    print()
    bajo, alto = 7, 0
    print("Jugador 2: ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        if valor_dado < bajo:
            bajo = valor_dado 

        if valor_dado > alto:
            alto = valor_dado

        print(valor_dado, end=" ")

    jugador2 = bajo + alto
    print()

    if jugador1 > jugador2 : print("Ha ganado el jugador 1")
    elif jugador2 > jugador1: print("Ha ganado el jugador 2")
    else: print("Han empatado")
