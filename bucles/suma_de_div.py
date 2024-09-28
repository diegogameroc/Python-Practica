#Calcule la suma de divisiores para un numero dado por el usuario

numero = int(input("Ingrese un numero:  "))

listado_divisores =[]
for i in range(numero):
    div= i+1
    
    if numero % div == 0:
        listado_divisores.append(div)
        pass
    
sumatoria=0
for numero in listado_divisores:
    sumatoria+=numero
    
print(f"La sumatoria de divisores es: {sumatoria}")
    
