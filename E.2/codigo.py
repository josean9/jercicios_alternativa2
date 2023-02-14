#Números, suma y producto
print("Elige dos numeros")
a = int(input("a: "))
b = int(input("b: "))
#Ahora vamos a ver el resultado de la suma y el producto
suma = a + b
producto = a * b
#decoradores
def funcion_decoradora1(funcion_parametro1):
    def funcion_interior1():
        print("Vamos a hacer la suma: ")
        funcion_parametro1()
        print("Hemos terminado la suma")
    return funcion_interior1
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("Vamos a hacer la multiplicacion: ")
        funcion_parametro()
        print("Hemos terminado la multiplicacion")
    return funcion_interior
@funcion_decoradora1
def suma():
    print(suma)
@funcion_decoradora
def producto():
    print(producto)