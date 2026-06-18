while True:
    contraseña=input("Ingresar contraseña: ").lower()
    contraseña=contraseña.strip()
    if "12345" in contraseña:
        print("contraseña insegura, ingrese otra:")
    else:
        print("Acseso permitido")
        break