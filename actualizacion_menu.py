from os import system, name

def limpiar_pantalla():
    # Identificar el sistema operativo
    if name == 'nt':
        # Windows
        system('cls')
    else:
        # Linux y Mac
        system('clear')

def menu():
    opcion_seleccionada = 0
    while opcion_seleccionada != "9":
        limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el menú
        opciones = ["Menú de Gestión de Inventarios", "1. Añadir producto",
                    "2. Editar producto", "3. Eliminar producto", "4. Añadir cliente",
                    "5. Registrar una venta", "6. Ver inventario actual",
                    "7. Buscar producto por ID", "8. Generar informe de inventario", "9. Salir"]
        for op in opciones:
            print(op)        
        opcion_seleccionada = input("Elija una opción: ")

        match opcion_seleccionada:
            case "1":
                # Añadir un producto
                cargar_productos(productos, stock)
                pass
            case "2":
                # Editar un producto
                editar_producto(productos, stock)
                pass
            case "3":
                # Eliminar un producto
                eliminar_producto(productos, stock)
            case "4":
                # Añadir un cliente
                cargar_cliente(clientes)
            case "5":
                # Registrar una venta
                registrar_venta(ventas, stock)
                pass
            case "6":
                # Ver el inventario actual
                inventario_actual(stock)
                pass
            case "7":
                # Buscar un producto por ID
                buscar_producto_id(productos, producto_id)
                pass
            case "8":
                # Generar informe del inventario
                generar_informe(stock)
                pass
            case "9":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente nuevamente.")

menu()