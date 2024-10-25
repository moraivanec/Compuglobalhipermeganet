def agregar_cliente(clientes: List[Dict[str, str]]) -> None:
    """
    Contrato:
    - Agrega un nuevo cliente a la lista de clientes.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - Agrega un nuevo cliente a la lista de "clientes"..
    """
    try:
        assert nombre_cliente != "", "El nombre no puede estar vacío."
        assert dni != "", "El DNI no puede estar vacío."
        assert correo != "", "El correo no puede estar vacío."
        
        if not re.match(r"^[A-Za-z\s]+$", nombre_cliente):
            print("El nombre solo puede tener letras y espacios.")
            return
            
        if not re.match(r"^\d{8}$", dni):
            print("El DNI debe tener exactamente 8 dígitos.")
            return
            
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
            print("El correo no es válido.")
            return
        
        nuevo_cliente = {
            "nombre": nombre_cliente,
            "dni": dni,
            "correo": correo
        }
        
        clientes.append(nuevo_cliente)
        print("¡Cliente agregado existosamente!")

    except ValueError:
        print("Error!")
            
   
def editar_cliente(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Edita un cliente existente en la lista de clientes. 
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo.
    
    Postcondiciones:
    - El cliente seleccionado es editado con los nuevos valores proporcionados.
    """
    try:
        assert dni != "", "El DNI del cliente a editar no puede estar vacío."
        
        # Busco al cliente en la lista y lo edito si se encuentra
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["dni"] == dni:
                cliente_encontrado = True
                
        assert cliente_encontrado, "Cliente no encontrado."
                
                assert nombre_cliente_editado != "", "El nuevo nombre no puede estar vacío."
                assert dni_editado != "", "El nuevo DNI no puede estar vacío."
                assert correo_editado != "", "El nuevo correo no puede estar vacío."
                 
                if not re.match(r"^[A-Za-z\s]+$", nombre_cliente_editado):
                    print("El nuevo nombre solo puede tener letras y espacios.")
                    return
                    
                if not re.match(r"^\d{8}$", dni_editado):
                    print("El nuevo DNI debe tener exactamente 8 dígitos.")
                    return
            
                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo_editado):
                    print("El nuevo correo no es válido.")
                    return
                    
                # Actualizo los datps
                cliente["nombre"] = nombre_cliente_editado
                cliente["dni"] = dni_editado
                cliente["correo"] = correo_editado
                print("¡Cliente editado exitosamente!")
                break
                
    except ValueError:
        print("Error!")
                    

def eliminar_cliente(clientes: List[Dict[str, Any]]) -> None:
     """
    Contrato:
    - Elimina un cliente existente en la lista de clientes.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios, donde cada diccionario representa un cliente con su nombre, DNI y correo.
    
    Postcondiciones:
    - El cliente seleccionado es eliminado de la lista de clientes.
    """
    try:
        assert dni != "", "El DNI del cliente a editar no puede estar vacío."
        
        cliente_encontrado = False
        for cliente in clientes:
            if cliente["dni"] == dni:
                cliente_encontrado = True
                clientes.remove(cliente)  # Elimino el cliente de la lista
                print("¡Cliente eliminado exitosamente!")
                return
            
        assert cliente_encontrado, "Cliente no encontrado."
        
    except ValueError:
        print("Error!"):
        

def consultar_lista_clientes(clientes: List[Dict[str, Any]]) -> None:
    """
    Contrato:
    - Consulta y muestra la lista de clientes registrados.
    
    Precondiciones:
    - "clientes" es una lista de diccionarios donde cada diccionario representa un cliente con su nombre, DNI y correo electrónico.
    
    Postcondiciones:
    - Si la lista "clientes" está vacía, se imprime en la consola un mensaje indicando que no hay clientes registrados.
    - Si hay clientes en la lista, se imprime en la consola una tabla con los detalles de cada uno.
    """
    print("Lo sentimos, esta función no está implementada. Intente más tarde.")

