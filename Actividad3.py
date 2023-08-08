import math

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina_inferior_izquierda = punto1
        self.esquina_superior_derecha = punto2

    def calcular_perimetro(self):
        base = abs(self.esquina_inferior_izquierda.x - self.esquina_superior_derecha.x)
        altura = abs(self.esquina_inferior_izquierda.y - self.esquina_superior_derecha.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inferior_izquierda.x - self.esquina_superior_derecha.x)
        altura = abs(self.esquina_inferior_izquierda.y - self.esquina_superior_derecha.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inferior_izquierda.x - self.esquina_superior_derecha.x)
        altura = abs(self.esquina_inferior_izquierda.y - self.esquina_superior_derecha.y)
        return base == altura

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_al_centro = punto.calcular_distancia(self.centro)
        return distancia_al_centro <= self.radio
    def verificar_punto(self, punto):
        return (punto.x - self.centro[0])*2 + (punto.y - self.centro[1]) * 2 == self.radio**2

class Carta:
    PINTAS = ["Corazón", "Diamante", "Trébol", "Pica"]

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad >= 0:
            self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad >= 0 and cantidad <= self.balance:
            self.balance -= cantidad

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= abs(cuota_manejo)

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance:.2f} USD")



# Ejemplo de uso
vehiculo = Vehiculo(200, 50000)
print(f"Velocidad máxima del vehículo: {vehiculo.velocidad_maxima} km/h")
print(f"Kilometraje del vehículo: {vehiculo.kilometraje} km")

punto1 = Punto(0, 0)
punto2 = Punto(3, 4)
punto1.mostrar()
punto2.mostrar()
print(f"Distancia entre los puntos: {punto1.calcular_distancia(punto2):.2f}")

rectangulo = Rectangulo(Punto(1, 1), Punto(4, 5))
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"¿Es un cuadrado? {rectangulo.es_cuadrado()}")

circulo = Circulo(Punto(0, 0), 5)
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
punto3 = Punto(3, 3)
print(f"¿El punto pertenece al círculo? {circulo.punto_pertenece(punto3)}")

carta = Carta("As", "Pica")
print(f"Carta: {carta.valor} de {carta.pinta}")

cuenta = CuentaBancaria("1234567890", ["Juan", "Ana"], 5000)
cuenta.depositar(1000)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()