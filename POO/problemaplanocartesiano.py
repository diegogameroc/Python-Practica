class punto:
    def __init__(self,x,y) -> None:
        self.coordenadaX=x
        self.coordenadaY=y
        print("Se añadio la coordenada: ")
    def __str__(self):
        return '{} ({} - {})'.format(self.coordenadaX, self.coordenadaY)
    

# metodo de la clase Punto
    def mostrar(self):
        print(f"Coordenada: ({self.coordenadaX},{self.coordenadaY})")
    
    def cuadrante(self):
        x = self.coordenadaX
        y = self.coordenadaY

        if x == 0 and y == 0:
            return "Está en el origen."
        elif x == 0:
            return "Está sobre el eje Y."
        elif y == 0:
            return "Está sobre el eje X."
        elif x > 0 and y > 0:
            return "Está en el cuadrante I."
        elif x < 0 and y > 0:
            return "Está en el cuadrante II."
        elif x < 0 and y < 0:
            return "Está en el cuadrante III."
        elif x > 0 and y < 0:
            return "Está en el cuadrante IV."
        


p=punto(5,8)

p.mostrar()

print(p.cuadrante())