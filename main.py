# Necesitamos importaciones de los modulos de core y data
from data.storage import NOMBRE_TIENDA, TASAS_IMPUESTOS, categorias_existentes, inventario
from core.inventory_manager import agregar_producto, eliminar_producto_por_nombre, listar_inventario

def run_app():
    print(f"Bienvenido a {NOMBRE_TIENDA}\n!" + "="*25)
    # print("Categorías disponibles:", ", ".join(categorias_existentes) if categorias_existentes else "No hay categorías registradas.")
    
    # 1. Agregar productos
    agregar_producto("Laptop Gamer", 1500.00, "Computación")
    agregar_producto("Smartphone", 800.00, "Electrónica")
    agregar_producto("Cámara", 500.00, "Fotografía")
    
    # 2. Acceder y Procesar datos
    if inventario:
        primer_producto = inventario[0]
        print(f"\nPrimer producto registrado: {primer_producto['nombre']} | Precio Base: ${primer_producto['precio']}")
        # precio_base = primer_producto["precio"]
        # precio_final = calcular_precio_final(precio_base, TASAS_IMPUESTOS)
        # print(f"\nPrecio final de '{primer_producto['nombre']}' con impuestos: ${precio_final}")
    # 3. Listar inventario
    listar_inventario()
    
    # 4. Eliminar un producto
    eliminar_producto_por_nombre("Laptop Gamer")
    
    # 5. Listar inventario actualizado
    listar_inventario()