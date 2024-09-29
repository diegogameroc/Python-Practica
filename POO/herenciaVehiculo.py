class Vehiculo:
    def __init__(self,marca,modelo,matricula):
        self.marca=marca
        self.modelo=modelo
        self.matricula=matricula
        
    def __str__(self):
        return f"Marca:{self.marca}, Modelo: {self.modelo}, Matricula: {self.matricula}"
    
#Creación de una clase Coche que hereda de vehiculo,clase hija

class Coche(Vehiculo):
    def __init__(self, marca,modelo,matricula,anchura,altura):
    #Llamamos al constructor de la clase hija
        super().__init__(marca,modelo,matricula)
        #Atributos propios de la clase coche
        self.ancho=anchura
        self.alto=altura
        
        #Sobreescritura del metodo __str__ para añadir atributos propios
    def __str__(self):
        return super().__str__() + f", Ancho: {self.ancho}, Alto: {self.alto}"

class Moto(Vehiculo) :
    def __init__(self,marca,modelo,matricula,cilindrada):
        super().__init__(marca,modelo,matricula)
        #Atributos propios
        self.cilindrada=cilindrada
        
        #Sobreescritura
    def __str__(self):
        return super().__str__() + f", Cilindrada: {self.cilindrada}"
       
#Creamos un objeto de la clase coche

mi_coche = Coche("Toyota","Corolla","1234ABC",2.5,1.5)
print(mi_coche)

mi_moto = Moto("Honda", "CBR", "5678DEF", 250)
print(mi_moto)
       