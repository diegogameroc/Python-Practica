libro ={'nombre':'Harry Potter','autor':'J.K.Rowling','paginas':300,'genero':'fantasia'}
libro['anio_publicacion']=1997

libro
print(f'Autor: {libro['autor']}')

libro.pop('genero')

libro.items()


for clave,valor in libro.items():
    #Modifico las claves y las paso a mayusculas
    if type(valor)=='str':
        libro[clave]=valor.upper()
    
    print(clave,valor)
    
    
    for anio in range(2001,2013):
        print(f"Informes del ano {anio}")