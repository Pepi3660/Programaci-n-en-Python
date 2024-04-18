class Inventario:
    def __init__(self):
        self.productos = []  # inicializamos la lista de productos

    def add_productos(self, producto):
        self.productos.append(producto)
        print("\n\t\tProducto:", producto.name, "agregado exitosamente\n\n")

    def backup(self, nombre_producto, nueva_cantidad):
        for producto in self.productos:  # recorremos el arreglo para cambiar la cantidad del producto
            if producto.name == nombre_producto:
                producto.cant = nueva_cantidad
                print("\n\t\tProducto alterado exitosamente\n\n")

    def delete(self, nombre_producto):
        for producto in self.productos:
            if producto.name == nombre_producto:
                self.productos.remove(producto)
                print("\n\t\tProducto eliminado exitosamente\n\n")
    def is_empty(self):
        return self.productos == []

    def show(self):
        if not self.is_empty():
            print("\n\t\tLista de productos: \n")
            for producto in self.productos:
                print("\t\tNombre: ", producto.name)
                print("\t\tCantidad: ", producto.cant)
                print("\t\tPrecio: ", producto.price)
                print("\n\n")
        else:
            print("\n\t\tLa lista de productos está vacía\n\n")