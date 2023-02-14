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
            descuento2 = 8/100
            print("Va a tener un descuento del 8%")
        elif abonado == "BEL":
            descuento2 = 11/100
            print("Va a tener un descuento del 11%")
        else:
            print("Va a tener un descuento del 10%")