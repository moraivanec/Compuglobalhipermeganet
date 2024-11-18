def agregar_cliente(clientes: List[Dict[str, str]], archivo: str) -> None:
    """
    Contrato:
    - Agrega un nuevo cliente a la lista de clientes y lo guarda en un archivo JSON.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    - "archivo" es el nombre del archivo JSON donde se almacenan los datos de los clientes.
    
    Postcondiciones:
    - Agrega un nuevo cliente a la lista de "clientes" y guarda la lista actualizada en el archivo JSON.
    """
    try:
        assert nombre_cliente != "", "El nombre no puede estar vacío."
        assert dni != "", "El DNI no puede estar vacío."
        assert correo != "", "El correo no puede estar vacío."
        
        if not re.match(r"^[A-Za-z\s]+$", nombre_cliente):
            print("El nombre solo puede tener letras y espacios.")
            return
            
        if not re.match(r"^\d{8}$", dni):
            print("El DNI debe tener exactamente 8 dígitos.")
            return
            
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
            print("El correo no es válido.")
            return
        
        nuevo_cliente = {
            "nombre": nombre_cliente,
            "dni": dni,
            "correo": correo
        }
        
        clientes.append(nuevo_cliente)
        
        with open(archivo, 'w', encoding = 'utf-8') as f:
            json.dump(clientes, f, indent = 4, ensure_ascii = False) # Guardo la lista actualizada en el archivo JSON
        
        print("¡Cliente agregado exitosamente!")

    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error en los datos proporcionados.")
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
        assert dni != "", "El DNI del cliente a editar no puede estar vacío."
        
        # Busco al cliente en la lista y lo edito si se encuentra
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["dni"] == dni:
                cliente_encontrado = True
                
        assert cliente_encontrado, "Cliente no encontrado."
                
                assert nombre_cliente_editado != "", "El nuevo nombre no puede estar vacío."
                assert dni_editado != "", "El nuevo DNI no puede estar vacío."
                assert correo_editado != "", "El nuevo correo no puede estar vacío."
                 
                if not re.match(r"^[A-Za-z\s]+$", nombre_cliente_editado):
                    print("El nuevo nombre solo puede tener letras y espacios.")
                    return
                    
                if not re.match(r"^\d{8}$", dni_editado):
                    print("El nuevo DNI debe tener exactamente 8 dígitos.")
                    return
            
                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo_editado):
                    print("El nuevo correo no es válido.")
                    return
                    
                # Actualizo los datps
                cliente["nombre"] = nombre_cliente_editado
                cliente["dni"] = dni_editado
                cliente["correo"] = correo_editado
                print("¡Cliente editado exitosamente!")
                break
                
    except ValueError:
        print("Error!")
                    
import re
from typing import List, Dict

def eliminar_cliente(clientes: List[Dict[str, str]], archivo: str) -> None:
    """
    Contrato:
    - Elimina un cliente existente en la lista de clientes.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo.
    - "archivo" es el nombre del archivo donde se guardan los datos de los clientes.
    
    Postcondiciones:
    - El cliente seleccionado es eliminado de la lista de clientes y se guarda la lista actualizada en el archivo JSON.
    """
    try:
        assert dni != "", "El DNI no puede estar vacío."
        
        cliente_encontrado = None
        
        for cliente in clientes:
            if cliente["dni"] == dni:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado is None:
            print("Cliente no encontrado.")
            return
        
        print(f"Cliente encontrado: {cliente_encontrado['nombre']} - DNI: {cliente_encontrado['dni']}")
        confirmacion = input(f"¿Está seguro que desea eliminar al cliente {cliente_encontrado['nombre']}? (s/n): ").lower() # Confirmo los datos de eliminación
        
        if confirmacion == 's':
            clientes.remove(cliente_encontrado)  # Elimino el cliente de la lista
            with open(archivo, 'w', encoding = 'utf-8') as f:
                json.dump(clientes, f, indent = 4, ensure_ascii = False) # Guardo la lista actualizada en el archivo JSON
            print("¡Cliente eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


import json
from typing import List, Dict
from tabulate import tabulate

def consultar_lista_clientes(archivo: str) -> None:
    """
    Contrato:
    - Consulta y muestra la lista de clientes registrados.
    
    Precondiciones:
    - "archivo" es el nombre del archivo JSON donde se almacenan los datos de los clientes.
    
    Postcondiciones:
    - Si la lista "clientes" está vacía, se imprime en la consola un mensaje indicando que no hay clientes registrados.
    - Si hay clientes en la lista, se imprime en la consola una tabla con los detalles de cada uno.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            clientes = json.load(f) # Abro el archivo JSON y cargo los datos

        if not clientes:
            print("No hay clientes registrados.")
        else:
            tabla_clientes = []  # Creo una lista de los clientes para mostrar en tabla
            for cliente in clientes:
                tabla_clientes.append([cliente['nombre'], cliente['dni'], cliente['correo']])
            print(tabulate(tabla_clientes, headers=["Nombre", "DNI", "Correo"], tablefmt="grid"))
    
    except FileNotFoundError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("Hubo un error al leer el archivo JSON.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

