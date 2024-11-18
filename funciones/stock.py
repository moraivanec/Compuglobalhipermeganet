
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
    try:
        assert id_producto in stock, f"Producto con ID {id_producto} no encontrado en el stock."
        assert stock[id_producto] >= cantidad_vendida, f"No hay suficiente stock para vender {cantidad_vendida} unidades del producto {id_producto}."
        
        stock[id_producto] -= cantidad_vendida  # Actualizo el stock
        
        venta = {
            "id_producto": id_producto,
            "cantidad_vendida": cantidad_vendida
        }
        ventas.append(venta)
        
        print(f"Venta registrada exitosamente: {cantidad_vendida} unidades del producto {id_producto}.")
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
    - Registra las entradas de productos al inventario y actualiza el stock.
    
    Precondiciones:
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    - "archivo_entradas" es el archivo JSON donde se registran las entradas de productos.
    
    Postcondiciones:
    - Si no hay productos ingresados, muestra un mensaje indicando que no hay entradas para mostrar.
    - Si hay productos ingresados, muestra un informe en formato JSON con la cantidad total ingresada de cada producto.
    """
    try:
        while True:
            assert id_producto != "", "El ID del producto no puede estar vacío."
            assert cantidad.isdigit(), "La cantidad debe ser un número entero positivo."
            cantidad = int(cantidad)
            assert cantidad > 0, "La cantidad debe ser mayor a cero."

            if id_producto in stock: # Verifico si el producto ya existe en el stock
                stock[id_producto] += cantidad 
            else:
                stock[id_producto] = cantidad
            
            entradas.append({
                "id_producto": id_producto,
                "cantidad_ingresada": cantidad
            })

        if not entradas: # Verifico si hay entradas registradas
            print("No se registraron entradas.")
        else:
            with open(archivo_entradas, 'w', encoding = 'utf-8') as f: 
                json.dump(entradas, f, ensure_ascii = False, indent = 4) # Guardo las entradas en el archivo JSON
            print("Informe de entradas:")
            print(json.dumps(entradas, ensure_ascii = False, indent = 4))
    
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Por favor ingrese un número válido para la cantidad.")
    except Exception as e:
        print(f"Error al registrar las entradas: {e}")


def registrar_salidas(ventas: List[Dict[str, int]], stock: Dict[str, int], archivo_salidas: str) -> None:
    """
    Contrato:
    - Registra las salidas de productos vendidos y actualiza el stock de acuerdo con las ventas registradas.
    
    Precondiciones:
    - "ventas" es una lista de diccionarios donde cada diccionario representa una venta, con el ID del producto y la cantidad vendida.
    - "stock" es un diccionario con los ID de los productos y sus cantidades disponibles.
    - "archivo_salidas" es el archivo JSON donde se registran las salidas de productos.
    
    Postcondiciones:
    - Si no hay ventas registradas, muestra un mensaje indicando que no hay salidas para mostrar.
    - Si hay ventas, muestra un informe en formato JSON con la cantidad total vendida de cada producto.
    """
    try:
        while True:
            assert id_producto != "", "El ID del producto no puede estar vacío."
            assert cantidad.isdigit(), "La cantidad debe ser un número entero positivo."
            cantidad = int(cantidad)
            assert cantidad > 0, "La cantidad debe ser mayor a cero."

            if id_producto in stock:
                if stock[id_producto] >= cantidad:
                    stock[id_producto] -= cantidad  # Actualizo el stock
                else:
                    print(f"No hay suficiente stock para el producto {id_producto}. Solo quedan {stock[id_producto]} unidades!")
                    continue  # No registro la venta si el stock es insuficiente
            else:
                print(f"El producto {id_producto} no existe en el stock.")
                continue

            salidas.append({
                "id_producto": id_producto,
                "cantidad_vendida": cantidad
            })

        if not salidas: # Verifico si hay salidas registradas
            print("No se registraron salidas.")
        else:
            with open(archivo_salidas, 'w', encoding = 'utf-8') as f:
                json.dump(salidas, f, ensure_ascii = False, indent = 4) # Guardo las salidas en el archivo JSON
            print("Informe de salidas:")
            print(json.dumps(salidas, ensure_ascii = False, indent = 4))
    
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Por favor ingrese un número válido para la cantidad.")
    except Exception as e:
        print(f"Error al registrar las salidas: {e}")

