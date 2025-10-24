from animal import Animal

class Pez(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "nadar")

    def hablar(self):
        print(f"{self.nombre} empezó a liberar burbujas como sonido")

    def jugar(self):
        print(f"{self.nombre} está persiguiendo un renacuajo")

