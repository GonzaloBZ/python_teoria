# Usando expresiones lambda escribir una función que permita codificar una
# frase según el siguiente algoritmo:
# encripto("a") --> "b"
# encripto("ABC") --> "BCD"
# encripto("Rock2021") --> "Spdl3132"


def encripto(cad):
    return "".join(list((map(lambda x: chr(ord(x) + 1), cad))))
