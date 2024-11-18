def agregar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Carga un nuevo producto en la lista de productos y actualiza el stock.
    
    Precondiciones:
    - "productos" es una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - "stock" es un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - Los productos son cargados en la lista "productos".
    - El stock es actualizado adecuadamente.
    """
    try:
        id_producto = input("Ingrese el ID del producto: ")
        nombre_producto = input("Ingrese el nombre del producto")
        precio = input("Ingrese el precio del producto: ")
        
        # Verifico que los datos no estén vacíos
        assert id_producto != "", "El ID del producto no puede estar vacío."
        assert nombre_producto != "", "El nombre del producto no puede estar vacío."
        assert precio != "", "El precio del producto no puede estar vacío."
        
        # Verifico el formato de los datos
        if not re.match(r"^\d+$", id_producto):
            print("El ID sólo puede tener números.")
            return

        if not re.match(r"^[A-Za-z\s]+$", nombre_producto):
            print("El nombre solo puede tener letras y espacios.")
            return
            
        if not re.match(r"^(0|[1-9]\d*)(\.\d{1,2})?$", precio):
            print("El precio tiene que ser un número positivo que incluya hasta dos decimales.")
            return
        
        precio = float(precio) # Cambio precio a float para asegurarme garantizan que los datos ingresados sean números válidos
        if precio <= 0:
            print("El precio tiene que ser un número positivo.")
            return
        
        nuevo_producto = {
            "id": id_producto,
            "nombre": nombre_producto,
            "precio": precio
        }
        
        # Agrego el nuevo producto a la lista de productos y actualizo el stock
        productos.append(nuevo_producto)
        stock[id_producto] = stock.get(id_producto, 0) # Inicio el stock en 0 si no existe
        print("¡Producto cargado exitosamente!")
        
    except ValueError as e:
        print(f"Error: {e}")
        

def editar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Edita un producto existente en la lista de productos y actualiza el stock si es necesario.
    
    Precondiciones:
    - "productos" es una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - "stock" es un diccionario con los ID de los productos y sus cantidades.

    Postcondiciones:
    - El producto seleccionado es editado con los nuevos valores proporcionados.
    - El stock del producto también puede ser actualizado si es necesario.
    """
    try:
        id_producto = input("Ingrese el ID del producto a editar: ")
        
        # Verifico que el id no esté vacío
        assert id != "", "El ID del producto no puede estar vacío."
        
        # Busco el producto en la lista
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
                
        assert producto_encontrado, "Producto no encontrado"
        
        nuevo_id = input("Ingrese el nuevo ID del producto: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_precio = input("Ingrese el nuevo precio del producto: ")
        
        # Verifico que los nuevos datos no estén vacíos
        assert nuevo_id != "", "El nuevo ID del producto no puede estar vacío."
        assert nuevo_nombre != "", "El nuevo nombre del producto no puede estar vacío."
        assert nuevo_precio != "", "El nuevo precio del producto no puede estar vacío."
        
        # Verifico el formato de los nuevos datos
        if not re.match(r"^\d+$", nuevo_id):
            print("El nuevo ID sólo puede tener números.")
            return
                
        if not re.match(r"^[A-Za-z\s]+$", nuevo_nombre):
            print("El nuevo nombre solo puede tener letras y espacios.")
            return
                
        if not re.match(r"^(0|[1-9]\d*)(\.\d{1,2})?$", nuevo_precio):
            print("El nuevo precio tiene que ser un número positivo que incluya hasta dos decimales.")
            return
                
        nuevo_precio = float(nuevo_precio) # Cambio precio a float para asegurarme garantizan que los datos ingresados sean números válidos
        if nuevo_precio <= 0:
            print("El precio tiene que ser un número positivo.")
            return
                
        # Actualizo el stock solo si el ID del producto se cambia
        if id_producto != nuevo_id:
            stock[nuevo_id] = stock.pop(id_producto, 0) # Muevo el stock del ID anterior al nuevo
                
        producto["id"] = nuevo_id
        producto["nombre"] = nuevo_nombre
        producto["precio"] = nuevo_precio
                
        print("¡Producto editado exitosamente!")
            
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error en los datos proporcionados.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
                

def eliminar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
    """
    Contrato:
    - Elimina un producto existente en la lista de productos y del stock.
    
    Precondiciones:
    - "productos" es una lista de diccionarios, donde cada diccionario representa un producto con su ID, nombre y precio.
    - "stock" es un diccionario con los ID de los productos y sus cantidades.
    
    Postcondiciones:
    - El producto seleccionado es eliminado de la lista de productos.
    - El stock del producto también es eliminado.
    """
    try:
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        
        # Verifico que el id no esté vacío
        assert id_producto != "", "El ID del producto no puede estar vacío."
        
        # Busco el producto en la lista
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
            
        assert producto_encontrado, "Producto no encontrado."
        
        productos.remove(producto_encontrado)  # Elimina el producto de la lista
        stock.pop(id_producto, None) # Elimina el stock del producto
        print("¡Producto eliminado exitosamente!")
        
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        

def consultar_lista_productos() -> None:
    """
    Contrato:
    - Consulta y muestra la lista de productos disponibles.
    
    Precondiciones:
    - Ninguna.
    
    Postcondiciones:
    - Si la lista "productos" está vacía, se imprime en la consola un mensaje indicando que no hay productos registrados.
    - Si hay productos en la lista, se imprime en la consola una tabla con los detalles de cada producto: ID, Nombre y Precio.
    """
    separador = ';'
    try:
        with open('productos.csv', 'rt', encoding = 'utf-8') as archivo:
            for linea in archivo: # Método iterando (lectura línea por línea) elementos del archivo
                id_producto, nombre, precio = linea.rstrip().split(separador)
                productos.append({"ID": id_producto, "Nombre": nombre, "Precio": precio})

        if not productos:
            print("No hay productos registrados.")
        else:
            encabezados = ["ID", "Nombre", "Precio"]
            print(tabulate(productos, headers = encabezados, tablefmt = "grid")) # Formateo la salida usando tabulate

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as e:
        print(f'Error en los datos: {e}')
        



