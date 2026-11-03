# EJERCICIO 3. CONVERSIÓN DE TEMPERATURA
# Se necesita convertir una temperatura de grados Celsius
# a grados Fahrenheit e indicar si hace frío, templado o calor.

# PROBLEMA
# Convertir una temperatura de Celsius a Fahrenheit y clasificarla.

# ENTRADAS
# celsius : float, grados Celsius, cualquier valor real.

# SALIDAS
# fahrenheit : float, grados Fahrenheit, mostrar con 2 decimales.
# clima : str, "Frío", "Templado" o "Calor".

# REGLAS Y SUPUESTOS
# - fahrenheit = celsius * 9 / 5 + 32.
# - Menos de 15 °C: "Frío".
# - De 15 °C a 25 °C (incluidos): "Templado".
# - Más de 25 °C: "Calor".
# - Con 15 °C es "Templado"; con 25 °C es "Templado".
# - Se supone que la temperatura ingresada es válida.
# - Fahrenheit se muestra con 2 decimales.

# CLASE
# Nombre: Temperatura
# Responsabilidad: almacenar una temperatura en Celsius,
# convertirla a Fahrenheit, clasificarla y mostrarla.

# ATRIBUTOS
# celsius : float
#   Temperatura en grados Celsius. Valor inicial: 0.0.
# fahrenheit : float
#   Temperatura convertida. Valor inicial: 0.0.
# clima : str
#   Clasificación del clima. Valor inicial: "".

# CONTRATO DE CLASE
# class Temperatura:
#
#   __init__(self) -> None:
#     Inicializa celsius=0.0, fahrenheit=0.0 y clima="".
#
#   leerCelsius(self) -> None:
#     Solicita la temperatura y la guarda en self.celsius.
#
#   convertir(self) -> None:
#     Convierte self.celsius a Fahrenheit y guarda el
#     resultado en self.fahrenheit.
#
#   clasificar(self) -> None:
#     Según self.celsius guarda "Frío", "Templado" o "Calor"
#     en self.clima.
#
#   mostrarTemperatura(self) -> None:
#     Muestra self.celsius, self.fahrenheit con 2 decimales
#     y self.clima.

# ALGORITMO
# 1. Desde menu/menu.py crear un objeto Temperatura.
# 2. Ejecutar leerCelsius().
# 3. Ejecutar convertir():
#    self.fahrenheit = self.celsius * 9 / 5 + 32
# 4. Ejecutar clasificar():
#    Si self.celsius < 15:
#        self.clima = "Frío"
#    En caso contrario, si self.celsius <= 25:
#        self.clima = "Templado"
#    En caso contrario:
#        self.clima = "Calor"
# 5. Ejecutar mostrarTemperatura():
#    mostrar Celsius, Fahrenheit con 2 decimales y el clima.

# CASOS DE PRUEBA
# 0 °C   -> 32.00 °F  Frío
# 15 °C  -> 59.00 °F  Templado
# 25 °C  -> 77.00 °F  Templado
# 30 °C  -> 86.00 °F  Calor
# -10 °C -> 14.00 °F  Frío

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase Temperatura.
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


class Temperatura:

    def __init__(self) -> None:
        self.celsius = 0.0
        self.fahrenheit = 0.0
        self.clima = ""

    def leerCelsius(self) -> None:
        self.celsius = float(input("Temperatura en °C: "))

    def convertir(self) -> None:
        self.fahrenheit = self.celsius * 9 / 5 + 32

    def clasificar(self) -> None:
        if self.celsius < 15:
            self.clima = "Frío"
        elif self.celsius <= 25:
            self.clima = "Templado"
        else:
            self.clima = "Calor"

    def mostrarTemperatura(self) -> None:
        print(f"Celsius: {self.celsius:.2f} °C")
        print(f"Fahrenheit: {self.fahrenheit:.2f} °F")
        print(f"Clima: {self.clima}")
