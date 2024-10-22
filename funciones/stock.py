
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



def registrar_entradas() -> None:
    """
    Contrato:
    - Registra las entradas de productos al inventario.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - Si no hay productos ingresados, muestra un mensaje indicando que no hay entradas para mostrar.
    - Si hay productos ingresados, muestra un informe en formato JSON con la cantidad total ingresada de cada producto.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")


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
