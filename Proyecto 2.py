def identificar_cuadrante(x, y):
    # Verificar que ninguna coordenada sea 0
    if x == 0 or y == 0:
        print("Las coordenadas no pueden ser cero.")
    else:
        # Determinar el cuadrante
        if x > 0 and y > 0:
            print("El punto se encuentra en el cuadrante I")
        elif x < 0 and y > 0:
            print("El punto se encuentra en el cuadrante II")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el cuadrante III")
        elif x > 0 and y < 0:
            print("El punto se encuentra en el cuadrante IV")

# Ejemplo de uso
try:
    x = float(input("Ingrese X: "))
    y = float(input("Ingrese Y: "))
    identificar_cuadrante(x, y)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
