print("PARES E IMPARES")

num1 = int(input("Escriba un numero entero: "))
num2 = int(input(f"Escriba un numero entero mayor o igual que {num1}: "))

if(num1 > num2):
    print(f"¡Le he pedido un numero entero mayor o igual que {num1}!")
else:
    for i in range(num1, num2 + 1):
        if(i % 2 == 0):
            print(f"El numero {i} es par")
        else:
            print(f"El numero {i} es impar")
