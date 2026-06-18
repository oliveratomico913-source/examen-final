comentario = input("Escribe el comentario de un producto: ")
comentario = comentario.lower()
if "malo" in comentario:
    print("Tu comentario no cumple con las normas, intenta de nuevo. ")
else:
    print("Comentario publicado con éxito. ")