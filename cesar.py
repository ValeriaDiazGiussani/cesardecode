def descifrar_cesar(texto_cifrado, desplazamiento):
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra.isalpha():  # Verifica si es una letra del alfabeto
            mayuscula = letra.isupper()  # Verifica si es mayúscula
            letra = letra.upper()  # Convierte a mayúscula para el descifrado
            codigo_ascii = ord(letra)
            codigo_descifrado = ((codigo_ascii - 65 - desplazamiento) % 26) + 65
            letra_descifrada = chr(codigo_descifrado)
            if not mayuscula:
                letra_descifrada = letra_descifrada.lower()  # Conserva la minúscula si lo era
            texto_descifrado += letra_descifrada
        else:
            texto_descifrado += letra  # Conserva caracteres que no son letras
    return texto_descifrado

# Mensaje cifrado y clave de desplazamiento
mensaje_cifrado = "PTYCJIWGPQRABKF"

for desplazamiento in range(0, 51):
    mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
    print(f"Desplazamiento {desplazamiento}: {mensaje_descifrado}")

for desplazamiento in range(-51, 0):
    mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
    print(f"Desplazamiento {desplazamiento}: {mensaje_descifrado}")
