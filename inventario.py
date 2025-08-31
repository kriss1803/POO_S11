import json

# ----------------------------------------
# Clase Producto
# ----------------------------------------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto  # ID único del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para actualizar atributos
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representación legible del producto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Serialización para almacenamiento en archivo
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    # Creación de objeto desde diccionario
    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


# ----------------------------------------
# Clase Inventario
# ----------------------------------------
class Inventario:
    def __init__(self):
        # Diccionario para un acceso rápido por ID
        self.productos = {}

    # Añadir producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            eliminado = self.productos.pop(id_producto)
            print(f"Producto '{eliminado.get_nombre()}' eliminado.")
        else:
            print("Error: No existe un producto con ese ID.")

    # Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: No existe un producto con ese ID.")

    # Buscar y mostrar productos por nombre
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todos(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("El inventario está vacío.")

    # Guardar inventario en archivo
    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w") as file:
                # Convertimos cada producto a diccionario
                json.dump([p.to_dict() for p in self.productos.values()], file, indent=4)
            print(f"Inventario guardado en '{nombre_archivo}' correctamente.")
        except Exception as e:
            print(f"Error al guardar archivo: {e}")

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as file:
                datos = json.load(file)
                self.productos = {d["id"]: Producto.from_dict(d) for d in datos}
            print(f"Inventario cargado desde '{nombre_archivo}' correctamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'.")
        except Exception as e:
            print(f"Error al cargar archivo: {e}")


# ----------------------------------------
# Interfaz de usuario en consola
# ----------------------------------------
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n=== Sistema de Gestión de Inventario ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para no cambiar): ")
            precio = input("Nuevo precio (Enter para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
        elif opcion == "0":
            inventario.guardar_en_archivo("inventario.json")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
