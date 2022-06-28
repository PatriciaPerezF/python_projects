saldo = 0
cantidad = 0
division = "-·" * 30

def depositar (saldo , cantidad):
    cantidad = int(input("¿Que cantidad desea depositar?\n"))
    saldo += cantidad
    print("Su nuevo saldo es de $ {}\n".format(saldo))
    mostrar_menu(saldo)
    return saldo

    
def girar(saldo, cantidad):
    if saldo > 0:
        cantidad = int(input("¿Que cantidad desea retirar?\n"))
        if saldo > cantidad:
            saldo -= cantidad
            print("Su saldo actual es de $ {}\n".format(saldo))
            mostrar_menu(saldo)
        else:
            print("No se puede girar esta cantidad. Su saldo es de $ {}\n".format(saldo))
            mostrar_menu(saldo)
    else:
        print("No pueden realizar giros. Su saldo es $ 0\n")
        mostrar_menu(saldo)
    return saldo
     
        
def mostrar_menu(saldo):
    print(division)
    opcion = int(input("""¡Bienvenido al portal del Banco Amigo!. Escoja una opcion:
     
      1. Consultar saldo
      2. Hacer depósito
      3. Realizar giro
      4. Salir\n""" ))
    print(division)

    while not(opcion in [1,2,3,4]):
        opcion = int(input ("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.\n"))

    if opcion == 1:
        print("Su saldo es de $ {}\n".format(saldo))
        mostrar_menu(saldo)
    elif opcion == 2:
        print("Su saldo es de $ {}\n".format(saldo))
        depositar(saldo,cantidad)
    elif opcion == 3:
        print("Su saldo es de $ {}\n".format(saldo))
        girar(saldo,cantidad)
    else:
        print("¡Gracias por visitar nuestra sucursal!")

saldo = mostrar_menu(0)