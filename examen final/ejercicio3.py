frase = input("Escribe una frase: ")
if "triste" in frase.lower():
    nueva_frase = frase.replace("triste", "feliz")
    print("Texto cambiado: ")
    print(nueva_frase)
else:
    print(frase.upper())