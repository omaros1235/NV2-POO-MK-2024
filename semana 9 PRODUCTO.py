class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto.
        :param precio: Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID sea único antes de añadir.
        :param producto: Objeto de tipo Producto a añadir.
        """
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        :param id: ID del producto a eliminar.
        """
        for prod in self.productos:
            if prod.get_id() == id:
                self.productos.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto existente por su ID.
        :param id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad del producto (opcional).
        :param precio: Nuevo precio del producto (opcional).
        """
        for prod in self.productos:
            if prod.get_id() == id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos en el inventario por nombre.
        Permite buscar nombres similares.
        :param nombre: Nombre del producto a buscar.
        """
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            for prod in self.productos:
                print(prod)
        else:
            print("No hay productos en el inventario.")

def menu():
    """
    Muestra el menú principal del sistema de gestión de inventarios.
    """
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    """
    Función principal que controla la interacción del usuario con el sistema.
    """
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")
            inventario.actualizar_producto(id, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()