print("Digito de control cuenta corriente")

entidad1 = int(input("Escriba el primer digito de la entidad:")) * 4
entidad2 = int(input("Escriba el Segundo digito de la entidad: ")) * 8
entidad3 = int(input("Escriba el tercer digito de la entidad: ")) * 5
entidad4 = int(input("Escriba el cuarto digito de la entidad")) * 10

entidadSuma = entidad1 + entidad2 + entidad3 + entidad4

print()

oficina1 = int(input("Escriba el primer digito de la oficina")) * 9
oficina2 = int(input("Escriba el segundo digito de la oficina")) * 7
oficina3 = int(input("Escriba el tercer digito de la oficina")) * 3
oficina4 = int(input("Escriba el cuarto digito de la oficina")) * 6

entidadOficina = oficina1 + oficina2 + oficina3 + oficina4

sumatoria = entidadSuma + entidadOficina

print()
print("El digito de control es:", 11 - (sumatoria % 11))
