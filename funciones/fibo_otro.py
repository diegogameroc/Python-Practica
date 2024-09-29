# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
print("")
def Fibonacci (a):
    sumFibo = 0
    Serie =[]
    i = 0
    j = 1
    while sumFibo < a :
        Serie.append(i)
        sumFibo = i + j
        i = j
        j = sumFibo
    Serie.append(i)
    return Serie 

aux = Fibonacci(50)
print(str(aux))