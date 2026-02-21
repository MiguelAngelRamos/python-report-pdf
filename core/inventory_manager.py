from data.storage import inventario, categorias_existentes

def agregar_producto(nombre: str, precio: float, categoria: str):
    """Inserta un diccionario en la lista y actualiza el set de categorías."""
    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria
    }

    # Ejemplo de producto
    # {"nombre": "Laptop Gamer", "precio": 1500.00, "categoria": "Computación"}
    inventario.append(producto)
    categorias_existentes.add(categoria)
    print(f"[LOG] Producto '{nombre}' registrado.")

# nombre viene con el valor "Laptop Gamer"
def eliminar_producto_por_nombre(nombre: str):
    """Borra un elemento de la lista buscando por su clave."""
    global inventario
    # Filtrar la lista (Crear una nueva sin el elemento a borrar)
    longitud_inicial = len(inventario)
    # inventario[:] = [p for p in inventario if p["nombre"].lower() != nombre.lower()]
    # esto es nuestro inventario 
    # inventario = [
    #     {"nombre": "Laptop Gamer", "precio": 1500.00, "categoria": "Computación"},
    #     {"nombre": "Smartphone", "precio": 800.00, "categoria": "Electrónica"},
    #     {"nombre": "Cámara", "precio": 500.00, "categoria": "Fotografía"}
    # ]
    nuevo_lista = []
    for producto in inventario:
        nombre_producto = producto["nombre"].lower() # nombre_producto = "Cámara"
        nombre_buscado  = nombre.lower() # nombre_buscado = "laptop gamer"
        # "Laptop Gamer" != "laptop gamer" (primera iteración)
        # "Smartphone" != "laptop gamer" (segunda iteración)
        # "Cámara" != "laptop gamer" (tercera iteración)
        if nombre_producto != nombre_buscado:
            nuevo_lista.append(producto)
            # nuevo_lista = [
            #     {"nombre": "Smartphone", "precio": 800.00, "categoria": "Electrónica"},
            #     {"nombre": "Cámara", "precio": 500.00, "categoria": "Fotografía"}
            # ]
    inventario[:] = nuevo_lista
    # nuestro inventario ahora es:
    # inventario = [
    #         {"nombre": "Smartphone", "precio": 800.00, "categoria": "Electrónica"},
    #         {"nombre": "Cámara", "precio": 500.00, "categoria": "Fotografía"}
    #        ]
    #
    
    if len(inventario) < longitud_inicial:
        print(f"[LOG] '{nombre}' eliminado del sistema.")
    else:
        print(f"[ERR] No se encontró el producto '{nombre}'.")

def listar_inventario():
    """Itera sobre la estructura y cuenta elementos."""
    print(f"\n--- Resumen de {len(inventario)} Productos ---")
    for idx, p in enumerate(inventario, 1):
        print(f"{idx}. {p['nombre']} | Cat: {p['categoria']} | Base: ${p['precio']}")
