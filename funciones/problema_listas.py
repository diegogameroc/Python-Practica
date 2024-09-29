"""
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    Debes escribir una función que reciba una cadena de texto con un día de la semana y una fecha (que puede estar en dos formatos):

Formato numérico: "3/10/2024" (día/mes/año).
Formato textual: "Miércoles 10, Octubre 2024" (día de la semana, día del mes, mes, año).
La función debe convertir ambos formatos a un formato estándar: YYYY-MM-DD (año-mes-día), y también debe verificar si el día de la semana que aparece en el formato textual es correcto para esa fecha.

Por ejemplo:

"3/10/2024" debería devolver 2024-10-03.
"Miércoles 10, Octubre 2024" debería devolver 2024-10-10 solo si el 10 de octubre de 2024 es un miércoles; de lo contrario, debe devolver un mensaje de error indicando que el día de la semana no coincide.
    
"""

import datetime

# Lista de días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Lista de meses
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def convertirFecha(fecha):
    # Caso 1: Formato numérico "día/mes/año"
    if "/" in fecha:
        dia, mes, anio = fecha.split("/")
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        return f"{anio}-{mes:02}-{dia:02}"
    
    # Caso 2: Formato textual "DíaSemana día, Mes año"
    else:
        dia_semana, dia, mes, anio = fecha.replace(",", "").split()
        dia = int(dia)
        anio = int(anio)
        
        # Convertir el mes a número usando la lista 'meses'
        mes = meses.index(mes) + 1
        
        # Crear un objeto de fecha con el día, mes y año
        fecha_obj = datetime.date(anio, mes, dia)
        
        # Obtener el día de la semana correcto para esa fecha
        dia_semana_correcto = dias_semana[fecha_obj.weekday()]  # weekday() devuelve 0 para Lunes, 1 para Martes, etc.
        
        # Verificar si el día de la semana coincide
        if dia_semana != dia_semana_correcto:
            return f"Error: El día de la semana {dia_semana} no coincide con la fecha {fecha_obj}. Debería ser {dia_semana_correcto}."
        
        return f"{anio}-{mes:02}-{dia:02}"

# Ejemplos de uso:
print(convertirFecha("3/10/2024"))            # Salida esperada: 2024-10-03
print(convertirFecha("Miércoles 10, Octubre 2024"))  # Salida esperada: 2024-10-10
print(convertirFecha("Viernes 10, Octubre 2024"))    # Salida esperada: Error
