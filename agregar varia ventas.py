subtotal_acumulado = 0
continuar = "s" # Empezamos asumiendo que sí hay productos

while continuar.lower() == "s":
    precio = float(input("Ingrese el precio del servicio/producto: S/ "))
    subtotal_acumulado += precio
    
    # Pregunta de control para romper el ciclo de forma humana
    continuar = input("¿Desea agregar otro producto? (s/n): ")

# --- Cálculos finales (Tu Misión) ---
igv = subtotal_acumulado * 0.18
total = subtotal_acumulado + igv

print("\n--- RESUMEN DE OPERACIÓN ---")
print("Subtotal Neto: S/", round(subtotal_acumulado, 2))
print("IGV (18%):     S/", round(igv, 2))
print("TOTAL A COBRAR: S/", round(total, 2))

input("\nPresiona Enter para cerrar la venta")
