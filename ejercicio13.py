print("="*5, "Programa que detecta palabras palindromas", "="*5)
cadena1 = input("Ingresa una cadena de texto: ")
cadena_al_reves = cadena1[::-1]

if(cadena1 == cadena_al_reves):
    print("La cadena ingresa es palindromo")
else:
    print("La cadena ingresa no es palindromo")
