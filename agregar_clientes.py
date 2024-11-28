import csv

clientes = []

def agregar_clientes():
  dni = input("Ingrese el DNI del cliente: ")
  nombre_cliente = input("Ingrese el nombre del cliente: ")
  email = input("Ingrese el correo electrónico del cliente: ")

  cliente = {'DNI': dni, 'Nombre': nombre_cliente, 'Correo electrónico': email}

  with open('clientes.csv', 'a', newline = '') as csvfile:
    columnas = ['DNI', 'Nombre', 'Correo electrónico']
    writer = csv.DictWriter(csvfile, fieldnames = columnas)
    
    if csvfile.tell() == 0:
        writer.writeheader()
    
    writer.writerow(cliente)
    
  clientes.append(cliente)
  print("\n¡Cliente agregado con éxito!")
   
agregar_clientes()