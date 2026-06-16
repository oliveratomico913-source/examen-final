while True:
    usuario = input("Ingrese nombre de usuario: ").strip()

    if usuario.lower() == "fin":
        break

    print("Usuario ingresado:", usuario)