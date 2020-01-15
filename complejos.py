from sys import stdin

def suma(num1,num2):
    #num1 y num2 deben ser arreglos
    c = num1[0] + num2[0]
    d = num1[1] + num2[1]
    tot = [c,d]
    return tot

def resta(num1,num2):
    
    c = num1[0] - num2[0]
    d = num1[1] - num2[1]
    tot = [c,d]
    return tot

def multiplicar(num1,num2):
    c = num1[0]*num2[0] - num1[1]*num2[1]
    d = num1[0]*num2[1] + num1[1]*num2[0]
    tot = [c,d]
    return tot

def dividir(num1,num2):
    nume1 = num1[0] * num2[0] + num1[1]* num2[1]
    deno = num1[0]^2 + num2[1]^2
    nume2 = num1[1]*num2[0] - num1[0]*num2[1]
    c = nume1/deno
    d = nume2/deno
    tot = [c,d]
    return tot
def conjugado(num):
    d = num[1]
    d = -d
    return [num[0],d]

def modulo(num):
    c = num[0]^2 + num[1]^2
    return c^0.5
def mostrar(n):
    """a es la parte real y b es la parte imaginaria"""
    a = n[0]
    b = n[1]
    
    if b > 0:
        
        print(a,'+',str(b)+'i')
    elif b == 0:
        print(a)
        
    elif b < 0:
        print(a,'-',str(abs(b))+'i')

def main():
    n1 = [2,3]
    n2 = [1,0]
    n3 = suma(n1,n2)
    n4 = multiplicar(n1,n2)
    n5 = dividir(n1,n2)
    n6 = conjugado(n1)
    mostrar(n1)
    mostrar(n2)
    mostrar(n3)
    mostrar(n4)
    mostrar(n5)
    mostrar(n6)
main()
