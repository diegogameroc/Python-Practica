"""
    Realiza un programa que pida al usuario cuantos numeros
    quiere introducir, luego lee todos los numeros y realiza
    una media aritmetica
    
"""

cantidad_numeros=int(input("Cuantos numeros desea introducir?"))
listado_numero=[]

for i in range(cantidad_numeros):
    x=int(input(f"Ingrese el numero {i+1}:"))
    ##print(listado_numero)
    listado_numero.append(x)

media_Arit=sum(listado_numero)/(cantidad_numeros)
print('La media aritmetica es ',media_Arit)  

# Para calcular la media aritmética tenemos 
# 2 metodos

"""
    #forma 1 con funcion sum()
    
    #forma 2 
    sumatoria=0
    
    for numero in listado_numeros:
    sumatoria +=numero # acumulando resultados
    media=sumatoria/cantidad_numeros
"""
