import sys
import random

#El jugador debe elegir que jugar
jugador=input("Elija entre piedra, papel o tijera:\n")
computador = random.randint(1,3)

#Si se ingresa un valor invalido se cerrará el juego
if not(jugador in ["piedra","papel", "tijera"]):
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()

#Opciones de juego
if computador == 1:
    print("Computador juega piedra.")
elif computador == 2:
    print("Computador juega papel.")
else:
    computador == "tijera"
    print("Computador juega tijera.")
    
if (computador == 3 and jugador == "papel") or (computador == 1 and jugador == "tijera") or (computador == 2 and jugador == "piedra"):
    print("Perdiste.")
elif (computador == 3 and jugador == "piedra") or (computador == 1 and jugador == "papel") or (computador == 2 and jugador == "tijera"):
    print("Ganaste.")
else:
    print("Empataste.")