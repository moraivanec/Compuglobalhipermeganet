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
    while opcion_seleccionada != 7:
        limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el menú
        print("Menú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Ver inventario actual")
        print("5. Buscar producto por ID")
        print("6. Generar informe de inventario")
        print("7. Salir")
        opcion_seleccionada = int(input("Elija una opción: "))

        match opcion_seleccionada:
            case 1:
                # Llamar a la función para añadir un producto
                pass
            case 2:
                # Llamar a la función para editar un producto
                pass
            case 3:
                # Llamar a la función para eliminar un producto
                pass
            case 4:
                # Llamar a la función para ver el inventario actual
                pass
            case 5:
                # Llamar a la función para buscar un producto por ID
                pass
            case 6:
                # Llamar a la función para generar un informe de inventario
                pass
            case 7:
                print("Saliendo del programa...")
            case _:
                print("Opción no válida, por favor intente nuevamente.")

menu()