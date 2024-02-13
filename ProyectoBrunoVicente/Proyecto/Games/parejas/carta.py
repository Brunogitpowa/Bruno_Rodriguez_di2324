class Carta:
    def __init__(self, valor):
        self.valor = valor
        self.revelada = False

    def revelar(self):
        self.revelada = True

    def ocultar(self):
        self.revelada = False

    def es_revelada(self):
        return self.revelada

    def obtener_valor(self):
        return self.valor
