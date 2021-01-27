import random
print("EL DADO MAS ALTO")

n_dados = int(input("Numero de dados: "));
ha_perdido = False
dado_anterior = 0
if(n_dados <= 0):
    print("Imposible")
else:
    print("Dados ", end="")
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        if(valor_dado != dado_anterior):
            dado_anterior = valor_dado
        else:
            ha_perdido = True
        print(valor_dado, end=" ")
    print(ha_perdido)
    print(dado_anterior)

    print()
    if ha_perdido: print("El jugador ha perdido")
    else : print("El jugador ha ganado")
