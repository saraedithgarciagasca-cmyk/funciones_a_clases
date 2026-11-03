import os
import sys

# esto permite importar las clases desde la carpeta "clases"
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from clases.ejercicio1_compra import CompraTienda
from clases.ejercicio2_calificacion import Calificaciones
from clases.ejercicio3_temperatura import Temperatura


def menu():
    opcion = ""
    while opcion != "0":
        print("\n===== DE FUNCIONES A CLASES =====")
        print("1. Descuento en tienda (CompraTienda)")
        print("2. Promedio de calificaciones (Calificaciones)")
        print("3. Conversión de temperatura (Temperatura)")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            compra = CompraTienda()
            compra.leerMonto()
            compra.calcularTotal()
            compra.mostrarTotal()
        elif opcion == "2":
            alumno = Calificaciones()
            alumno.leerCalificaciones()
            alumno.calcularPromedio()
            alumno.determinarResultado()
            alumno.mostrarResultado()
        elif opcion == "3":
            temp = Temperatura()
            temp.leerCelsius()
            temp.convertir()
            temp.clasificar()
            temp.mostrarTemperatura()
        elif opcion == "0":
            print("Fin del programa.")
        else:
            print("Opción no válida.")


menu()
