def procedimiento(list):
    for i in list:
        for j in range(i):
            print('*', end="")
        print()

print("Los valores ingresados son 4, 9, 7, por lo tanto:")
procedimiento([4, 9, 7])
