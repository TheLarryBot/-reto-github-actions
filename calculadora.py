def promedio(notas):
    return sum(notas) / len(notas)


def estado(nota):
    return "Aprobado" if nota >= 3.0 else "Reprobado"
