"""
Este módulo contiene una implementación de la función factorial.
"""

def factorial(n):

    """
    Calcula el factorial de un número.
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial no está definido para números no enteros o negativos.")
    if n in {0, 1}:
        return 1
    return n * factorial(n - 1)
    