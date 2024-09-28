"""
    Realiza una funcion llamada area_Rectangulo (base,altura)
    que devuelva el area del rectangulo a partir de una base y
    una altura. Calcula el área de un rectangulo de 15 de base
    y 10 de altura

"""
def CalcularArea(base,altura):
    Area=base*altura
    return Area


base = float(input(("Ingrese la base: ")))
altura = float(input(("Ingrese la altura: ")))

print("El area es: ", CalcularArea(base,altura))
