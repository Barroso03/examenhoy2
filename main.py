from tkinter import N
from unicodedata import name
from ejercicios.ejercicios1_2 import *
from ejercicios.ejercicio3 import *
from ejercicios.ejercicio5 import *


if __name__ == '__main__':
    print("Ejercicio1y2:")
    a = Alumno("Juan", 4)
    print(a)
    print(a.calificacion())
    Alumno.crear_alumnos()
    print("Ejercicio3:")
    Producto.crear_producto()
    print("Ejercicio5:")
    catalogar([c, b, r, M], 0)