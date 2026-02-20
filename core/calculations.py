def calcular_precio_final(precio: float, impuestos: tuple) -> float:
    """Calcula el precio sumando los porcentajes de la tupla de impuestos."""
    factor_impuesto = sum(impuestos)
    return round(precio * (1 + factor_impuesto), 2)
