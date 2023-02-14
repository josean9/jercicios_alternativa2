#Ejercicio 6: Descuento en los microprocesadores

def descuentos():
    print("A continuacion tendra una calculadora de descuentos en los microprocesadores")
    print("Eres abonado a COMMAQ o a BEL? (S/N)")
    abonado = input()
    if abonado == "S":
        print("A cual de los 2? (COMMAQ/BEL)")
        abonado = input()
    print("Cuantos microprocesadores quieres comprar?")
    cantidad = input(int())
    if cantidad (10000, 20000):
    
        if abonado == "COMMAQ":
            print("Va a tener un descuento del 8%")
        elif abonado == "BEL":
            print("Va a tener un descuento del 11%")
        else:
            print("Va a tener un descuento del 10%")
    elif cantidad (20001, 40000 ):
        if abonado == "COMMAQ":
            print("Va a tener un descuento del 13%")
        elif abonado == "BEL":
            print("Va a tener un descuento del 16%")
        else:
            print("Va a tener un descuento del 15%")
    
    elif cantidad > 40000:
        if abonado == "COMMAQ":
            print("Va a tener un descuento del 18%")
        elif abonado == "BEL":
            print("Va a tener un descuento del 21%")
        else:
            print("Va a tener un descuento del 20%")
descuentos()
