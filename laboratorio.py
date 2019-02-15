
class Producto():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Medicamento(Producto):
    def __init__(self,nombre, cantidad, precio, composicion, porcentaje):
        super().__init__(nombre, cantidad, precio)
        self.composicion = composicion
        self.porcentaje = porcentaje

class Laboratorio():
    def __init__(self, nombre, Producto1, Producto2):
        self.nombre = nombre
        self.producto1 = Producto1
        self.producto2 = Producto2

gel = Producto("gel de baño",1, 2)
antibiotico = Medicamento("zinat", 1, 5, "cloperastina", 0.5)
normon = Laboratorio("Normon", gel, antibiotico)

print("El laboratorio", normon.nombre, "tiene", normon.producto1.nombre ," y ", normon.producto2.nombre)
print("La composición de", normon.producto2.nombre,"es", normon.producto2.composicion, "en un porcentaje de", normon.producto2.porcentaje)
