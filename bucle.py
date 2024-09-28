"""
    Mientras que año sea menor o igual a 2012, imprimir la 
    frase "Informes del Año"
    * Para el año 2010 realizamos una salida forzada del bucle
    * si el año es 2005 o 2006 , no imprimas ese informe
    
    
"""
anio=2001
while anio <= 2012:
    
    if anio==2010:
        print("Salida del bucle, año 2010")
        break
    
    if anio in [2005,2066]:
        anio +=1 # aumentamos el contador
        continue
    
    print(f'Informes del año {anio}')
    anio +=1
    pass # pass es un comando que no hace nada
print('Finalizando el programa')

