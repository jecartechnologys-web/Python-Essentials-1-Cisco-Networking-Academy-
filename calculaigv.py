# 1. Pedimos el precio base (Neto)
precio_base = float(input("Ingresa el precio base del producto: S/ "))

# 2. Calculamos el impuesto (18%)
igv = precio_base * 0.18

# 3. Calculamos el total (Suma de ambos)
total = precio_base + igv

# 4. Imprimimos el reporte redondeado a 2 decimales
print("--- RESUMEN DE COBRO ---")
print("Precio base:     S/", round(precio_base, 2))
print("IGV (18%):       S/", round(igv, 2))
print("Total a pagar:   S/", round(total, 2))

input("Presiona Enter para salir")
