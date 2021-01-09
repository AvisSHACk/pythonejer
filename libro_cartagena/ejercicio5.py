def suma(lista):
    suma = 0

    for i in lista:
        suma += i
    return suma

def multi(lista):
    multi = 1
    for i in lista:
        multi *= i
    return multi

print(suma([1, 2, 3, 4]))
print(multi([1, 2, 3, 4]))
