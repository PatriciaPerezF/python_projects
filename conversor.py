def cambiar(moneda_recibida):
    moneda_recibida = float(moneda_recibida)
    if cambio == 1 :
        moneda_entregada = moneda_recibida / valor_dolar
        moneda_entregada = round(moneda_entregada,2)
        moneda_entregada = str(moneda_entregada)
        return moneda_entregada
    else:
        moneda_entregada = moneda_recibida * valor_dolar
        moneda_entregada = round(moneda_entregada,2)
        moneda_entregada = str(moneda_entregada)
    return moneda_entregada
print("Bienvenido a la casa de cambio")
cambio = int(input("""Elige el cambio que deseas realizar
[1] Cambio CLP a $ 
[2] Cambio $ a CLP: """))
valor_dolar = 870
if cambio == 1 :
    clp_usd = input("¿Cuantos Pesos Chilenos quieres cambiar?: ")
    resultado = cambiar(clp_usd)
    print ("Tus " + clp_usd + " CLP equivalen a " + resultado + " Dólares")
elif cambio == 2 :
    usd_clp = input("¿Cuantos Dólares quieres cambiar?: ")
    resultado = cambiar(usd_clp)
    print ("Tus " + usd_clp + " Dólares equivalen a " + resultado + " CLP")
else : 
    print("***** No has ingresado una opción valida *****")
