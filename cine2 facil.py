"""
El Cine "La Gran Pantalla"
Crea un programa para vender entradas de cine.
Entrada: Edad del cliente. Si la edad es 0, termina el programa.
Reglas:
Si es menor de 12 años: paga 10 soles.
Si tiene entre 12 y 60 años: paga 20 soles.
Si es mayor de 60 años: paga 15 soles.
Validación: No permitas edades negativas.
Final: Muestra el total de entradas vendidas y el dinero total recaudado.
"""
entradas_vendidas = 0 
total_recaudado = 0 
while True:
    edad = int(input("ingrese su edad para saber el precio de su entrada al cine:"))

    if edad == 0:
           break

    if edad < 0:
        print("error ingrese un numero positivo")
        continue
    
    if edad < 12:
            edad = 10
            print ("El precio de su entrada es:" , edad)
            total_recaudado +=  edad
            entradas_vendidas += 1

    elif edad >= 12 and edad <= 60:
            edad = 20
            print ("El precio de su entrada es:" , edad)
            total_recaudado = total_recaudado + edad
            entradas_vendidas += 1

    elif edad >= 61:
            edad = 15
            print ("El precio de su entrada es:" , edad)
            total_recaudado = total_recaudado + edad
            entradas_vendidas += 1
    
    if edad < 0:
            print("error ingrese un numero positivo")


print("total recaudado:" , total_recaudado)
print ("total entradas vendidas" , entradas_vendidas)