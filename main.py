from Perro import Perro
from Gato import Gato
from Pez import Pez

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
