'''
Crear un programa que al llamar al método "misDatos" muestre nombre, apellidos, edad y 
teléfono. El usuario debe poder introducir todos estos valores por teclado y durante la ejecución
del programa se darán de alta tres usuarios y se mostrarán todos sus datos
'''


def mis_Datos():
    contador = 0
    while contador < 3:
        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca su apellido: ")
        edad = int(input("Introduzca su edad: "))
        telefono = int(input("Introduzca su teléfono: "))
        print(
            f"Datos ingresados correctamente. {nombre} {apellidos} {edad} {telefono}")
        contador = contador + 1


mis_Datos()
