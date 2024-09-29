class Perro:
# metodo constructor 
# nos permite inicializar los atributos de la clase
# self es una referencia a la instancia de la clase

    """
    El método __init__ en Python es el constructor de una clase, y su 
    propósito es inicializar los atributos de la clase cuando se crea 
    una nueva instancia. El nombre especial __init__ (con dos guiones 
    bajos antes y después) es reconocido por Python como el método que
    se llama automáticamente al crear un objeto.
     
    """

    def __init__(self,nombre,color,raza)-> None:
        self.nombre = nombre
        self.color = color
        self.raza = raza
        pass
    
    # métodos de la clase,son funciones que pertenecen a la clase
    def ladrar(self):
        print("Guau Guau")
        pass
    
    def oler(self):
        print("Sniff Sniff")
        pass
    
    def dormir(self):
        print("ZZZZZ")
        
    def imprimir(self):
        print(f'Perro {self.nombre} de raza {self.raza} y color {self.color}')
        pass
    pass

 # Instanciamos la clase Perro
 
perro1= Perro("Firulais","Cafe","Pastor Aleman")
perro2= Perro("Rex","Blanco","Pitbull")

print(perro1)
print(perro2)

perro1.imprimir()
perro2.imprimir()