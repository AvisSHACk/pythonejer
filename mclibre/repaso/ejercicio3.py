print("Comprador de numeros")

numeros = []

for i in range(3):
    num = int(input("Escriba un numero: "))
    numeros.append(num)

bajo = max(numeros)
alto = min(numeros)
medio = (numeros[0] + numeros[1] + numeros[2]) - bajo - alto

print(alto, "es el mas grande")
print(bajo, "es el ams bajo")
print(medio, "es el medio")
