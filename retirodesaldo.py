saldo = 1000

retiro = int(input("¿Cuánto dinero deseas retirar?: "))

if retiro <= saldo:
    saldo = saldo - retiro
    print("Retiro exitoso. Tu nuevo saldo es:", saldo)

else :
    print ("Error: Fondos insuficientes. Solo tienes", saldo)


input ("presiona")
