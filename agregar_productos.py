import csv
from datetime import datetime

productos = []
stock = {}
entradas = []

def agregar_productos():
    id_producto = int(input("Ingrese el ID del producto: "))
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad inicial del producto: "))

    producto = {'ID': id_producto, 'Nombre': nombre_producto, 'Precio': precio}
    
    with open('productos.csv', 'a', newline = '') as csvfile: # Abre el archivo en modo "append" y maneja las nuevas líneas de manera consistente (Windows, Linux, etc.)
        columnas = ['ID', 'Nombre', 'Precio']
        writer = csv.DictWriter(csvfile, fieldnames = columnas) # Crea un objeto que se utiliza para escribir diccionarios en el archivo CSV.
        
        if csvfile.tell() == 0: # Verifica si el archivo está vacío antes de escribir el encabezado
            writer.writeheader()
            
        writer.writerow(producto) # Escribe el nuevo producto en el archivo CSV    
        
        productos.append(producto)
        stock[id_producto] = cantidad
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entradas.append({'ID': id_producto, 'Cantidad': cantidad, 'Fecha': fecha_actual})
        
    print("\n¡Producto agregado con éxito!")
    
agregar_productos()