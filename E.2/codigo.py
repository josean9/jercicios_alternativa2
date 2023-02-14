#Números, suma y producto
print("Elige dos numeros")
a = int(input("a: "))
b = int(input("b: "))
#Ahora vamos a ver el resultado de la suma y el producto
suma = a + b
producto = a * b
print("La suma de los dos numeros es: ", suma)
print("El producto de los dos numeros es: ", producto)
#compararemos los numero a continuacion
lista = [a, b, suma, producto]
lista.sort()
print("asi quedaria ordenados de menor a mayor ", lista)

