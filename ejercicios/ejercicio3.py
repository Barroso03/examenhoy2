class Producto():
    print("Ejercicio3:")
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    def __str__(self):
        return "Codigo: {}, Nombre: {}, Precio: {}, Tipo: {}".format(self.codigo, self.nombre, self.precio, self.tipo)
    def precio_final(self):
        if self.tipo == "A":
            return "Precio final: {}".format(self.precio * 1.21)
        elif self.tipo == "B":
            return "Precio final: {}".format(self.precio * 1.10)
        else:
            return "Precio final: {}".format(self.precio)
    def crear_producto():
      
      codigo = input("Introduce el codigo del producto: ")
      nombre = input("Introduce el nombre del producto: ")
      precio = float(input("Introduce el precio del producto: "))
      tipo = input("Introduce el tipo del producto: ")
      print("Producto creado",Producto(codigo, nombre, precio, tipo))
      print(Producto.precio_final(Producto(codigo, nombre, precio, tipo)))