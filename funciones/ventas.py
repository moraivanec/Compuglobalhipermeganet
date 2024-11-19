import json
from datetime import datetime
from typing import List, Dict, Any

# Nombre del archivo donde se guardarán las ventas
archivo_ventas = 'ventas.json'

def cargar_ventas() -> List[Dict[str, Any]]:
    """Carga las ventas desde el archivo JSON."""
    try:
        with open(archivo_ventas, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devolvemos una lista vacía

def guardar_ventas(ventas: List[Dict[str, Any]]) -> None:
    """Guarda las ventas en el archivo JSON."""
    with open(archivo_ventas, 'w') as archivo:
        json.dump(ventas, archivo, indent=4)

def registrar_venta(ventas: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """Registra una nueva venta."""
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    
    # Verificar si hay suficiente stock
    if stock.get(producto, 0) >= cantidad:
        precio = float(input("Ingrese el precio del producto: "))
        nueva_venta = {
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Cargar ventas existentes y agregar la nueva venta
        ventas = cargar_ventas()
        ventas.append(nueva_venta)
        guardar_ventas(ventas)
        
        # Actualizar el stock
        stock[producto] -= cantidad
        print("Venta registrada exitosamente.")
    else:
        print("No hay suficiente stock para realizar la venta.")

