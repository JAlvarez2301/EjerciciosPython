'''
Repetir el ejercicio anterior utilizando un for y creando pidiendo al usuario cuantos empleados
quiere dar de alta haciendo este bucle dinámico, cada vez que se de un usuario de alta se debe
imprimir el usuario. Al final devolver el n.º de usuarios dados de alta que sean mayores de edad
'''

def mis_datos():
    NumeroEmpleados = int(input("Ingrese el número de empleados que quieres ingresar"))
    mayor_de_edad = 0
    
    for i in range(NumeroEmpleados):
        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca su apellido: ")
        edad = int(input("Introduzca su edad: "))
        telefono = int(input("Introduzca su teléfono: "))
        print(f"Datos ingresados correctamente. {nombre} {apellidos} {edad} {telefono}")
        if edad >= 18:
            mayor_de_edad += 1
            print("Este usuario es mayor de edad")
        else: print("Este usuario no es mayor de edad")
    print("Se han ingresado " + str(NumeroEmpleados) + " empleados, y son mayores de edad: " + str(mayor_de_edad))

mis_datos()        