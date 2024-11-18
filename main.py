import os
import json as js
from os import system, name
from tabulate import tabulate
from typing import List, Dict, Any
from funciones import clientes as cl, productos as pr, stock as st

def limpiar_pantalla() -> None:
    """
    Contrato:
    - Limpia la pantalla de la consola.
    
    Precondiciones:
    - El sistema operativo es compatible con los comandos "cls" (Windows) o "clear" (Unix, Linux, Mac).
    - Los módulos 'os.system' y 'os.name' están disponibles.

    Postcondiciones:
    - La pantalla de la consola se limpia.
    """
    if name == "nt":
        # Windows
        system("cls")
    else:
        # Linux y Mac
        system("clear")
        

def mostrar_menu(opciones: List[str]) -> None:
    """
    Contrato:
    - Muestra un menú de opciones en la consola.
    
    Precondiciones:
    - "opciones" es una lista no vacía.

    Postcondiciones:
    - Muestra un menú de opciones en la consola, con cada opción numerada.
    """
    print("\nGestión de Inventario y Clientes")
    tabla = [[i + 1, opcion] for i, opcion in enumerate(opciones)]
    print(tabulate(tabla, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
    print("0. Salir")
    

def seleccionar_opcion(opciones: List[str]) -> int:
    """
    Contrato:
    - Solicita al usuario que seleccione una opción del menú y la devuelve.
    
    Precondiciones:
    - "opciones" es una lista no vacía.

    Postcondiciones:
    - Devuelve un número entero (0 a 12) según la opción seleccionada por el usuario.
    - Si la opción está fuera del rango continúa solicitando al usuario hasta que se elija una opción válida.
    """
    while True:
        opcion = int(input("\nSeleccione una opción: "))
        if 0 <= opcion <= len(opciones):
            return opcion
        print("Por favor, elija una opción válida.")

def main() -> None:
    """
    Contrato:
    - Menú que permite al usuario seleccionar opciones para gestionar el inventario y los clientes.
    
    Precondiciones:
    - Ninguna.

    Postcondiciones:
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
    entradas = []
    salidas = []

    while True:
        mostrar_menu(opciones)
        opcion = seleccionar_opcion(opciones)
        match opcion:
            case 0:
                print("Saliendo del sistema...")
                break
            case 1:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                pr.agregar_producto(productos, stock)
            case 2:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                pr.editar_producto(productos, stock)
            case 3:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                pr.eliminar_producto(productos, stock)
            case 4:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                pr.consultar_lista_productos(productos)
            case 5:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                cl.agregar_cliente(clientes)
            case 6:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                cl.editar_cliente(clientes)
            case 7:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                cl.eliminar_cliente(clientes)
            case 8:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                cl.consultar_lista_clientes(clientes)
            case 9:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                st.registrar_venta(ventas, stock)
            case 10:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                st.inventario_actual(stock)
            case 11:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                st.registrar_entradas(stock)
            case 12:
                print(f"Has seleccionado la opción: {opciones[opcion - 1]}")
                st.registrar_salidas(ventas)

if __name__ == "__main__":
    main()