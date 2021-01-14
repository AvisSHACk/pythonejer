import random

print("TIRADA DE DADOS")

n_dados = int(input("Numero de jugadores: "));
valor_conseguir = int(input("Valor a conseguir: "))

if(n_dados <= 0):
    print("Imposible")
else:
    gana = False
    print("Dados: ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        print(valor_dado, end=" ")

        if valor_conseguir == valor_dado:
            gana = True

    if gana:
        print("\nEl jugador ha ganado")
    else:
        print("\nEl jugador haperdido")
