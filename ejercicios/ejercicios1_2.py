class Alumno():
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)
    def calificacion(self):
        if self.nota >= 5:
            return "Calificacion: Aprobado" 
        else:
            return "Calificacion: Suspenso"
    def crear_alumnos():
      
      nombre = input("Introduce el nombre del alumno: ")
      nota = int(input("Introduce la nota del alumno: "))
      print("Alumno creado",Alumno(nombre, nota))
      print(Alumno.calificacion(Alumno(nombre, nota)))