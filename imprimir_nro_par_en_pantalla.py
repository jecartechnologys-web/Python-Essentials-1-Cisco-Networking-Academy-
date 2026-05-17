n = int(input("Dime un número: "))

# 1. Agregamos ':' y usamos n + 1 para llegar al número final
for n in range(1, n + 1): 
    # 2. Todo esto está DENTRO del for (4 espacios)
    if n % 2 == 0:
        # 3. Esto está DENTRO del if (8 espacios)
        print("El número", n, "es par")
    else:
        print("El número", n, "NO es par")

input("Presione una tecla para continuar")
