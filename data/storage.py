# Variables Globales y Estructuras de Datos
NOMBRE_TIENDA = "TechStore Chile"

# Usamos una lista para el inventario (permite orden y duplicados de productos)
inventario = [] # importante: esta variable es global y se modificará desde otros módulos

# Usamos un set para categorías únicas
categorias_existentes = set() # importante: esta variable es global y se modificará desde otros módulos

# Usamos una tupla para impuestos (inmutabilidad)
# 0.19 = IVA, 0.05 = Tasa Proceso
TASAS_IMPUESTOS = (0.19, 0.05)
