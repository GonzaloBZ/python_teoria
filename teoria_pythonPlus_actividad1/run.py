import csv
import json
import os
import PySimpleGUI as sg

bot_size = (20, 2)
pad_bot_ds = ((30, 0), (5, 5))
pad_bot_exit = ((30, 0), (20, 30))

# directorio donde están los archivos.
path_files = "files"

layout = [
    [sg.Text("¿Qué datos analizamos?", text_color="darkblue", font=("", 14))],
    [sg.Button("Exportación Yerba Mate", size=bot_size, pad=pad_bot_ds, key="-EXPO-")],
    [sg.Button("Programas Deportivos", size=bot_size, pad=pad_bot_ds, key="-DEPOR-")],
    [sg.Button("Salir", size=bot_size, pad=pad_bot_exit, key="-SALIR-")],
]

window = sg.Window(
    "Actividad 1 x Python Plus - TEORÍA -",
    layout,
    margins=(80, 0),
    no_titlebar=True,
)


def estructurar_datos(arch, arch_path):
    datos = []
    if os.path.exists(os.path.dirname(arch_path)):
        try:
            with open(os.path.join(arch_path, arch)) as expo:
                for i in csv.DictReader(expo):
                    datos.append(dict(i))
        except FileNotFoundError:
            print("Archivo no encontrado.")
    else:
        print(f"No existe el directorio{arch_path}")
    return datos


def procesar_expo(datos):
    """
    Guarda en un archivo json, los datos de 10 países a los que se exportó yerba mate.
    campo "mercaderia_certificada" (string) Descripción del producto declarado.
    """
    paises = []
    for d in datos:
        if d["mercaderia_certificada"] == "Yerba Mate":
            paises.append(d)
    diez = [x for x in paises[:10]]
    # Guardar los datos
    arch_path = os.path.join(os.getcwd(), path_files)
    with open(os.path.join(arch_path, "expo-2020-vegetales.json"), "w") as f:
        json.dump(diez, f, indent=4)


def procesar_depo(datos):
    """
    Guarda en un archivo json, los programas deportivos del bario de Caballito.
    campo "barrio" (string).
    """
    prog_dep_cab = []
    for d in datos:
        if d["barrio"] == "Caballito":
            prog_dep_cab.append(d)
    # Guardo los datos
    arch_path = os.path.join(os.getcwd(), path_files)
    with open(os.path.join(arch_path, "prog_depo_caballito.json"), "w") as f:
        json.dump(prog_dep_cab, f, indent=4)


while True:
    event, values = window.read()

    if event == "-SALIR-" or event == sg.WIN_CLOSED:
        break

    if event == "-EXPO-":
        arch_expo = "expo-2020-vegetales-certificados-senasa.csv"
        path_arch = os.path.join(os.getcwd(), path_files)
        data = estructurar_datos(arch_expo, path_arch)
        if len(data) > 0:
            procesar_expo(data)

    if event == "-DEPOR-":
        arch_depo = "programas-deportivos.csv"
        path_arch = os.path.join(os.getcwd(), path_files)
        data = estructurar_datos(arch_depo, path_arch)
        if len(data) > 0:
            procesar_depo(data)

window.close()
