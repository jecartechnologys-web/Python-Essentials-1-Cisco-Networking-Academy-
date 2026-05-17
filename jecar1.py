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

laptop = 0
impresora = 0
otro_equipo = 0
precio = 0
total_equipos = 0

tipo_equipo = int (input ("presiona 1 para laptops o 2 para impresoras:"))

while tipo
    
    if tipo_equipo == 1:
        laptop = float (input("precio de la reparación de la laptop:"))
    
    elif tipo_equipo == 2:
        impresora = float (input("precio de la reparación de la impresora:"))
        
    else
        print("No es un numero valido," , tipo_equipo)
                
                   
