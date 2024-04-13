class Inventario:
    def __init__(self):
        self.productos = []  #inicializamos la lista de productos
    
    def add_productos(self, producto):
        self.producto.append(producto)
        print("Product: ", producto, "add successfully")

    def backup(self, nombre_producto, nueva_cantidad):
        for producto in self.productos:         #recorremos el arreglo para cambiar la cantidad del producto
            if producto == nombre_producto:
                producto.cantidad = nueva_cantidad 
                print("Product alter succesfully")

    def delete(self, nombre_producto):
        for producto in self.productos:
            if(producto == nombre_producto):
                self.productos.remove(producto)
                print("Producto delete succesfully")
    
    def is_empty(self):
        return self.productos == []

    def show(self):
        for producto in self.productos:
            print(producto)
            if not self.is_empty():
                print(producto)
            else:
                print("List products is empty")
