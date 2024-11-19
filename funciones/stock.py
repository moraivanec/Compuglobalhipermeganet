from typing import List, Dict, Any
#from funciones import clientes as cl, productos as pr, stock as st

stock_productos_csv = 'csv\stock_productos_csv.csv'
#st.escribir_csv(productos, stock_productos_csv)

def escribir_csv(productos: List[Dict[str, Any]], stock_productos_csv: str) -> None:
    """
    Escribe la lista de productos en un archivo CSV

    """
    if not productos:
        print("No hay productos para guardar.")
        return

    encabezados = productos[0].keys()
    try:
        with open(stock_productos_csv, mode='a', encoding='utf-8') as archivo_csv:
            archivo_csv.write(','.join(encabezados) + '\n')
            for producto in productos:
                fila = ','.join(str(producto[encabezado]) for encabezado in encabezados)
                archivo_csv.write(fila + '\n')
    except Exception as e:
        print(e)

    print(f"Productos guardados en {stock_productos_csv} correctamente.")


def cargar_stock(stock_productos_csv: str) -> List[Dict[str, Any]]:
    """
    Carga los productos desde un archivo .csv
    Pre: 
    - El archivo existe y está en el formato correcto
    Post:
    - Se devuelve una lista con los productos o devuelve una excepción si hay un error.
    """
    productos = []
    try:
        with open(stock_productos_csv, mode= 'r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                productos.append(fila)
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return productos

def bajo_stock(stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Verifica y muestra los productos que están por debajo del stock mínimo.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - Si no hay productos con bajo stock, muestra un mensaje indicando que no hay productos con bajo stock.
    - Si hay productos por debajo del umbral, muestra un informe en formato JSON con los productos y sus cantidades.
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
    
    
def inventario_actual(stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Muestra el inventario actual de productos y sus cantidades.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - Si el inventario está vacío, muestra un mensaje indicando que el inventario está vacío.
    - Si el inventario no está vacío, muestra el inventario en formato JSON.
    """
    if not stock:
        print("El inventario está vacío.")
        return

    inventario_JSON = js.dumps(stock, indent=2)
    print("Inventario actual en formato JSON:")
    print(inventario_JSON)
    
    
def registrar_venta(ventas: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Registra la venta de productos y actualiza el stock de acuerdo con la venta registrada.
    
    Precondiciones:
    - "ventas" es una lista de diccionarios donde cada diccionario representa una venta, con el ID del producto y la cantidad vendida.
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - Registra la venta en la lista "ventas" y actualiza las cantidades en "stock".
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")



def registrar_entradas(movimientos: list[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Registra las entradas de productos al inventario.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - Si no hay productos ingresados, muestra un mensaje indicando que no hay entradas para mostrar.
    - Si hay productos ingresados, muestra un informe en formato JSON con la cantidad total ingresada de cada producto.
    """
    for movimiento in movimientos:
        print(movimiento)




def registrar_salidas() -> None:
    """
    Contrato:
    - Registra las salidas de productos vendidos.
    
    Precondiciones:
    - "ventas" es una lista de diccionarios donde cada diccionario representa una venta, con el ID del producto y la cantidad vendida.
      
    Postcondiciones:
    - Si no hay ventas registradas, muestra un mensaje indicando que no hay salidas para mostrar.
    - Si hay ventas, muestra un informe en formato JSON con la cantidad total vendida de cada producto.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")
