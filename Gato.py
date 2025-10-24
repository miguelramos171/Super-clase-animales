from animal import Animal

class Gato(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "correr")

    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau miau!")

    def jugar(self):
        print(f"{self.nombre} está corriendo tras un ratón de juguete")
