from src._03condicionales import mayor_de_dos_numeros, es_numero_par, calificacion_examenes

def test_mayor_de_dos_numeros():
    assert mayor_de_dos_numeros(5, 3) == 5
    assert mayor_de_dos_numeros(2, 4) == 4

def test_es_numero_par():
    assert es_numero_par(2) == True
    assert es_numero_par(3) == False

def test_calificacion_examenes():
    assert calificacion_examenes(75) == 'Aprobado'
    assert calificacion_examenes(59) == 'Reprobado'