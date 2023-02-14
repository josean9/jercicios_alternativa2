"""ADIF hace descuento a las familias que van al Parque Warner Madrid en función de la cantidad de niños
 que hay en la familia. Este descuento es del 10 % para 2 niños, 15 % para 3 niños y 18 % para 4 niños. 
 A partir de 5 niños, el descuento es del 18 %, pero aumenta un 1 % por cada niño por encima de 4.
Establecer el algoritmo que calcula el importe del descuento al que tendrá derecho una familia dada.
"""
def solicitar_datos():
    numero_de_ninos = int(input("Introduce el número de niños: "))
    precio_de_la_entrada = float(input("Introduce el precio de la entrada: "))
    return numero_de_ninos, precio_de_la_entrada
def calcular_descuento(numero_de_ninos, precio_de_la_entrada):
    if numero_de_ninos == 2:
        descuento = 0.1
    elif numero_de_ninos == 3:
        descuento = 0.15
    elif numero_de_ninos == 4:
        descuento = 0.18
    else:
        descuento = 0.18 + (numero_de_ninos - 4) * 0.01
    return ("El descuento es del", descuento * 100, "% y el precio final es de", precio_de_la_entrada * (1 - descuento), "€")