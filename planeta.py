import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = masa                          # kg
        self.radio = radio                        # metros
        self.distancia_al_sol = distancia_al_sol  # UA
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4 / 3) * math.pi * self.radio ** 3
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2

    
    def __str__(self):
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        return (f"Planeta {self.nombre}: densidad = "
                f"{self.calcular_densidad():.2f} kg/m³, planeta {tipo}")


# Instancias de prueba
tierra = Planeta("Tierra", 5.972e24, 6.371e6, 1.0, True)
jupiter = Planeta("Júpiter", 1.898e27, 6.9911e7, 5.2)
saturno = Planeta("Saturno", 5.683e26, 5.8232e7, 9.58)

print(tierra)
print(jupiter)
print(saturno)