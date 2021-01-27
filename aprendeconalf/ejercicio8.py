def mcd(num1, num2):
    while True:
        if num2 == 0 :
            break
        else:
            resto = num1 % num2
            num1 = num2
            num2 = resto

    return num1

def mcm(num1, num2, mcd):
    return num1 * num2 // mcd

print(mcd(150, 39))
print(mcm(150, 39, mcd(150, 39)))
print(mcd(6, 9))
print(mcd(56, 104))
