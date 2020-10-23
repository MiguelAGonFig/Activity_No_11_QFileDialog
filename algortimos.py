import math

def distancia_euclidiana(self, origen_x=0, origen_y=0, destino_x=0, destino_y=0):
    return math.sqrt(((destino_x - origen_x)**2) + ((destino_y - origen_y)**2))
