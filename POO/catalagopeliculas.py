"""
Dado un sistema de Peliculas Streaming como Netflix, deberemos construir un catálogo de películas que permita:
- Agregar peliculas al catálogo
- Eliminar películas del catálogo
- Mostrar las películas del catálogo
- Buscar una película dentro del catálogo
"""

class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)
        
    def __str__(self):
            return '{} ({})'.format(self.titulo, self.lanzamiento)


class CatalogoPeliculas:
    peliculas = [] # Esta lista contendrá objetos de la clase pelicula
    
    #Constructor de clase, recibe una lista de objetos Pelicula
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    
    def agregar(self,p): #p será un objeto Pelicula
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)
            
    def buscar_pelicula(self,titulo_pelicula):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo_pelicula:
                return pelicula
        return None
    
    
    def eliminar_pelicula(self, titulo_pelicula:str):
        pelicula = self.buscar_pelicula(titulo_pelicula)
        if pelicula:
            nombre_pelicula=pelicula.titulo
            self.peliculas.remove(pelicula)
            print(f"Se elimino pelicula {nombre_pelicula} del listado")
        pass
    

p = Pelicula("El Padrino", 175, 1972)
catalogo_netflix = CatalogoPeliculas([p]) 
catalogo_netflix.mostrar()

catalogo_netflix.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
catalogo_netflix.agregar(Pelicula("El Padrino: Parte 3", 200, 1980))
catalogo_netflix.agregar(Pelicula("Harry Pother", 200, 2001))  # Añadimos otra

# Mostramos el catalogo de películas actualizado
catalogo_netflix.mostrar()

peliculas = [Pelicula("El señor de los Anillos", 175, 2001), 
             Pelicula("El señor de los Anillos: Las 2 Torres", 202, 2003), 
             Pelicula("El señor de los Anillos:El retorno del Rey", 200, 2005)]

catalogo_amazon = CatalogoPeliculas(peliculas=peliculas)

catalogo_amazon.mostrar()
pelicula_buscada = catalogo_netflix.buscar_pelicula("Diego")

if pelicula_buscada:
    print("Película encontrada:", pelicula_buscada)
else:
    print("Película no encontrada.")