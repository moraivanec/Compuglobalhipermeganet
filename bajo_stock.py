import json as js
from typing import Dict

def bajo_stock(stock: Dict[str, int]) -> None:
    umbral_minimo = 10
    # Filtra el diccionario 'stock' para encontrar productos con cantidades por debajo del umbral mínimo.
    productos_bajo_stock = dict(filter(lambda item: item[1] < umbral_minimo, stock.items())) 

    if not productos_bajo_stock:
        print("\nNo hay productos con bajo stock.")
        return

    informe_bajo_stock = js.dumps(productos_bajo_stock, indent = 2)
    print("¡Atención! Productos con bajo stock:")
    print(informe_bajo_stock)
    
# Ejemplo de uso
stock = {
    "Monitor LED 24": 15,
    "Teclado Gamer Wireless": 8,
    "Procesador AMD Ryzen": 5
}

bajo_stock(stock)