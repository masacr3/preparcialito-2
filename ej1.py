class polinomio:
    def __init__(self,coeficientes):
        """Constructor polinomio
           [coeficientes = lista] de numeros
           coeficientes = [a^n,b^n-1,..., c]
           pre: se asume que [coeficietes] contiene aunque sea 1 elemento

        """
        self.coeficientes = coeficientes

    def __eq__(self,otro):
        pass

    def __str__(self):
        str_polinomio = ""
        exponente = len(self.coeficientes)

        for coeficiente in self.coeficientes:
            exponente -= 1
            if exponente == 0:
                str_polinomio += str(coeficiente)
                continue

            if not (coeficiente == 0) :
                str_polinomio += "{}x^{} + ".format(coeficiente,exponente)
        return str(str_polinomio)

    def __eq__(self,otro):
        if not (len(self.coeficientes) == len(otro.coeficientes)):
            return False

        for coeficiente in self.coeficientes:
            if coeficiente not in otro.coeficientes:
                return False
        return True

    def derivar(self):
        exponente = len(self.coeficientes)

        if exponente == 0:
            return polinomio([0])

        derivado = []
        for coeficiente in self.coeficientes:
            exponente -= 1

            if exponente == 0:
                continue

            derivado.append (coeficiente * exponente)

        return polinomio(derivado)
