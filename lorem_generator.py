i = 0
parrafo_generado = ""
numero_parrafo = int(input("Ingresa el numero de parrafo\n"))
parrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi aclacinia nibh, nec faucibus enim. Nullam quis lorem posuere, hendrerit tellus eget, tincidunt ipsum. Nam nulla tortor, elementum in elit nec,fermentum dignissim sapien. Sed a mattis nisi, sit amet dignissim elit. Sed finibus eros sit amet ipsum scelerisque interdum. Curabitur justo nibh, viverra a elit vel, elementum hendrerit erat. Duis feugiat mattis ante vel hendrerit. Etiam nec nibh nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\n"


while i < numero_parrafo:
    i += 1
    parrafo_generado += parrafo
    
print (parrafo_generado)