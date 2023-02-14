"""El tipo DÍA define por enumeración un día de la semana. En el ejercicio que determina el día del 1 de mayo de un año dado, 
también se ha especificado una función sucesor para un día de la semana. Falta dar una definición de esta función.

Dar una definición completa de la función sucesor para un día de la semana.
"""
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran
        print("Comienza el programa:")
        # Llamada a la función pasada como parámetro
        funcion_parametro(*args, **kwargs)
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo, se cierra el programa")
    return funcion_interior
dias_de_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}
@funcion_decoradora
def sucesor_de_dia():
    dia = int(input("Introduce un día de la semana (1-7): "))
    if dia == 7:
        dia = 1
    else:
        dia += 1
    print("El día siguiente es", dias_de_semana[dia])
sucesor_de_dia()