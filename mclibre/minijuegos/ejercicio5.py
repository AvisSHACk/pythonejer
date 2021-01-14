import random

print("EL DADO MAS ALTO")

n_dados = int(input("Numero de dados: "));
dado = 0

if(n_dados <= 0):
    print("Imposible")
else:
    print("Dados: ", end="")
    masAlto = 0
    for i in range(n_dados):
        valor_dado = random.randint(1, 6)
        print(valor_dado, end=" ")

        if masAlto < valor_dado: masAlto = valor_dado

    print()
    print(f"El dado mas alto es {masAlto}")
