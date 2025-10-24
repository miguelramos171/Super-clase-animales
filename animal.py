class Animal:
    def __init__(self, nombre, tipo_movimiento):
        self.nombre = nombre
        self.tipo_movimiento = tipo_movimiento
    
    def hablar(self):
        raise NotImplementedError

    def moverse(self):
        print(f"{self.nombre} empezó a {self.tipo_movimiento} a toda velocidad!!")


class Perro(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "correr")


    def hablar(self):
        print(f"\n{self.nombre} dice Guauu!!!")

    def jugar(self):
        print(f"{self.nombre} está corriendo tras una pelota")


class Gato(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "correr")

    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau miau!")

    def jugar(self):
        print(f"{self.nombre} está corriendo tras un ratón de juguete")


class Pez(Animal):

    def __init__(self, nombre):
        super().__init__(nombre, tipo_movimiento = "nadar")

    def hablar(self):
        print(f"{self.nombre} empezó a liberar burbujas como sonido")

    def jugar(self):
        print(f"{self.nombre} está persiguiendo un renacuajo")

def main():
    animales = [Perro("Mateo"), Gato("Michi"), Pez("Pipe")]
    
    hamster= Perro("pepo")
    hamster.jugar()
    hamster = Gato("pepo")
    hamster.jugar()

    for animal in animales:
        animal.hablar()
        animal.moverse()
        animal.jugar()
        print()

if __name__ == "__main__":
    main()
