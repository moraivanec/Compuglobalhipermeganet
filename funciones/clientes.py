from typing import List, Dict, Any
from tabulate import tabulate 

def agregar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Agrega un nuevo cliente a la lista de clientes.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - Agrega un nuevo cliente a la lista de "clientes"..
    """
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        dni = input("Ingrese el DNI del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        """"
        # Validación simple
        """
        if not nombre or not dni or not correo:
            raise ValueError("Todos los campos son obligatorios.")

        nuevo_cliente = {
            "nombre": nombre,
            "dni": dni,
            "correo": correo
        }
        clientes.append(nuevo_cliente)
        print("Cliente agregado exitosamente.")
    except ValueError as ve:
            print(f"Error: {ve}")
    except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


def editar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Edita un cliente existente en la lista de clientes. 
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo.
    
    Postcondiciones:
    - El cliente seleccionado es editado con los nuevos valores proporcionados.
    """
    try:
        dni = input("Ingrese el DNI del cliente a editar: ")
        for cliente in clientes:
            if cliente["dni"] == dni:
                nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                nuevo_correo = input("Ingrese el nuevo correo (deje en blanco para no cambiar): ")

                if nuevo_nombre:
                    cliente["nombre"] = nuevo_nombre
                if nuevo_correo:
                    cliente["correo"] = nuevo_correo

                print("Cliente editado exitosamente.")
                return
        raise ValueError("Cliente no encontrado.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def eliminar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Elimina un cliente existente en la lista de clientes.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo.
    
    Postcondiciones:
    - El cliente seleccionado es eliminado de la lista de clientes.
    """
    try:
        dni = input("Ingrese el DNI del cliente a eliminar: ")
        for i, cliente in enumerate(clientes):
            if cliente["dni"] == dni:
                del clientes[i]
                print("Cliente eliminado exitosamente.")
                return
        raise ValueError("Cliente no encontrado.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def consultar_lista_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Consulta y muestra la lista de clientes registrados.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - Si la lista "clientes" está vacía, se imprime en la consola un mensaje indicando que no hay clientes registrados.
    - Si hay clientes en la lista, se imprime en la consola una tabla con los detalles de cada uno.
    """
    try:
        if not clientes:
            raise ValueError("No hay clientes registrados.")

        print("Lista de clientes:")
        tabla = [[cliente["nombre"], cliente["dni"], cliente["correo"]] for cliente in clientes]
        print(tabulate(tabla, headers=["Nombre", "DNI", "Correo"], tablefmt="fancy_grid"))
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

