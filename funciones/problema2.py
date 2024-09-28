# Suma los divisores de los numeros del 5 al 20

def sumdiv(num):
    listado_div=[]
    for i in range(num):
        div=i+1
        if num % div == 0:
            listado_div.append(div)
        
    return sum(listado_div)
    

from pprint import pprint

dic_numeros={}

for numero in range(5,21):
    dic_numeros[numero]=sumdiv(numero)
    pass
pprint(dic_numeros)