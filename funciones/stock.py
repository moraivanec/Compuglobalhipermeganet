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
    productos_bajo_stock = { # Filtro los productos que tienen menos de 10 items
        producto: cantidad
        for producto, cantidad in stock.items()
        if cantidad < umbral_minimo
    }

    if not productos_bajo_stock:
        print("No hay productos con bajo stock.")
        return

    informe_bajo_stock = json.dumps(productos_bajo_stock, indent = 2) # Paso el informe a formato JSON
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
    # Verifico si el inevntario está vacío
    if not stock:
        print("El inventario está vacío.")
        return

    inventario_JSON = json.dumps(stock, indent = 2) # Paso el inventario a formato JSON
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
    try:
        id_producto = input("Ingrese el ID del producto vendido: ")
        cantidad_vendida = input("Ingrese la cantidad vendida: ")
        cantidad_vendida = int(cantidad_vendida) # Paso la cantidad a un entero
        
        # Verifico que el producto exista en el stock y que haya suficiente cantidad para vender
        assert id_producto in stock, f"Producto con ID {id_producto} no encontrado en el stock."
        assert stock[id_producto] >= cantidad_vendida, f"No hay suficiente stock para vender {cantidad_vendida} unidades del producto {id_producto}."
        
        stock[id_producto] -= cantidad_vendida  # Actualizo el stock
        
        venta = {
            "id_producto": id_producto,
            "cantidad_vendida": cantidad_vendida
        }
        ventas.append(venta)
        
        print(f"¡Venta registrada exitosamente!")
        print(f"Stock actualizado: {stock[id_producto]} unidades restantes.")
    
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Por favor ingrese una cantidad válida.")
    except Exception as e:
        print(f"Error al registrar la venta: {e}")


def registrar_entradas(stock: Dict[str, int], archivo_entradas: str) -> None:
    """
    Contrato:
    - Muestra las entradas de productos registradas durante el día.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    - "archivo_entradas" es el archivo JSON donde se registran las entradas de productos.
    
    Postcondiciones:
    - Si no hay productos ingresados, muestra un mensaje indicando que no hay entradas para mostrar.
    - Si hay productos ingresados, muestra un informe en formato JSON con la cantidad total ingresada de cada producto.
    """
    try:
        with open(archivo_entradas, 'r', encoding = 'utf-8') as f: 
            entradas = json.load(f) # Cargo las entradas desde el archivo

        if not entradas:  # Verifico si hay entradas registradas
            print("No se registraron entradas.")
        else:
            print("Informe de entradas:")
            print(json.dumps(entradas, ensure_ascii = False, indent = 4)) # Muestro el informa en formato JSON

    except FileNotFoundError:
        print("El archivo de entradas no existe.")
    except json.JSONDecodeError: # Manejo errores de decodificación JSON
        print("Hubo un error al leer el archivo JSON de entradas.")
    except Exception as e:
        print(f"Error al mostrar las entradas: {e}")


def registrar_salidas(archivo_salidas: str) -> None:
    """
    Contrato:
    - Muestra las salidas de productos registradas.
    
    Precondiciones:
    - "archivo_salidas" es el archivo JSON donde se registran las salidas de productos.
    
    Postcondiciones:
    - Si no hay productos vendidos, muestra un mensaje indicando que no hay salidas para mostrar.
    - Si hay productos vendidos, muestra un informe en formato JSON con la cantidad total vendida de cada producto.
    """
    try:
        with open(archivo_salidas, 'r', encoding = 'utf-8') as f: 
            salidas = json.load(f) # Cargo las salidas desde el archivo

        if not salidas: # Verifico si hay salidas registradas
            print("No se registraron salidas.")
        else:
            print("Informe de salidas:")
            print(json.dumps(salidas, ensure_ascii = False, indent = 4)) # Muestro el infrome en formato JSON

    except FileNotFoundError:
        print("El archivo de salidas no existe.")
    except json.JSONDecodeError: # Manejo errores de decodificación JSON
        print("Hubo un error al leer el archivo JSON de salidas.")
    except Exception as e:
        print(f"Error al mostrar las salidas: {e}")