class Vehiculo():
    print("Ejercicio5:")

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )
    #Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
    
        


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    # recibe la funcion catagolar() de la clase padre
    
        
c = Coche("rojo", 4, 150, 1300)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)
    
b = Bicicleta("azul", 2, "urbana")


class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)

r = Camioneta("verde", 4, 90, 2000, 1000)


class motocicleta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.tipo = tipo

    def __str__(self):
        return Coche.__str__(self) + ", {}".format(self.tipo)