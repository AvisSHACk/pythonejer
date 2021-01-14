n_dvd = int(input("Cuantos DVD'S desea comprar: "))
poster = False;
monto = 0
descuento = 0

for i in range(n_dvd):
    marca = int(input("Marca de DVD: \n1:Salsa\n2:Rock\n3:Popn\n4:folclore\n"))

    if(marca == 1):
        monto += 56
    elif marca == 2:
        poster = True
        monto += 63
    elif marca == 3:
        poster = True
        monto += 87
    elif marca == 4:
        monto += 120
    else:
        print("Ingresa una marca validad")
        break;

if n_dvd == 4:
    descuento = monto * 0.06
elif n_dvd >= 5 and n_dvd <= 10:
    descuento = monto * 0.08
else:
    descuento = monto * 10.2

print("Importa de la compra: ", monto)
print("Descuento: ", descuento)
print("Importe total a pagar: ", monto - descuento)

if poster:
    print("==0=00Recibes in poster=======")
