from animales import Animales 
class Perro(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "correr")


    def hablar(self):
        print(f"\n{self.nombre} dice Guauu!!!")

    def jugar(self):
        print(f"{self.nombre} está corriendo tras una pelota")

