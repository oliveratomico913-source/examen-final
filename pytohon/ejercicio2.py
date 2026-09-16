try:
    vehiculo = input("Ingrese el tipo de vehículo (1: Auto, 2: Moto, 3: Camión): ")
    horas = float(input("Ingrese las horas de parqueo: "))
    if horas <= 0:
        print("Error: las horas deben ser mayores a 0")
    elif vehiculo not in ["1", "2", "3"]:
        print("Error: opción de vehículo no válida")
    else:
        if vehiculo == "1":
            tarifa = 10
            nombre = "Auto"
        elif vehiculo == "2":
            tarifa = 5
            nombre = "Moto"
        else:
            tarifa = 20
            nombre = "Camión"
        total = tarifa * horas
        if horas > 4:
            recargo = total * 0.15
            total_final = total + recargo
        else:
            recargo = 0
            total_final = total
        print("\n--- DETALLE DEL COBRO ---")
        print("Vehículo:", nombre)
        print("Horas:", horas)
        print("Tarifa por hora:", tarifa, "Bs")
        print("Subtotal:", total, "Bs")
        print("Recargo:", recargo, "Bs")
        print("Total a pagar:", total_final, "Bs")

except ValueError:
    print("Error: ingrese un dato válido")