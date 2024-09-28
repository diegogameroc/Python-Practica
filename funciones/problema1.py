"""
    Identifique los divisores para cada uno de los numeros del 10 al 30 
"""
#Funciones nos permiten reutilizar codigo

def genera_listado_divisores(num):
    listado_divisores=[]
    for i in range(numero):
        div=i+1
        if numero % div == 0:
            listado_divisores.append(div)
            pass
    return listado_divisores


from pprint import pprint
dic_numeros ={}

for numero in range(10,31):
    dic_numeros[numero]=genera_listado_divisores(numero) # aqui deberia ir el listado de los divisores del numero colacado como llave
    pass
    
pprint(dic_numeros)


