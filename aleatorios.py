#!/usr/bin/env python3
"""
Módulo para la generación de números pseudoaleatorios utilizando el algoritmo
del Generador Lineal Congruente (LGC).

Estudiante: Marta Pitarch Granell
Descripción: Este fichero contiene una clase iterable 'Aleat' y una función
generadora 'aleat()' que permiten generar secuencias bajo el estándar POSIX 
o parámetros personalizados.
"""

class Aleat:
    """
    Clase iterable e iteradora que implementa el algoritmo LGC.

    El algoritmo calcula el siguiente término mediante la ecuación:
    x_{n+1} = (a * x_n + c) % m

    Ejemplos de uso con doctest:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Inicializa los parámetros del generador LGC utilizando únicamente
        argumentos por clave (keyword-only parameters).
        """
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.estado = x0

    def __iter__(self):
        """Retorna el propio objeto como iterador."""
        return self

    def __next__(self):
        """Calcula y devuelve el siguiente número pseudoaleatorio."""
        self.estado = (self.a * self.estado + self.c) % self.m
        return self.estado

    def __call__(self, x0, /):
        """
        Reinicia la secuencia tomando la nueva semilla proporcionada.
        Obligatoriamente posicional (positional-only parameter).
        """
        self.x0 = x0
        self.estado = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que implementa el algoritmo LGC.

    Argumentos:
        m (int): Módulo del generador. Por defecto, POSIX (2**48).
        a (int): Multiplicador. Por defecto, POSIX.
        c (int): Incremento. Por defecto, POSIX.
        x0 (int): Semilla inicial. Por defecto, 1212121.

    Produce:
        int: Siguiente número pseudoaleatorio de la secuencia.

    Ejemplos de uso con doctest:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    estado = x0
    while True:
        estado = (a * estado + c) % m
        # Al usar send(), el valor enviado se captura en la asignación de yield
        nueva_semilla = yield estado
        if nueva_semilla is not None:
            estado = nueva_semilla


if __name__ == "__main__":
    import doctest
    # Ejecuta los tests unitarios embebidos en las cadenas de documentación
    doctest.testmod()