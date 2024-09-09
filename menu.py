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
    while opcion_seleccionada != "7":
        limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el menú
        opciones = ["Menú de Gestión de Inventarios", "1. Añadir producto",
                    "2. Editar producto", "3. Eliminar producto",
                    "4. Ver inventario actual", "5. Buscar producto por ID",
                    "6. Generar informe de inventario", "7. Salir"]
        for op in opciones:
            print(op)        
        opcion_seleccionada = input("Elija una opción: ")

        match opcion_seleccionada:
            case "1":
                # Añadir un producto
                pass
            case "2":
                # Editar un producto
                pass
            case "3":
                # Eliminar un producto
                pass
            case "4":
                # Ver el inventario actual
                pass
            case "5":
                # Buscar un producto por ID
                pass
            case "6":
                # Generar informe
                pass
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente nuevamente.")

menu()
