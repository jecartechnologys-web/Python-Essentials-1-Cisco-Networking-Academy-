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
edad = -1
while edad != 0:
    print("***La Gran Pantalla***")
    print("1. Entradas para edades hasta 11 años, precio: 10 soles")
    print("2. Entradas para edades de 12 años hasta 60 años, precio: 20 soles")
    print("3. entradas para edades de 61 años en adelante, precio: 15 soles")
    
    while True:
        opcion = int(input("Elige rango de edad 1, 2, 3 y 0 para sair:"))
        edad = int(input("ingrese su edad para saber el precio de su entrada al cine "))
        
        if opcion == 1 or opcion == 2 or opcion ==3:
            break
        else:
            print("Edad incorrecta")

    if opcion <= 1 and opcion <= 11:
        edad = 10
        print ("El precio de su entrada es:" , edad)
        edad += 1
        total_recaudado = total_recaudado + edad

    elif opcion <=12 and opcion <= 60:
        edad = 20
        print ("El precio de su entrada es:" , edad)
        edad += 1
        total_recaudado = total_recaudado + edad

    elif opcion >= 61:
        edad = 15
        print ("El precio de su entrada es:" , edad)
        edad += 1
        total_recaudado = total_recaudado + edad

print ("final" , )