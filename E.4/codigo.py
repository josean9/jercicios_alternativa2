def evaluacion_alumno(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 15:
        evaluacion = "Alumno con talento"
    elif media >= 12:
        evaluacion = "Alumno con capacidad"
    else:
        evaluacion = "Debe reorientarse"
    return media, evaluacion

