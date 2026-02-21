def calcular_precio_final(precio: float, impuestos: tuple) -> float:
    """Calcula el precio sumando los porcentajes de la tupla de impuestos."""
     
    factor_impuesto = sum(impuestos) # 0.19 + 0.05 = 0.24
    # 1000×(1+0.24)=1000×1.24=1240.0
    return round(precio * (1 + factor_impuesto), 2)