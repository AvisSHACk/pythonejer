print("DIVISORES")
num = int(input("Escriba un numero mayor que cero: "))

if num < 0:
    print("Le he pedido un numero entero mayor que cer!")
else:
    print("Los divisores de 200 son", end=" ")
    for i in range(1, num // 2 + 1):
        if(num % i == 0):
            print(i, end=" ")
    else:
        print(num)
