import string
i = 1
j = 0

clave = input("Ingresa una clave\n").lower()
abc = string.ascii_lowercase
intentos = 0

for i in clave:
    if not(i in abc):
        print("La clave solo debe contener letras.")
        quit()
    
for i in clave:
    for j in abc:
        intentos += 1
        if i == j :
            break
print("Se requieren {} intentos".format(intentos))