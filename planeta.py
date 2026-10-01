class Planeta:
       def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
           self.nombre = nombre
           self.masa = masa                      # kg
           self.radio = radio                    # metros
           self.distancia_al_sol = distancia_al_sol  # UA
           self.tiene_vida = tiene_vida