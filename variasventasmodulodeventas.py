--#Crea un programa que:

#Use un bucle while.

#Te pida el precio de un producto.

#Lo vaya sumando a una variable subtotal_acumulado.

#Si el usuario escribe 0, el bucle se rompe (break).

#Al final, calcula el IGV y el Total de toda la suma.


#contador = 1
#while contador <= 5:                 Condición
  #  print(f"Número: {contador}")
  #  contador += 1                    Actualización (evita bucle infinito)


subtotal_acumulado = 0
agregar = "s"

cliente = input("Nombre del cliente: ")

while agregar.lower() == "s":
##    precio = float ( input ( "Ingresa el precio = S/"))
    try:
        
        precio = float (input("Ingresa el precio del producto: S/ "))
        subtotal_acumulado += precio
        agregar = input ( "¿Desea agregar otro producto o servicio? s/n =")
        
    except ValueError:
        # Si float() falla porque el usuario puso letras, venimos aquí
        print("❌ ERROR: Formato inválido. Ingresa números (ej: 10.50).")
        # El ciclo while continuará porque 'agregar' sigue siendo "s"

igv = subtotal_acumulado *0.18
total = subtotal_acumulado + igv


print("cliente", cliente.upper())
print("Subtotal Neto: S/", round(subtotal_acumulado, 2))
print("IGV (18%):     S/", round(igv, 2))
print("TOTAL A PAGAR: S/", round(total, 2))

input("Venta finalizada. Presiona Enter.")


