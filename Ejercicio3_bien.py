import math

class Calculadora:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def sumar(n1,n2,n3):
        resultado = n1 + n2 + n3
        print("El resultado de la suma es: " + str(resultado))

    def restar(n1,n2,n3):
            resultado = n1 - n2 - n3
            print("El resultado de la resta es: " + str(resultado))

    def multiplicar(n1,n2):
        resultado = n1 * n2
        print("El resultado de la multiplicación es: " + str(resultado))

    def potencia(n1,n2):
        resultado = pow(n1, n2)
        print("El resultado de la potencia es: " + str(resultado))

    def raizCuadrada(n1):
        resultado = math.sqrt(n1)
        print("El resultao de la raíz cuadrada es: " + str(resultado))

    def factorial(n1):
        
        resultado = 1
        for i in range(1, n1 + 1):
            resultado *= i
        print("El resultado del factorial es: " + str(resultado))
        
    sumar(1,2,3)
    restar(10,5,3)
    multiplicar(5,5)
    potencia(5,2)
    raizCuadrada(47)
    factorial(5)