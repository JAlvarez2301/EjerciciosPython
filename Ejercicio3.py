'''
Crear una clase Calculadora, la cual tendrá tres variables n1, n2 y n3 . Debe contener los
métodos sumar (3 números), restar (3), multiplicar(2), potencia(2), raíz cuadrada(1) y factorial(1).
Debéis mostrar la ejecución de todos los métodos.

'''

'''
Este ejercicio lo voy a hacer como si fuesen métodos donde no pasamos los parametros, luego lo realizaré correctamente, para usarlo de práctica

'''




import math
class Calculadora:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def sumar():
        n1 = int(input("Introduzca un número para sumar:"))
        n2 = int(input("Introduzca otro número para sumar:"))
        n3 = int(input("Introduzca otro número para sumar:"))
        resultado = n1 + n2 + n3
        print("El resultado es: " + str(resultado))

    def restar():
        respuesta = input(
            "Quieres introducir un número total para restar? Yes / No")
        if respuesta == "Yes" or respuesta == "yes" or respuesta == "si":
            numeroTotal = int(input("Introduzca un número para restar:"))
            numeroRestar = int(input("Introduzca cuánto le quieres restar:"))
            resultado = numeroTotal - numeroRestar
            print("El resultado es: " + str(resultado))
        else:
            print("Va a introducir entonces 3 números para restar")
            n1 = int(input("Introduzca un número para restar:"))
            n2 = int(input("Introduzca otro número para restar:"))
            n3 = int(input("Introduzca otro número para restar:"))
            resultado = n1 - n2 - n3
            print("El resultado es: " + str(resultado))

    def multiplicar():
        n1 = int(input("Introduzca un número para multiplicar:"))
        n2 = int(input("Introduzca otro número para multiplicar:"))
        resultado = n1 * n2
        print("El resultado es: " + str(resultado))

    def potencia():
        n1 = int(input("Introduzca el número al que quieres realizar la potencia:"))
        n2 = int(input("Introduzca la potencia: "))
        resultado = pow(n1, n2)
        print("El resultado es: " + str(resultado))

    def raizCuadrada():
        n1 = int(
            input("Introduzca el número al que quieres realizar la raíz cuadrada: "))
        resultado = math.sqrt(n1)
        print("El resultao es: " + str(resultado))

    def factorial():
        n1 = int(input("Introduzca el número al que quieres realizar la factorial: "))
        resultado = 1
        for i in range(1, n1 + 1):
            resultado *= i
        print("El resultado es: " + str(resultado))
        
    sumar()
    restar()
    multiplicar()
    potencia()
    raizCuadrada()
    factorial()