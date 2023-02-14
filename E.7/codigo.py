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

def hotel(alumnos,dias):
    if alumnos <= 30:
        costohotel = 4.75*alumnos*dias
    elif alumnos >= 31 and alumnos <= 35:
        costohotel = 4*alumnos*dias
    elif alumnos >= 36:
        costohotel = 3.50*alumnos*dias
    return costohotel
print("El costo total del hotel es de: ", hotel(alumnos, dias), "€")
def costo_total_del_viaje(alumnos, dias):
    costototal = trayecto(alumnos)+comida(alumnos, dias)+hotel(alumnos, dias)
    return costototal
print("El costo total del viaje es de: ", costo_total_del_viaje(alumnos, dias), "€")