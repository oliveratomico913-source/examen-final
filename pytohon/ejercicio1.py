while True:
    try:
        n=int(input("ingrese la cantidad de terminos: "))
        if n <=0:
            print("error volver a pedir el dato hasta q sea valido")
        else:
            a=0
            b=1
            print("susecion")
            for i in range(n):
                print(a, end=" ")
                siguiente =a + b
                a = b
                b = siguiente
                break
    except ValueError:
        print("error ingrese un numero enterno")
        



