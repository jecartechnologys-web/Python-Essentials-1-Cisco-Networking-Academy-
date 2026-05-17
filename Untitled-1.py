"""
JECAR recibe equipos para reparar.
El programa pregunta el tipo de equipo 
y el precio de la reparación.
Si el precio es 0 termina.

Las reglas son:
- Laptop: si supera 200 soles aplica 15% descuento
- Impresora: si supera 100 soles aplica 10% descuento
- Otro equipo: sin descuento

Al final muestra:
- Total de equipos atendidos
- Total recaudado con descuentos aplicados
"""

total_equipos = 0
total_recaudado = 0
precio = -1

while precio != 0:

    print("Registro de equipos")
    print("1. Laptops")
    print("2. Impresora")
    print("3. Otro equipo")

    while True:
        opcion = int(input("Elige las siguientes opciones:"))
        if opcion == 1 or opcion == 2 or opcion == 3:
            break
        else:
            print("numero invalido")        

    precio = float(input("agrega el precio de la reparacion 0 para terminar:"))


    if opcion == 1:
        if precio >= 200:
            print("si aplica el descuento de 15%")
            precio = precio - (precio * 0.15)
    elif opcion == 2: 
        if precio >= 100:
            print("si aplica el descuento de 10%")
            precio = precio - (precio * 0.10)
    
    elif opcion == 3:
        print("gracias por su compra")

    if precio !=0:
        total_equipos = total_equipos +1
        total_recaudado = total_recaudado + precio

print("El total recaudado es:" , total_recaudado)
print ("El total de los servicios es:" , total_equipos)