import complejos as comp
def generar(n,m):
    ma = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append([])
        ma.append(l)
    return ma
def sumamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los suma, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generar(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.suma(matriz1[i][j],matriz2[i][j])
    return res
def restamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los resta, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generar(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.resta(matriz1[i][j],matriz2[i][j])
    return res

def multiplicarmatriz(matriz1,matriz2):
    """La funcion accion es un caso especial de esta funcion donde la matriz2 es un vector,
    se realiza la verificacion por medio del condicional"""
    ##GUIA m[i][j] = m[i][j] + m1[i][k]* m2[k][j]
    if len(matriz1[0]) == len(matriz2):
        res = generar(len(matriz1),len(matriz2[0]))
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = [0,0]
                for k in range(len(matriz2)):
                    res[i][j] = comp.suma(res[i][j],#
                                comp.multiplicar(matriz1[i][k],matriz2[k][j]))
        return res
    else:
        return "No se puede multiplicar"

def mostrar(matriz):
    for i in matriz:
        print(*i)
    
def inversoadimatriz(matriz):
    """Recibe una matriz o un vector y halla el inverso aditiva de este(a)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.inversoaditivo(matriz[i][j])
    return matriz

def multescalarmatriz(escalar,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.escalarpornum(escalar,matriz[i][j])
    return matriz

def transpuesta(matriz):
    res = generar(len(matriz[0]),len(matriz))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            res[i][j] = matriz[j][i]
    return res

def conjugadamatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.conjugado(matriz[i][j])
    return matriz

def adjuntamatriz(matriz):
    conjugada = conjugadamatriz(matriz)
    transpuest = transpuesta(conjugada)
    return transpuest

def main():
    ma1 = [[[1,-3],[-2,3],[-3,4]],[[3,4],[4,5],[3,5]]]
    ma2 = [[[2,3],[1,0]],[[2,3],[0,1]],[[3,4],[5,3]]]
    #mult = multiplicarmatriz(ma1,ma2)
    mostrar(ma1)
    print()
    #mostrar(ma2)
    #print()
    mostrar(adjuntamatriz(ma1))
    print()
main()
