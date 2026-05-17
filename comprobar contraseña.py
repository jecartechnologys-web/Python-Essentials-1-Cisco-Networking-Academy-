clave = "peru2026"

#maximo 3 intentos 

#usar bucle for

#clave correcta == bienvenido

for i in range (1, 4):
    clave = input ("ingresa la clave:")

    if clave == "peru2026":
        print ("clave correcta")
        break #rompe el blucle 
        
    else:
        print ("clave incorrecta")

        if i == 3: # le digo al codigo cuando llegue a su 3er intento le diga cuenta bloqueada
            print ("cuenta bloqueada")
input("presiona")
