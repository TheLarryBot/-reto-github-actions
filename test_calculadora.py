from calculadora import promedio, estado


def test_promedio():
    assert promedio([3.0, 4.0, 5.0]) == 4.0


def test_aprobado():
    assert estado(3.5) == "Aprobado"


def test_reprobado():
    assert estado(2.5) == "Reprobado"
