import os
import json as js
from os import system, name
from tabulate import tabulate
from typing import List, Dict, Any


# FUNCIÓN: limpiar_pantalla
def limpiar_pantalla() -> None:
    """
    Precondiciones:
    - El sistema operativo debe ser compatible con los comandos "cls" (Windows) o "clear" (Unix, Linux, Mac).
    - Los módulos 'os.system' y 'os.name' deben estar disponibles.

    Postcondiciones:
    - La pantalla de la consola se limpia.
    - En sistemas Windows, se ejecuta el comando 'cls'.
    - En sistemas Unix (Linux y Mac), se ejecuta el comando 'clear'.
    """
    if name == "nt":
        # Windows
        system("cls")
    else:
        # Linux y Mac
        system("clear")


# FUNCIÓN: mostrar_menu
def mostrar_menu(opciones: List[str]) -> None:
    """
    Precondiciones:
    - 'opciones' debe ser una lista no vacía.

    Postcondiciones:
    - Muestra un menú de opciones en la consola, con cada opción numerada.
    - Se incluye una opción "0. Salir" al principio del menú.
    """
    print("\nGestión de Inventario y Clientes")
    tabla = [[i + 1, opcion] for i, opcion in enumerate(opciones)]
    print(tabulate(tabla, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
    print("0. Salir")


# FUNCIÓN: seleccionar_opcion
def seleccionar_opcion(opciones: List[str]) -> int:
    """
    Precondiciones:
    - Se asume que el usuario introducirá un número entero válido.

    Postcondiciones:
    - Devuelve un número entero que representa la opción seleccionada por el usuario.
    - El número devuelto estará en el rango de 0 a 12.
    - Continúa solicitando al usuario hasta que se proporciona una opción válida.
    """
    while True:
        opcion = int(input("\nSeleccione una opción: "))
        if 0 <= opcion <= len(opciones):
            return opcion
        print("Por favor, elija una opción válida.")


# FUNCIÓN: cargar_producto
def cargar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'productos' debe ser una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - Los productos serán cargados en el sistema.
    - El stock será actualizado adecuadamente.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: editar_producto
def editar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'productos' debe ser una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - El producto seleccionado será editado con los nuevos valores proporcionados.
    - El stock del producto también podrá ser actualizado si es necesario.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: eliminar_producto
def eliminar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'productos' debe ser una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - El producto seleccionado será eliminado de la lista de productos.
    - El stock del producto también será eliminado.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: consultar_lista_productos
def consultar_lista_productos() -> None:
  """
  Precondiciones:
  - 'productos' debe ser una lista de diccionarios, donde cada diccionario representa un producto con sus atributos.

  Postcondiciones:
  - Si la lista 'productos' está vacía, se imprime en la consola un mensaje indicando que no hay productos registrados.
  - Si hay productos en la lista, se imprime en la consola una tabla con los detalles de cada producto: ID, Nombre y Precio.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: agregar_cliente
def agregar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Precondiciones:
    - 'clientes' debe ser una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - La función deberá agregar un nuevo cliente a la lista de clientes después de solicitar la información necesaria al usuario.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: editar_cliente
def editar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Precondiciones:
    - 'clientes' debe ser una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - La función deberá permitir seleccionar un cliente y actualizar su información en la lista de clientes después de solicitar los nuevos datos al usuario.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: eliminar_cliente
def eliminar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Precondiciones:
    - 'clientes' debe ser una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.

    Postcondiciones:
    - La función deberá permitir seleccionar un cliente de la lista y eliminarlo, actualizando la lista de clientes en consecuencia.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: consultar_lista_clientes
def consultar_lista_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    Precondiciones:
    - 'clientes' debe ser una lista de diccionarios donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - La función deberá mostrar la lista de clientes en la consola.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: bajo_stock
def bajo_stock(stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - Si no hay productos con bajo stock, se muestra un mensaje indicando que no hay productos con bajo stock.
    - Si hay productos por debajo del umbral, se muestra un informe en formato JSON con los productos y sus cantidades.
    """
    umbral_minimo = 10
    productos_bajo_stock = {
        producto: cantidad
        for producto, cantidad in stock.items()
        if cantidad < umbral_minimo
    }

    if not productos_bajo_stock:
        print("No hay productos con bajo stock.")
        return

    informe_bajo_stock = js.dumps(productos_bajo_stock, indent=2)
    print("Productos con bajo stock en formato JSON:")
    print(informe_bajo_stock)


# FUNCIÓN: registrar_venta
def registrar_venta(ventas: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'ventas' debe ser una lista de diccionarios donde cada diccionario representa una venta, con el ID del producto y la cantidad vendida.
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - La función debería registrar la venta en la lista de ventas y actualizar las cantidades en el stock de acuerdo con la venta registrada.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: inventario_actual
def inventario_actual(stock: Dict[str, int]) -> None:
    """
    Precondiciones:
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - Si el inventario está vacío, se muestra un mensaje indicando que el inventario está vacío.
    - Si el inventario no está vacío, se muestra el inventario en formato JSON.
    """
    if not stock:
        print("El inventario está vacío.")
        return

    inventario_JSON = js.dumps(stock, indent=2)
    print("Inventario actual en formato JSON:")
    print(inventario_JSON)


# FUNCIÓN: registrar_entradas
def registrar_entradas() -> None:
    """
    Precondiciones:
    - 'stock' debe ser un diccionario con los ID de los productos y sus cantidades.
    - 'entradas' debe ser una lista de diccionarios donde se registrarán las entradas.

    Postcondiciones:
    - Registra el ID del producto, la cantidad ingresada y la fecha en la lista de entradas.
    - Si no hay productos ingresados, se muestra un mensaje indicando que no hay entradas para mostrar.
    - Si hay productos ingresados, se muestra un informe en formato JSON con la cantidad total ingresada de cada producto.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: registrar_salidas
def registrar_salidas() -> None:
    """
    Precondiciones:
    - 'ventas' debe ser una lista de diccionarios donde cada diccionario representa una venta, con el ID del producto y la cantidad vendida.
      
    Postcondiciones:
    - La función registra las salidas (ventas) por producto.
    - Si no hay ventas registradas, se muestra un mensaje indicando que no hay salidas para mostrar.
    - Si hay ventas, se muestra un informe en formato JSON con la cantidad total vendida de cada producto.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Ejecuta el menú principal, permitiendo al usuario interactuar con el sistema.
    - El estado de las listas de productos, stock, ventas y clientes se mantiene.
    - No tiene parámetros de retorno.
    """
    opciones = [
        "Añadir producto",
        "Editar producto",
        "Eliminar producto",
        "Consultar lista de productos",
        "Agregar cliente",
        "Editar cliente",
        "Eliminar cliente",
        "Consultar lista de clientes",
        "Registrar venta",
        "Ver inventario actual",
        "Informe de entradas",
        "Informe de salidas",
    ]
    productos: List[Dict[str, Any]] = []
    stock: Dict[str, int] = {}
    ventas: List[Dict[str, Any]] = []
    clientes: List[Dict[str, Any]] = []

    while True:
        mostrar_menu(opciones)
        opcion = seleccionar_opcion(opciones)
        match opcion:
            case 0:
                print("Saliendo del sistema...")
                break
            case 1:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                agregar_producto(productos, stock)
            case 2:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                editar_producto(productos, stock)
            case 3:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                eliminar_producto(productos, stock)
            case 4:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                consultar_lista_productos(productos)
            case 5:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                agregar_cliente(clientes)
            case 6:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                editar_cliente(clientes)
            case 7:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                eliminar_cliente(clientes)
            case 8:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                consultar_lista_clientes(clientes)
            case 9:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                registrar_venta(ventas, stock)
            case 10:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                inventario_actual(stock)
            case 11:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                registrar_entradas(stock)
            case 12:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                registrar_salidas(ventas)

if __name__ == "__main__":
    main()