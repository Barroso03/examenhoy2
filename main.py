from ejercicios.ejercicios1_2 import *
from ejercicios.ejercicio3 import *
from ejercicios.ejercicio5 import *


if __name__ == '__main__':
    Alumno.crear_alumnos()
    Producto.crear_producto()
    
    c = Coche("rojo", 4, 150, 1300)
    b = Bicicleta("azul", 2, "urbana")
    r = Camioneta("verde", 4, 90, 2000, 1000)
    m = motocicleta
    a = Alumno("Juan", 4)
    print(a)
    print(a.calificacion())