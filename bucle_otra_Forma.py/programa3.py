"""
Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos 'SAL' no se apaga.

Esta calculadora funciona de la siguiente manera:

Recogemos los datos A y B

- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
- Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
 """
import math
CLAVE="sal"
while True:
    print("1. la raíz cuadrada de la suma de A y B")
    print("2. calcula A / B. Vigilamos que B no sea 0")
    print("3. calculamos la siguiente fórmula: ( A * B ) / 2.5")
    opcion=(input("Ingrese una opcion : "))
    
    if opcion==CLAVE:
         print("Se esta apagando la calculadora")
         break
    
    if opcion=="1":
        num1=int(input("Ingrese el primer numero "))
        num2=int(input("Ingrese el segundo numero "))
    
        resultad1=(math.sqrt(num1+num2))
        print(f"El resultado es: {resultad1}")
    if opcion=="2":
        num1=int(input("Ingrese el primer numero "))
        num2=int(input("Ingrese el segundo numero "))
        if num2==0:
            print("No se puede dividir entre cero")
        elif num2>0:
            resultad2=(num1/num2)
            print(f"El resultado es: {resultad2}")
        
    if opcion=="3":
        num1=int(input("Ingrese el primer numero "))
        num2=int(input("Ingrese el segundo numero "))
        resultad3=float((num1*num2)/2.5)
        print(f"El resultado es: {resultad3}")
    else:
        print("Opcion no valida ")
  

        
        
    
    
     
     
     