def devolverSegundos(dias, horas, minutos, segundos):
    tiempo_total = (86400 * dias) + (3600 * horas) + (60 * minutos) + segundos
    print(f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos son {tiempo_total} segundos")

print("Convertidor a segundos")
n_dias = int(input("Digame un numero de dias: "))
n_horas = int(input("Digame un numero de horas"))
n_minutos = int(input("Digame un numero de minutos"))
n_segundos = int(input("Digame un numero de segudos"))

devolverSegundos(n_dias, n_horas, n_minutos, n_segundos)
