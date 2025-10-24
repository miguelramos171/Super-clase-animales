# 🐾 Superclase Animales  

Este proyecto en **Python** demuestra el uso de **herencia y polimorfismo** en la **Programación Orientada a Objetos (POO)** mediante una superclase llamada `Animal` y varias subclases (`Perro`, `Gato`, `Pez`) que heredan de ella.  

---

## 🧠 Descripción del programa  

El programa modela distintos tipos de animales mostrando cómo comparten comportamientos generales (como **moverse**) y al mismo tiempo poseen acciones únicas (como **hablar** y **jugar**) según su especie.  

El código permite:  
- Definir una **superclase `Animal`** con atributos y métodos comunes.  
- Crear **subclases específicas** que heredan y redefinen comportamientos.  
- Ejecutar acciones con varios animales para demostrar el **polimorfismo**.  

---

## 🧩 Estructura del código  

### 🦴 Clase `Animal`

La clase `Animal` actúa como **superclase**.  
Define los atributos y métodos comunes a todos los animales.  

**Atributos:**  
- `nombre`: nombre del animal.  
- `tipo_movimiento`: forma en que el animal se desplaza (por ejemplo, correr o nadar).  

**Métodos:**  
- `hablar()`: método abstracto que será implementado por las subclases.  
- `moverse()`: imprime un mensaje indicando cómo se mueve el animal.  

```python
class Animal:
    def __init__(self, nombre, tipo_movimiento):
        self.nombre = nombre
        self.tipo_movimiento = tipo_movimiento
    
    def hablar(self):
        raise NotImplementedError

    def moverse(self):
        print(f"{self.nombre} empezó a {self.tipo_movimiento} a toda velocidad!!")
