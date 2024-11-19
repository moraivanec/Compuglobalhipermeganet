from typing import List, Dict, Any
from tabulate import tabulate
from funciones import clientes as cl, stock as st, ventas as vt
from datetime import datetime



def cargar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int],nuevo_producto: Dict[str, Any], movimientos: List[Dict[str, Any]]) -> None:
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
    #for producto in productos:
    #        if producto['ID'] == nuevo_producto['ID']:
    #           print(f"El producto con ID {nuevo_producto['ID']} ya existe.")
    #            return
    for producto in productos:
        #if 'id' in producto and producto['id'] == nuevo_producto['id']:
        if 'ID' in producto and producto['ID'] == nuevo_producto['id']:
            print(f"El producto con ID {nuevo_producto['id']} ya existe.")
            return
    """
    Agrega el nuevo producto a la lista
    """
    productos.append(nuevo_producto)
    st.escribir_csv(productos, 'csv/stock_productos_csv.csv')

    """
    Actualiza el stock
    """
    stock[nuevo_producto['id']] = nuevo_producto.get('cantidad', 0) 
    print(f"El producto {nuevo_producto['nombre']} fue añadido exitosamente! :)")
    movimientos.append({
        "producto": nuevo_producto,
        "fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "tipo": "Entrada"
    })



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
    id_producto = input("Ingrese el ID del producto a editar: ")
    nuevos_datos = {}

    for producto in productos:
        if producto['ID'] == id_producto:
            nuevo_nombre = input("Ingrese el nuevo nombre (deje vacío para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                producto['precio'] = float(nuevo_precio)
            if nueva_cantidad:
                producto['cantidad'] = int(nueva_cantidad)
                stock[id_producto] = producto['cantidad']  # Actualiza el stock

            print(f"Producto {id_producto} editado con éxito.")
            st.escribir_csv(productos, 'csv/stock_productos_csv.csv')
            return
    print(f"Producto con ID {id_producto} no encontrado.")

def eliminar_producto(productos: List[Dict[str, Any]], stock: Dict[str, int], movimientos: [Dict[str, Any]]) -> None:
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
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    
    for i, producto in enumerate(productos):
        #if producto['id'] == id_producto:
        if producto['ID'] == id_producto:
            del productos[i]
            del stock[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
            movimientos.append({
                "producto": productos[i],
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "tipo": "Salida"
            })
            return
    
    print(f"Producto con ID {id_producto} no encontrado.")



def consultar_lista_productos(productos: List[Dict[str, Any]], stock_productos_csv: str) -> None:
    """
    Contrato:
    - Consulta y muestra la lista de productos disponibles.
    
    Precondiciones:
    - Ninguna.
    
    Postcondiciones:
    - Si la lista "productos" está vacía, se imprime en la consola un mensaje indicando que no hay productos registrados.
    - Si hay productos en la lista, se imprime en la consola una tabla con los detalles de cada producto: ID, Nombre y Precio.
    """
    try:
        with open(stock_productos_csv, 'r', encoding = 'utf-8') as file:
            """
            reader = DictReader(file)
            for row in reader:
                
                row = {key.replace('\ufeff', '').strip(): value for key, value in row.items()}
                
                row['Precio'] = int(row['Precio'])
                productos.append(row)

                print(row)
            """
            headers = file.readline().strip().split(',')
            headers = [header.replace('\ufeff', '').strip() for header in headers]  # Limpiar encabezados

            for line in file:
                # Leer cada línea y dividirla en columnas
                values = line.strip().split(',')
                # Crear un diccionario para el producto
                producto = {headers[i]: values[i] for i in range(len(headers))}
                #producto = {headers[i].lower(): values[i] for i in range(len(headers))}
                productos.append(producto)

                #print(producto)

        if not productos:
            print("No hay productos registrados.")
            return

        print("Lista de productos:")
        tabla = [[producto["ID"], producto["Nombre"], producto["Precio"]] for producto in productos]
        print(tabulate(tabla, headers=["ID", "Nombre", "Precio"], tablefmt="fancy_grid"))
    
    except FileNotFoundError:
        print(f"Error: El archivo '{stock_productos_csv}' no se encontró.")
    except KeyError as e:
        print(f"Error: La clave '{e}' no se encontró en los datos del producto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

