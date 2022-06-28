cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

i = 0
while cuenta_regresiva > i:
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
    i += 1