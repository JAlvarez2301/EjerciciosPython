'''
Crear una clase Motocicleta que inicialice los siguientes atributos (3 puntos)
color, Matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion,
velocidad_punta, y peso.
Añade otro atributo llamado motor. Lo utilizaremos con un valor booleano para especificar si el
motor está en marcha o detenido. True, en marcha. False, detenido. Por defecto, q los motores
estarán detenidos.
Método arrancar:
Si el motor está detenido, se indica que el motor ha arrancado.
Si el motor está ya en marcha y se intenta arrancar de nuevo, se indica que el motor ya estaba en
marcha.
Método detener:
Si el motor está en marcha, se indica que el motor se ha detenido.
Si el motor está ya detenido, y se intenta detener de nuevo, se indica que el motor ya estaba
detenido.
Crea el metodo __str__ con toda la información de la motocicleta.
Crea un método para comprobar la cantidad de combustible que tienen las motocicletas. Este
servirá para informarnos del estado antes de iniciar el repostaje.
Crea el metodo repostaje añadirá los litros que faltan al deposito, el precio de la gasolina es de
1,63 E/litro, al final del repostaje debe informar los litros suministrados y el precio total.
Añadir un atributo capacidadDeposito
'''


class Motocicleta:
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, motor, capacidadDeposito):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False  # Se nos pide que por defecto el motor esté detenido
        self.capacidadDeposito = capacidadDeposito

    def arrancar(self, arrancar):
        if self.motor == True:
            self.motor = True
            print("El motor ya está en marcha")
        else:
            self.motor = True
            print("El motor se ha arrancado")

    def detener(self, detener):
        if self.motor == False:
            self.motor = False
            print("El motor ya está detenido")
        else:
            self.motor = False
            print("El motor se ha detenido")

    def __str__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, capacidadDeposito):
        print("El color es: " + color, "\n La matricula es: " + matricula, "\n La cantidad de combustible es: " + str(combustible_litros), "\n El numero de ruedas es: " + str(numero_ruedas), "\n La Marca es: " + marca, "\n La Modelo es: " + modelo,
        "La fecha de fabricación es: " + fecha_fabricacion, "\n La velocidad punta es: " + velocidad_punta, "\n El peso es:  " + peso+"\n La capacidad de deposito es: " + str(capacidadDeposito))
    
    def Comprobar_combustible(self, combustible_litros, capacidadDeposito):
        print("La cantidad de combustible es: " + str(combustible_litros)+"\n y La capacidad de deposito es: " + str(capacidadDeposito))
    
    def repostaje(self,combustible_litros, capacidadDeposito):
        litros_suministrados = 0
        litros_suministrados = capacidadDeposito - combustible_litros
        precio_total = litros_suministrados*1,63
        print("El precio del repostaje es: " + str(precio_total)+"\n La cantidad de litros suministrados es: " + str(litros_suministrados))
