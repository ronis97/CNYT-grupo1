import complejos as c
def test_suma():
    assert c.suma([-3,2],[4,1]) ==  [1,3], 'Debe ser 1 + 3i'
def test_resta():
    assert c.resta([-3,2],[4,1]) == [-7,1], 'Debe ser -7 + i'
def test_producto():
    assert c.multiplicar([-7,3],[-2,3]) == [5,-27], 'Debe ser 5-27i' 
def test_division():
    #print(c.dividir([-7,3],[1,1]))
    assert c.dividir([-7,3],[1,1]) == [-2.0,5.0], 'Debe ser -2 +5i'
def conjugado():
    assert c.conjugado([-4,5]) == [-4,-5], 'Debe ser -4-5i'
def modulo():
    assert c.modulo([1,1]) == 1.4142, 'Debe ser 1.4142'
def fase():
    assert c.fase_complejo


if __name__ == "__main__":
    test_suma()
    test_producto()
    test_division()
    print("Prueba exitosa")
