anio=2001
while anio<=2012:
    if anio in [2005,2006]:
     pass
    else:
        print(f"Informes del año {anio}")
    
    if anio==2010:
        print('Salida del bucle , año 2010')
        break
    anio+=1
pass
print("Finalizando el programa")