"""Este es el módulo funcions. Aquí puedes describir lo que hace tu módulo."""

import math

def es_primo(numero):
    """Esta función determina si un número es primo."""
    if numero < 2:
        return False
    for num in range(2, math.isqrt(numero) + 1):
        if num % num == 0:
            return False
    return True
