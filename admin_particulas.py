from particula import Particula
import json

class Admin_particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, part:Particula):
        self.__particulas.append(part)

    def agregar_inicio(self, part:Particula):
        self.__particulas.insert(0, part)
    
    def consultar(self):
        for part in self.__particulas:
            print(part)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0       

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0