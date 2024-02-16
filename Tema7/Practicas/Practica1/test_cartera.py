import pytest
from cartera import Cartera,SaldoInsuficiente

def test_saldo_inicial():
    cartera = Cartera()
    assert cartera.saldo == 0

def test_saldo_inicial_positivo():
    cartera = Cartera(saldo_inicial=10)
    assert cartera.saldo == 10

def test_ingresar_dinero():
    cartera = Cartera(saldo_inicial=10)
    cartera.ingresar(20)
    assert cartera.saldo == 30

def test_gastar_dinero():
    cartera = Cartera(saldo_inicial=30)
    cartera.gastar(20)
    assert cartera.saldo == 10

def test_excepcion_saldo_insuficiente():
    cartera = Cartera(saldo_inicial=20)
    with pytest.raises(SaldoInsuficiente, match="Saldo insuficiente, Saldo actual: 20"):
        cartera.gastar(30)  

#test_cartera.py (2Parte)

def test_saldo_negativo():
    cartera = Cartera(saldo_inicial=-10)
    assert cartera.saldo == 0                      