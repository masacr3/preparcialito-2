class PERSONA:
    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return str(self.nombre)


class COLECTIVO:
    def __init__(self):
        self.pasajeros = {}

    def subir(self,destino,pasajero):
        if destino not in self.pasajeros:
            self.pasajeros[destino] = []

        self.pasajeros[destino].append(pasajero)

    def bajar(self,destino):
        if destino not in self.pasajeros:
            return []

        return self.pasajeros[destino].pop(destino)

    def __str__(self):
        return str(self.pasajeros)
