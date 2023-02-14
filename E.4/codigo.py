def evaluacion_alumno(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 15:
        evaluacion = "Alumno con talento"
    elif media >= 12:
        evaluacion = "Alumno con capacidad"
    else:
        evaluacion = "Debe reorientarse"
    return media, evaluacion

nota1 = float(input("Introduce la primera nota:"))
nota2 = float(input("Introduce la segunda nota:"))
nota3 = float(input("Introduce la tercera nota:"))
nota4 = float(input("Introduce la cuarta nota:"))

media, evaluacion = evaluacion_alumno(nota1, nota2, nota3, nota4)

print("La media del alumno es:", media)
print("Evaluacion:", evaluacion)