"""
PIN_SECRETO='diegoredi1'
n=0
while n<3:
    contrasena= input("Ingrese la contraseña porfavor ")
    if contrasena == PIN_SECRETO:
        print('Login correcto')
        break
    else: 
        n+=1
        if n < 3:
            print("Login incorrecto, ingrese de nuevo la contraseña")
        else:
            print('Llamando a la policia')
"""
import time 
PIN_SECRETO='diegoredi1'
n=0
while True: 
    contrasena = input("Ingrese la contraseña por favor: ")
    if contrasena == PIN_SECRETO:
        print('Pin correcto')
        break  
    else: 
        n += 1
        if n < 3: 
            print(f"Ponga bien la contraseña por favor, te quedan {5-n-1} intentos")
           
        elif n == 3:  
            print("Es tu ultimo intento , sino espera 5 segundos: ")
            contrasena = input("Ingrese la contraseña por favor: ")
            if contrasena!=PIN_SECRETO:
                print("Espera 5 segundos: ")
                time.sleep(5)
        elif n == 4:  
            print("Intentos maximos alcanzados: Llamando a la policía")
            break
        
        


     