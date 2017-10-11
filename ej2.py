def main():
    """Abre un archivo csv y vuelva el contenido swapeado de las columnas
        en un archivo de salida.csv
        pre: se asume q las columas estan en el rango de las filas
        y que col1,col2 son numeros enteros 
    """
    col1 = int(input("columna 1:"))
    col2 = int(input("columna 2:"))

    with open("archivo.csv") as archivo:
    	with open("salida.csv", "w") as salida:
    		linea = archivo.readline().strip().split(",")
    		linea[col1], linea[col2] = linea[col2], linea[col1]
    		salida.write(",".join(linea))
