# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. 
# Imprimir aquellas que empiecen y terminen con la misma letra.

pal = input("Ingrese una palabra: ")
while pal != "FIN":
    if pal[0] == pal[len(pal)-1]:
        print(pal)
    pal = input("Ingrese una palabra: ")