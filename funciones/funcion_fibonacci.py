"""
Número de Fibonacci
Escribe una función que devuelva el n-ésimo número de Fibonacci. 
Los primeros dos números de Fibonacci son 0 y 1, y cada número posterior es la suma de los dos anteriores.
    
"""

def fibonacci_n_terms(n):
    Serie = []  # Inicializamos la lista vacía para almacenar la serie
    
    for i in range(n):  # Iteramos desde 0 hasta n-1
        if i == 0:  # Si es el primer término, añadimos 0
            Serie.append(0)
        elif i == 1:  # Si es el segundo término, añadimos 1
            Serie.append(1)
        else:  # Para los términos restantes, sumamos los dos anteriores
            siguiente = Serie[i - 1] + Serie[i - 2]
            Serie.append(siguiente) 
    return Serie

# Ejemplo de prueba
aux = fibonacci_n_terms(10)  
print(str(aux))
