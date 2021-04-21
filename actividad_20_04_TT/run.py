import csv

archivo_txt = open("archivo.txt", "w")

# names = 3, max_players = 5, num_votes = 12, image_url = 13, category = 17
with open("bgg_db_1806.csv", newline="", encoding="utf8") as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=",")
    # Muevo el puntero del reader a la siguiente fila, ya que no quiero procesar el encabezado.
    next(reader)
    juegos_cartas = filter(lambda x: int(x[5]) < 3 and x[17] == "Card Game", reader)
    for juego in juegos_cartas:
        archivo_txt.write(juego[3])
        archivo_txt.write("\n")

archivo_txt.write("\n")

with open("bgg_db_1806.csv", newline="", encoding="utf8") as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=",")
    # Muevo el puntero del reader a la siguiente fila, ya que no quiero procesar el encabezado.
    next(reader)
    mas_votados = list(sorted(reader, key=lambda x: int(x[12]), reverse=True))
    for juego in mas_votados[:10]:
        print(f"Cant. votos: {juego[12]}")
        archivo_txt.write(juego[13])
        archivo_txt.write("\n")

archivo_csv.close()
archivo_txt.close()

# Ayuda para el punto 2
# import requests
# juego = "Gloomhaven"
# icon_url = "https://cf.geekdo-images.com/original/img/lDN358RgcYvQfYYN6Oy2TXpifyM=/0x0/pic2437871.jpg"
# icono = requests.get(icon_url)
# with open(f"ejemplos/clase6/{juego}.jpg", "wb") as f:
#    f.write(icono.content)
