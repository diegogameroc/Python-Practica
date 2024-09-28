"""
    Escribir un programa que pida al usuario un número entero
    y muestre por pantalla un triangulo rectanglo como el de más abajo 
    de altura del numero introducdo
    para n = 4
    #
    ##
    ###
    ####
"""
h=int(input('Ingrese la altura de la piramide: '))
for i in range(1,h+1):
    print('#'*i)
    
