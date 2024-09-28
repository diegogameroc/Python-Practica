lista=["diego","lady","amor"]

for nombre in lista:
    print(nombre)
    
for i, nombre in enumerate(lista):
    print(i,nombre)
    

for i, nombre in enumerate(lista):
    if nombre == 'diego':
        lista[i]= 'POTO'
print(lista)

d={'foo':1,'bar':2,'baz':3}
for k, v in d.items():
    print('k-',k,',v-',v)
    
    libro ={ 'nombre':'Harry Potter','autor':'J.K.Rowling','paginas':300}
    
        
        