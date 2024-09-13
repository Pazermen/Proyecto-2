# Programa para verificar la longitud de una frase

# Solicitar la entrada del usuario
frase = input("Ingresa una frase: ")

# Obtener la longitud de la frase sin contar espacios
longitud = len(frase.replace(" ", ""))

# Verificar la longitud de la frase
if 4 <= longitud <= 8:
    print(f"La frase es correcta. Tiene {longitud} letras.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")
