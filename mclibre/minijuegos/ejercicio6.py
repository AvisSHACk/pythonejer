import random

print("EL DADO MAS ALTO")

n_dados = int(input("Numero de dados: "));
jugador1, jugador2 = 0, 0
if(n_dados <= 0):
    print("Imposible")
else:
    print("Jugador 1: ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        jugador1 += valor_dado
        print(valor_dado, end=" ")
    print()
    print("Jugador 2: ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        jugador2 += valor_dado
        print(valor_dado, end=" ")

    print()
    if jugador1 > jugador2 : print("Ha ganado el jugador 1")
    elif jugador2 > jugador1: print("Ha ganado el jugador 2")
    else: print("Han empatado")



