# Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
# ¿cuál es el promedio de las notas?
# ¿cuántos estudiantes están por debajo del promedio?


def menores_al_promedio(promedio, lista):
    tot = 0
    for nota in lista:
        if nota < promedio:
            tot += 1
    return tot


lista = []
total = 0
nota = int(input("Ingrese una nota: "))
while nota != -1:
    lista.append(nota)
    total += nota
    nota = int(input("Ingrese una nota: "))
promedio = total / len(lista)
print(f"El promedio de las notas de todos los alumnos es: {promedio}")
print(f"Cantidad de alumnos cuyas notas son menores al promedio: {menores_al_promedio(promedio, lista)}")