import pytest
import suma

def test_suma_cero():
    assert suma.suma_enteros(0, 0) == 0

def test_suma_positivos():
    assert suma.suma_enteros(5, 5) == 10

def test_suma_positivos_negativos():
    assert suma.suma_enteros(-5, 5) == 0

def test_suma_negativos():
    assert suma.suma_enteros(-5, -5) == -10

def test_suma_excepcion_sumando1():
    with pytest.raises(TypeError):
        suma.suma_enteros(5.0,5) == 0

def test_suma_excepcion_sumando2():
    with pytest.raises(TypeError):
        suma.suma_enteros(5.0, 'a') == 0 

def test_suma_excepcion_sumandos():
    with pytest.raises(TypeError):
        suma.suma_enteros(True, 'a') == 0                               
