n_numeros = int(input("Digame cuantos numeros va a escribir: "))

hayPar = False

for i in range(n_numeros):
   numero = int(input(f"Digame el numero {i + 1}")) 
   if numero % 2 == 0:
       hayPar = True

if hayPar:
    print("Has escrito algun numero par")
else:
    print("No has ingresado numero pares")
