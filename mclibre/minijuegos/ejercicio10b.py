import random


def main():
    print("DADOS IGUALES")
    numero = int(input("Número de dados: "))
    if numero < 2:
        print("¡Imposible!")
    else:
        print("Dados: ", end="")
        repetido = False
        anterior = random.randrange(1, 7)
        print(f"{anterior} ", end="")
        for _ in range(1, numero):
            dado = random.randrange(1, 7)
            print(f"{dado} ", end="")
            if dado == anterior:
                repetido = True
            anterior = dado
        print()
        if repetido:
            print(f"El jugador ha perdido.")
        else:
            print(f"El jugador ha ganado.")


if __name__ == "__main__":
    main()
