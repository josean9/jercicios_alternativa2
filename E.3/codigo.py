def descuento(precio):
    if precio < 100:
        return 0
    elif precio < 500:
        return precio * 0.05
    else:
        return precio * 0.08