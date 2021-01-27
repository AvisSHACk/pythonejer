def cuadrados(lista):
    newList = []
    for i in lista:
        newList.append(i ** 2)

    return newList

lista = [2, 4, 6, 8]
print("La lista ingresa es:", lista)
print(cuadrados([2, 4, 6, 8]))

