n = int(input("Ingresa un numero\n"))
i = 1
suma = ""
resultado = 0

while i < n:
    i += 1
    if i % 2 == 0:
        suma += str(i) + " + "
        resultado += i
print(suma[:len(suma)-2])
print("La suma de los numeros pares es {}".format(resultado))