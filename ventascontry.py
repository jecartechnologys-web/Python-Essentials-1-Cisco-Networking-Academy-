subtotal_acumulado = 0
agregar = "s"

cliente = input("Nombre del cliente: ")

while agregar.lower() == "s":
    # --- BLOQUE DE SEGURIDAD ---
    try:
        precio_input = input("Ingresa el precio = S/")
        precio = float(precio_input)
        
        # Si el número es válido, sumamos y preguntamos si sigue
        subtotal_acumulado += precio
        agregar = input("¿Desea agregar otro producto o servicio? s/n = ")
        
    except ValueError:
        # Aquí es donde capturamos el error de "letras"
        print("⚠️ NOTIFICACIÓN: ¡Dato inválido! Por favor, usa números (ej: 25.90)")
        # No cambiamos 'agregar', así que el bucle vuelve a pedir el precio
        continue 

# --- Cálculos finales ---
igv = subtotal_acumulado * 0.18
total = subtotal_acumulado + igv

print("\n" + "="*25)
print("CLIENTE:", cliente.upper())
print("Subtotal Neto: S/", round(subtotal_acumulado, 2))
print("IGV (18%):     S/", round(igv, 2))
print("TOTAL A PAGAR: S/", round(total, 2))
print("="*25)

input("Venta finalizada. Presiona Enter.")
