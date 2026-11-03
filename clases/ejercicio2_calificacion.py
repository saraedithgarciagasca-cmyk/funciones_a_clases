# EJERCICIO 2. PROMEDIO DE CALIFICACIONES
# Un alumno tiene tres calificaciones parciales.
# Aprueba si su promedio es de 70 o más.
# Se necesita mostrar el promedio y si aprobó o reprobó.

# PROBLEMA
# Calcular el promedio de tres calificaciones y determinar
# si el alumno aprueba.

# ENTRADAS
# cal1 : float, puntos, valor entre 0 y 100.
# cal2 : float, puntos, valor entre 0 y 100.
# cal3 : float, puntos, valor entre 0 y 100.

# SALIDAS
# promedio : float, puntos, mostrar con 2 decimales.
# resultado : str, "Aprobado" o "Reprobado".

# REGLAS Y SUPUESTOS
# - promedio = (cal1 + cal2 + cal3) / 3.
# - Si el promedio es de 70 o más, el resultado es "Aprobado".
# - Si el promedio es menor a 70, el resultado es "Reprobado".
# - Con promedio de 70 exactos aprueba.
# - Se supone que las calificaciones ingresadas son válidas.
# - El promedio se muestra con 2 decimales.

# CLASE
# Nombre: Calificaciones
# Responsabilidad: almacenar las tres calificaciones de un alumno,
# calcular su promedio, determinar si aprueba y mostrarlo.

# ATRIBUTOS
# cal1 : float
#   Primera calificación. Valor inicial: 0.0.
# cal2 : float
#   Segunda calificación. Valor inicial: 0.0.
# cal3 : float
#   Tercera calificación. Valor inicial: 0.0.
# promedio : float
#   Promedio calculado. Valor inicial: 0.0.
# resultado : str
#   "Aprobado" o "Reprobado". Valor inicial: "".

# CONTRATO DE CLASE
# class Calificaciones:
#
#   __init__(self) -> None:
#     Inicializa cal1=0.0, cal2=0.0, cal3=0.0, promedio=0.0
#     y resultado="".
#
#   leerCalificaciones(self) -> None:
#     Solicita las tres calificaciones y las guarda en
#     self.cal1, self.cal2 y self.cal3.
#
#   calcularPromedio(self) -> None:
#     Calcula el promedio de las tres calificaciones y lo
#     guarda en self.promedio.
#
#   determinarResultado(self) -> None:
#     Según self.promedio guarda "Aprobado" o "Reprobado"
#     en self.resultado.
#
#   mostrarResultado(self) -> None:
#     Muestra self.promedio con 2 decimales y self.resultado.

# ALGORITMO
# 1. Desde menu/menu.py crear un objeto Calificaciones.
# 2. Ejecutar leerCalificaciones().
# 3. Ejecutar calcularPromedio():
#    self.promedio = (self.cal1 + self.cal2 + self.cal3) / 3
# 4. Ejecutar determinarResultado():
#    Si self.promedio >= 70:
#        self.resultado = "Aprobado"
#    En caso contrario:
#        self.resultado = "Reprobado"
# 5. Ejecutar mostrarResultado():
#    mostrar el promedio con 2 decimales y el resultado.

# CASOS DE PRUEBA
# 80, 90, 100 -> 90.00 Aprobado
# 70, 70, 70  -> 70.00 Aprobado
# 60, 70, 79  -> 69.67 Reprobado
# 50, 40, 30  -> 40.00 Reprobado

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase Calificaciones.
# - Usa los atributos y métodos del contrato.
# - Inicializa los atributos en __init__.
# - Utiliza self para acceder a los atributos.
# - Conserva las reglas y el orden del algoritmo.
# - No agregues funciones auxiliares ni otras clases.
# - No agregues validaciones, mensajes ni cálculos
#   no especificados.
# - No crees ni uses objetos en este archivo;
#   se crean y ejecutan desde menu/menu.py.
# - No agregues bibliotecas innecesarias.

# Implementa la clase según esta especificación.


class Calificaciones:

    def __init__(self) -> None:
        self.cal1 = 0.0
        self.cal2 = 0.0
        self.cal3 = 0.0
        self.promedio = 0.0
        self.resultado = ""

    def leerCalificaciones(self) -> None:
        self.cal1 = float(input("Calificación 1: "))
        self.cal2 = float(input("Calificación 2: "))
        self.cal3 = float(input("Calificación 3: "))

    def calcularPromedio(self) -> None:
        self.promedio = (self.cal1 + self.cal2 + self.cal3) / 3

    def determinarResultado(self) -> None:
        if self.promedio >= 70:
            self.resultado = "Aprobado"
        else:
            self.resultado = "Reprobado"

    def mostrarResultado(self) -> None:
        print(f"Promedio: {self.promedio:.2f}")
        print(f"Resultado: {self.resultado}")
