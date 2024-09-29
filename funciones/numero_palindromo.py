"""
Escribe una función que determine si un número es palíndromo 
(es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
 
"""
lista=['oso','anita lava la tina',121,123]

def esPalidromo(p):
  estandar = str(p).lower().replace(' ','')
  return estandar == estandar[::-1]
  
  
for p in lista:
    resultado=esPalidromo(p)
    print(resultado)
    
    """
    numero_str[::-1] es una forma de obtener la cadena invertida. 
    El operador [::-1] significa "toda la cadena, pero desde el final al principio".
    """
    