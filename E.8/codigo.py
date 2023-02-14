def prima_anual(distancia_recorrida: float, antigüedad: int, accidentes: int):
    prima_distancia = min(distancia_recorrida* 0.01, 400)
    prima_antigüedad = 0
    if antigüedad >= 4:
        prima_antigüedad = 200 + (antigüedad - 4)* 20

    prima_total = prima_distancia + prima_antigüedad 
    if accidentes == 0:
        return prima_total
    elif accidentes == 1:
        return prima_total / 2
    elif accidentes == 2:
        return prima_total / 3
    elif accidentes == 3:
        return prima_total / 4
    else:
        return 0