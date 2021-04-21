import csv

archivo_txt = open("archivo.txt", "w")

# 1) guardar en otro archivo las películas agregadas en el año 2020.
# type = 1 (TV Show, Movie), title = 2, country = 5, date_added = 6
with open("netflix_titles.csv", newline="", encoding="utf8") as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=",")
    # Muevo el puntero del reader a la siguiente fila, ya que no quiero procesar el encabezado.
    next(reader)
    pel_2020 = filter(lambda x: "2020" in x[6] and x[1] == "Movie", reader)
    for pel in pel_2020:
        archivo_txt.write(pel[2] + "\n")

archivo_txt.write("\n\nPaíses con más producciones: \n")

# 2) los cinco (5) países con más producciones en Netflix.
# type = 1 (TV Show, Movie), title = 2, country = 5, date_added = 6
with open("netflix_titles.csv", newline="", encoding="utf8") as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=",")
    # Muevo el puntero del reader a la siguiente fila, ya que no quiero procesar el encabezado.
    next(reader)
    # Obtengo todos los países de las producciones.
    countries = [x[5] for x in reader]
    # Debo hacer esto por cómo están guardados los países.
    l_countries = "\n".join(countries).replace(",", "\n")
    list_countries = l_countries.split("\n")
    nueva = [pais.strip() for pais in list_countries if pais != ""]
    # Obtengo todos los países sin repetir.
    set_countries = set(nueva)
    # Obtengo una lista de tuplas de cada país con la cantidad de producciones.
    lista_final = [(pais, nueva.count(pais)) for pais in set_countries]
    # Obtengo una lista ordenada de los países con mayor cantidad de producciones.
    mas_prod = sorted(lista_final, key=lambda x: x[1], reverse=True)
    for pais in mas_prod[:5]:
        archivo_txt.write(pais[0] + ": " + str(pais[1]) + "\n")

archivo_csv.close()
archivo_txt.close()
