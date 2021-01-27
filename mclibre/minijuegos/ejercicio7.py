import random
print("EL DADO MAS ALTO")

n_dados = int(input("Numero de dados: "));
jugador1, jugador2 = 0, 0
if(n_dados <= 0):
    print("Imposible")
else:
    print("Dados ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        if(valor_dado % 2 == 0): jugador1 += 1 
        else: jugador2 += 1
        print(valor_dado, end=" ")

    print()
    if jugador1 > jugador2: print("El jugador 1 ha ganado")
    elif jugador2 > jugador1: print("El jugador 2 ha ganado")
    else: print("Han empatado")
