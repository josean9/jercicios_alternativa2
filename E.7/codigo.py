# viaje escolar 
print("Calculo de viaje escolar segun el numero de alumnos y el costo por alumno")
alumnos = int(input("Ingrese el numero de alumnos: "))
dias = int(input("Ingrese el numero de dias: "))
def trayecto(alumnos):
    if alumnos <= 25:
        costotrayecto = 67,30*alumnos
    elif alumnos > 25 :
        costotrayecto = 61*alumnos
    return costotrayecto
print("El costo total del trayecto es de: ", trayecto(alumnos), "€")

def comida(alumnos, dias):
   costocomida = 3.50*alumnos*dias
print("El costo total de la comida es de: ", comida(alumnos, dias), "€")