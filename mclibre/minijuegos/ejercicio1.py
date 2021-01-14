import random

print("TIRADA DE DADOS")

n_dados = int(input("Ingresa el numero de dados: "));

if(n_dados <= 0):
    print("Imposible")
else:
    print("Dados: ", end="")
    for i in range(n_dados):
        print(random.randint(1, 6), end=" ")
