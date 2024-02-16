class SaldoInsuficiente(Exception):
    pass

class Cartera(object):

    def __init__(self, saldo_inicial=0):
        if isinstance(saldo_inicial, int) and saldo_inicial > 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0 #Se asignara el 0 en caso de salgo negativo

    def gastar(self, cantidad):
        if self.saldo < cantidad:
            raise SaldoInsuficiente("Saldo insuficiente, Saldo actual: {}".format(self.saldo))
        self.saldo -= cantidad

    def ingresar(self, cantidad):
        self.saldo += cantidad
        