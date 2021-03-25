# Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.

cad_1 = input("Ingresa una cadena de caracteres: ")
cad_2 = input("Ingresa otra cadena de caracteres: ")

if len(cad_1) > len(cad_2):
    print(f"La cadena {cad_1} es más larga.")
elif len(cad_1) == len(cad_2):
    print("Las cadenas tienen la misma longitud.")
else:
    print(f"La cadena {cad_2} es más larga.")