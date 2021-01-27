# entrada = list(reversed(input("Digame algo: ")))


entrada = input("Digame algo: ")
# print(entrada)

if entrada == entrada[::-1]:
    print(entrada, "es capicua o palindroma")
else:
    print(entrada, "no es capicua o palindroma")
