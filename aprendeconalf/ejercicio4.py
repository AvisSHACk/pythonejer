def facturar(monto, iva=21):
    impuesto = monto * (iva / 100)
    monto = monto + impuesto
    return monto

monto = 60

print("Monto: ", monto)
print("Monto con iva", facturar(monto))
