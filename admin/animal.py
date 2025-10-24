class Animal:
    def __init__(self, nombre, tipo_movimiento):
        self.nombre = nombre
        self.tipo_movimiento = tipo_movimiento
    
    def hablar(self):
        raise NotImplementedError

    def moverse(self):
        print(f"{self.nombre} empezó a {self.tipo_movimiento} a toda velocidad!!")