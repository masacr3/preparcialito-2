def verifica_vendedores(archivo,error):
    """
    archivo = error = son rutas de archivo = str
    pre: se asume que [archivo] contiene un <header>
    post: retorna un diccionario de los venderdores como clave y los montos como valor
    """

    with open(archivo) as a_archivo, open(error,"a") as a_error:
        #saltamos el header
        a_archivo.readline().rstrip("\n")
        vendedores = {}
        try:
            for linea in a_archivo:
                anio,mes,vendedor,cliente,monto = linea.readline().rstrip("\n").split(",")

                if vendededor not in vendedores:
                    vendedores[vendededor] = 0

                vendedores[vendedor] += int(monto)

        except ValueError:
            a_error.write("{} -> {} \n".format("linea invalida",linea))

    return vendedores
