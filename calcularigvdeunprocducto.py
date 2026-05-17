#Vamos a calcular el IGV (18%) de una venta.


precio = 0



#Tu misión:

#Pide al usuario el precio de un producto.

#Calcula el impuesto: igv = precio * 0.18.

#Calcula el total: total = precio + igv.


#Imprime un pequeño reporte:

#"Precio base: [precio]"

#"IGV (18%): [igv]"

#"Total a pagar: [total]"

precio = float (input( "El precio del producto es ="))

igv = precio * 0.18
total = precio 

print ("Precio base:", round (precio - igv, 2) )
print ("el impuesto a pagar es del (18%):", round(igv, 2) )
print ("Total a pagar:", round(total, 2))

input ("presiona para salir")






