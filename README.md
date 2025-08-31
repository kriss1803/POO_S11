# Tarea: Sistema Avanzado de Gestión de Inventario
## Descripción:
Desarrollar un sistema avanzado de gestión de inventarios para una tienda, que incorpore las colecciones en POO para un manejo eficiente de los ítems del inventario y almacene la información del inventario en archivos.

## Objetivos:
Aplicar los conceptos de POO para la estructura del programa.
Utilizar colecciones (listas, diccionarios, conjuntos, tuplas) para gestionar los datos del inventario.
Implementar la lectura y escritura de archivos para el almacenamiento persistente del inventario.

## Requisitos:
1. Clase Producto: Debe contener atributos como ID (único), nombre, cantidad y precio. Implementa métodos para obtener y establecer estos atributos.
2. Clase Inventario: Debe utilizar una colección adecuada (p. ej., un diccionario) para almacenar los productos. Implementa métodos para:
   * Añadir nuevos productos.
   * Eliminar productos por ID.
   * Actualizar cantidad o precio de un producto.
   * Buscar y mostrar productos por nombre.
   * Mostrar todos los productos en el inventario.
3. Integración de Colecciones: Utiliza colecciones para optimizar las operaciones del inventario, como búsqueda rápida de productos y manejo eficiente de los datos.
4. Almacenamiento en Archivos: Implementa funciones para guardar y cargar el inventario desde archivos. Esto incluye la serialización de la colección del inventario para su almacenamiento y la deserialización al cargar el programa.
5. Interfaz de Usuario: Crea un menú interactivo en la consola que permita al usuario realizar operaciones sobre el inventario (añadir, eliminar, actualizar, buscar, mostrar).
