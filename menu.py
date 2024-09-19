# Sistema de Gestión de Inventario y Clientes de tienda de artículos computación

import os
import json as js
from os import system, name
from tabulate import tabulate
from typing import List, Dict, Any


# FUNCIÓN: limpiar_pantalla
def limpiar_pantalla() -> None:
    """
    CONTRATO:
    PRE:
    Ninguno
    POST:
    Limpia la pantalla de la consola para sistemas operativos de Windows (cls) y Unix (clear).
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
    CONTRATO:
    PRE:
    opciones en una lista de str no vacía.
    POST:
    Muestra el menú de opciones.
    """
    print("\nGestión de Inventario y Clientes")
    tabla = [[i + 1, opcion] for i, opcion in enumerate(opciones)]
    print(tabulate(tabla, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
    print("0. Salir")


# FUNCIÓN: seleccionar_opcion
def seleccionar_opcion(opciones: List[str]) -> int:
    """
    CONTRATO:
    PRE:
    opciones en una lista de str no vacía.
    POST:
    Retorna una opción válida seleccionada por el usuario (int).
    """
    while True:
        opcion = int(input("\nSeleccione una opción: "))
        if 0 <= opcion <= len(opciones):
            return opcion
        print("Por favor, elija una opción válida.")


# FUNCIÓN: cargar_productos
def cargar_productos(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        productos en una lista de diccionarios.
    POST:
        Carga de productos en el sistema.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: editar_producto
def editar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        productos en una lista de diccionarios.
    POST:
        Edita un producto en el sistema.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: eliminar_producto
def eliminar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        productos en una lista de diccionarios.
    POST:
        Elimina un producto del sistema.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: inventario_actual
# FUNCIÓN: inventario_actual
def inventario_actual(stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        stock es un diccionario con los productos y sus cantidades.
    POST:
        Muestra el inventario actual en formato JSON con indentación de 2 espacios.
    """
    if not stock:
        print("El inventario está vacío.")
        return

    inventario_JSON = js.dumps(stock, indent=2)
    print("Inventario actual en formato JSON:")
    print(inventario_JSON)


# FUNCIÓN: generar_informe
def generar_informe(stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        stock es un diccionario con los productos y sus cantidades.
    POST:
        Genera un informe en formato JSON del inventario actual.
    """
    if not stock:
        print("El inventario está vacío.")
        return

    informe_JSON = js.dumps(stock, indent=2)
    print("Informe de inventario actual en formato JSON:")
    print(informe_JSON)


# FUNCIÓN: bajo_stock
def bajo_stock(stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        stock es un diccionario con los productos y sus cantidades.
    POST:
        Muestra los productos con cantidades por debajo del umbral mínimo especificado.
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


# FUNCIÓN: registrar_entrada
def registrar_entrada(stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        stock en un diccionario de productos y cantidades.
    POST:
        Registra la entrada de productos al inventario.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: registrar_venta
def registrar_venta(ventas: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    CONTRATO:
    PRE:
        ventas en una lista de diccionarios.
    POST:
        Registra una venta y actualiza el inventario.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: consultar_lista_clientes
def consultar_lista_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    CONTRATO:
    PRE:
        clientes en una lista de diccionarios.
    POST:
        Muestra la lista de clientes.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: agregar_cliente
def agregar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    CONTRATO:
    PRE:
        clientes en una lista de diccionarios.
    POST:
        Agrega un nuevo cliente a la lista.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: editar_clientes
def editar_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    CONTRATO:
    PRE:
        clientes en una lista de diccionarios.
    POST:
        Edita un cliente en la lista.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


# FUNCIÓN: eliminar_clientes
def eliminar_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    CONTRATO:
    PRE:
        clientes en una lista de diccionarios.
    POST:
        Elimina un cliente de la lista.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


def main() -> None:
    """
    CONTRATO:
    PRE:
        Ninguno
    POST:
        Ejecuta el menú principal y gestiona las opciones.
        No tiene parámetros de retorno.
    """
    opciones = [
        "Añadir producto",
        "Editar producto",
        "Eliminar producto",
        "Ver informe de inventario actual",
        "Ver informe de movimientos",
        "Ver productos con bajo stock",
        "Registrar entrada de producto",
        "Registrar salida de producto",
        "Consultar lista de clientes",
        "Agregar cliente",
        "Editar cliente",
        "Eliminar cliente",
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
                cargar_productos(productos, stock)
            case 2:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                editar_producto(productos, stock)
            case 3:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                eliminar_producto(productos, stock)
            case 4:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                inventario_actual(stock)
            case 5:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                generar_informe(stock)
            case 6:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                bajo_stock(stock)
            case 7:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                registrar_entrada(stock)
            case 8:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                registrar_venta(ventas, stock)
            case 9:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                consultar_lista_clientes(clientes)
            case 10:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                agregar_cliente(clientes)
            case 11:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                editar_clientes(clientes)
            case 12:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                eliminar_clientes(clientes)


if __name__ == "__main__":
    main()
