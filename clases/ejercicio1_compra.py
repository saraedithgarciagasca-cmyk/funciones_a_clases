# EJERCICIO 1. DESCUENTO EN TIENDA
# Una tienda aplica un descuento del 10% a las compras
# de $1000 o más. Las compras menores no tienen descuento.
# Se necesita mostrar el descuento y el total a pagar.

# PROBLEMA
# Calcular el total a pagar de una compra según su monto.

# ENTRADAS
# monto : float, pesos, valor mayor o igual a 0.

# SALIDAS
# descuento : float, pesos, mostrar con 2 decimales.
# total : float, pesos, mostrar con 2 decimales.

# REGLAS Y SUPUESTOS
# - Si el monto es de $1000 o más, el descuento es del 10%.
# - Si el monto es menor a $1000, el descuento es $0.
# - Con $1000 exactos sí se aplica el descuento.
# - total = monto - descuento.
# - Se supone que el monto ingresado es válido.
# - Los resultados se muestran con 2 decimales.

# CLASE
# Nombre: CompraTienda
# Responsabilidad: almacenar el monto de una compra,
# calcular su descuento y total, y mostrarlos.

# ATRIBUTOS
# monto : float
#   Monto de la compra. Valor inicial: 0.0.
# descuento : float
#   Descuento calculado. Valor inicial: 0.0.
# total : float
#   Total a pagar. Valor inicial: 0.0.

# CONTRATO DE CLASE
# class CompraTienda:
#
#   __init__(self) -> None:
#     Inicializa monto=0.0, descuento=0.0 y total=0.0.
#
#   leerMonto(self) -> None:
#     Solicita el monto y lo guarda en self.monto.
#
#   calcularTotal(self) -> None:
#     Calcula el descuento según self.monto, lo guarda en
#     self.descuento y almacena el total en self.total.
#
#   mostrarTotal(self) -> None:
#     Muestra self.monto, self.descuento y self.total con 2 decimales.

# ALGORITMO
# 1. Desde menu/menu.py crear un objeto CompraTienda.
# 2. Ejecutar leerMonto().
# 3. Ejecutar calcularTotal():
#    Si self.monto >= 1000:
#        self.descuento = self.monto * 0.10
#    En caso contrario:
#        self.descuento = 0.0
#    self.total = self.monto - self.descuento
# 4. Ejecutar mostrarTotal():
#    mostrar el monto, el descuento y el total con 2 decimales.

# CASOS DE PRUEBA
# $500     -> descuento $0.00,   total $500.00
# $999.99  -> descuento $0.00,   total $999.99
# $1000    -> descuento $100.00, total $900.00
# $2500    -> descuento $250.00, total $2250.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase CompraTienda.
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


class CompraTienda:

    def __init__(self) -> None:
        self.monto = 0.0
        self.descuento = 0.0
        self.total = 0.0

    def leerMonto(self) -> None:
        self.monto = float(input("Monto de la compra: $"))

    def calcularTotal(self) -> None:
        if self.monto >= 1000:
            self.descuento = self.monto * 0.10
        else:
            self.descuento = 0.0
        self.total = self.monto - self.descuento

    def mostrarTotal(self) -> None:
        print(f"Monto: ${self.monto:.2f}")
        print(f"Descuento: ${self.descuento:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")
