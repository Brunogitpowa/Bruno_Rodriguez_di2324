def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Tiene que ser un entero")
    if n < 0:
        raise ValueError("Tiene que ser un entero positivo o cero")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)