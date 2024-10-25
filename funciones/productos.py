def cargar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int]) -> None:
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
        assert id_producto != "", "El ID del producto no puede estar vacío."
        assert nombre_producto != "", "El nombre del producto no puede estar vacío."
        assert precio != "", "El precio del producto no puede estar vacío."
        
        if not re.match(r"^\d+$", id_producto):
            print("El ID sólo puede tener números.")
            return

        if not re.match(r"^[A-Za-z\s]+$", nombre_producto):
            print("El nombre solo puede tener letras y espacios.")
            return
            
        if not re.match(r"^(0|[1-9]\d*)(\.\d{1,2})?$", precio):
            print("El precio tiene que ser un número positivo que incluya hasta dos decimales.")
            return
            
        if precio <= 0:
            print("El precio tiene que ser un número positivo.")
            return
        
        nuevo_producto = {
            "id": id_producto,
            "nombre": nombre_producto,
            "precio": precio
        }
        
        productos.append(nuevo_producto)
        
        # Inicio el stock en 0 si no existe
        stock[id] = stock.get(id, 0)
        print("¡Producto cargado exitosamente!")
        
    except ValueError:
        print("Error!")
        

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
        assert id != "", "El ID del producto no puede estar vacío."
        
        producto_encontrado = False
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = True
                
        assert producto_encontrado, "Producto no encontrado"
                
                assert id_producto_editado != "", "El nuevo ID del producto no puede estar vacío."
                assert nombre_producto_editado != "", "El nuevo nombre del producto no puede estar vacío."
                assert precio_editado != "", "El nuevo precio del producto no puede estar vacío."
                
                if not re.match(r"^\d+$", id_producto_editado):
                    print("El nuevo ID sólo puede tener números.")
                    return
                
                if not re.match(r"^[A-Za-z\s]+$", nombre_producto_editado):
                    print("El nuevo nombre solo puede tener letras y espacios.")
                    return
                
                if not re.match(r"^(0|[1-9]\d*)(\.\d{1,2})?$", precio_editado):
                    print("El nuevo precio tiene que ser un número positivo que incluya hasta dos decimales.")
                    return
                
                if precio <= 0:
                    print("El precio tiene que ser un número positivo.")
                    return
                
                # Actualizo el stock solo si el ID del producto se cambia
                if id_producto != id_producto_editado:
                    stock[id_producto_editado] = stock.pop(id_producto, 0) # Muevo el stock del ID anterior al nuevo
                
                producto["id"] = id_producto_editado
                producto["nombre"] = nombre_producto_editado
                producto["precio"] = precio_editado
                
                print("¡Producto editado exitosamente!")
                break
            
    except ValueError:
        print("Error!")
                

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
        assert id_producto != "", "El ID del producto no puede estar vacío."
        
        producto_encontrado = False
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = True
                productos.remove(producto)  # Eliminar el producto de la lista
                print("¡Producto eliminado exitosamente!")
                break
        
        assert producto_encontrado, "Producto no encontrado."
    
    except ValueError:
        print("Error!")

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
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")