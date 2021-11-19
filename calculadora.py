numero = int(input("Escribe un numero: "))
operacion = int(input("""¿Qué deseas realizar?: 
[1] Conocer la tabla de multiplicar
[2] Conocer la potencia hasta 12 :"""))

if operacion == 1:
    for i in range(13):
        print(numero * i)
        
elif operacion == 2:
    for i in range(13):
        print(numero ** i)

else:
    print("Elige una opcion valida")