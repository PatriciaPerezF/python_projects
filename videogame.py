import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("""¡Adivina el numero!
    Elige un numero entre el 1 y 100: """))
    while numero_aleatorio !=  numero_elegido:
        while numero_aleatorio < numero_elegido:
            print ("Es un número más pequeño")
            numero_elegido = int(input("Elige otro numero: "))
        while numero_aleatorio > numero_elegido:
            print ("Es un número más grande")
            numero_elegido = int(input("Elige otro numero: "))
    print("¡Ganaste!")
        
if __name__ == "__main__":
    run()
