# Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
# ¿cuál es el promedio de las notas?
# ¿cuántos estudiantes están por debajo del promedio?


def menores_al_promedio(prom, lista):
    """Esta función retorna la cantidad de alumnos con
    notas por debajo del promedio."""
    tot = 0
    for nota in lista:
        if nota < prom:
            tot += 1
    return tot


def leer_notas():
    """Esta función retorna una lista con notas de estudiantes."""
    liszt = []
    nota = int(input("Ingrese una nota: "))
    while nota != -1:
        liszt.append(nota)
        nota = int(input("Ingrese una nota: "))
    return liszt


def promedio(lista):
    """Esta función retorna el promedio de notas de los estudiantes."""
    total = 0
    for nota in lista:
        total += nota
    return total / len(lista)


lista = leer_notas()
prom = promedio(lista)
print(f"El promedio de las notas de todos los alumnos es: {prom}")
print(
    f"Cantidad de alumnos cuyas notas son menores al promedio: {menores_al_promedio(prom, lista)}"
)
