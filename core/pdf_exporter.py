from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from datetime import datetime
import os


def exportar_reporte_pdf(inventario: list, nombre_tienda: str, tasas_impuestos: tuple, calcular_precio_final) -> str:
    """
    Genera un reporte PDF con el inventario actual de la tienda.
    Retorna la ruta del archivo generado.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reporte_inventario_{timestamp}.pdf"
    ruta_salida = os.path.join(os.getcwd(), nombre_archivo)

    doc = SimpleDocTemplate(
        ruta_salida,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        "Titulo",
        parent=estilos["Heading1"],
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=6,
        textColor=colors.HexColor("#1a1a2e"),
    )
    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555"),
        spaceAfter=16,
    )

    elementos = []

    # --- Encabezado ---
    elementos.append(Paragraph(nombre_tienda, estilo_titulo))
    elementos.append(
        Paragraph(
            f"Reporte de Inventario &mdash; {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            estilo_subtitulo,
        )
    )
    elementos.append(Spacer(1, 0.4 * cm))

    # --- Tabla de productos ---
    encabezados = ["#", "Producto", "Categoría", "Precio Base", "Precio c/ IVA"]
    filas = [encabezados]

    total_base = 0
    total_final = 0

    for idx, p in enumerate(inventario, 1):
        precio_base = p["precio"]
        precio_final = calcular_precio_final(precio_base, tasas_impuestos)
        total_base += precio_base
        total_final += precio_final
        filas.append([
            str(idx),
            p["nombre"],
            p["categoria"],
            f"${precio_base:,.0f}".replace(",", "."),
            f"${precio_final:,.0f}".replace(",", "."),
        ])

    # Fila de totales
    filas.append([
        "",
        "TOTAL",
        "",
        f"${total_base:,.0f}".replace(",", "."),
        f"${total_final:,.0f}".replace(",", "."),
    ])

    tabla = Table(
        filas,
        colWidths=[1 * cm, 6.5 * cm, 4 * cm, 3.5 * cm, 3.5 * cm],
    )
    tabla.setStyle(
        TableStyle([
            # Encabezado
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 11),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
            # Cuerpo
            ("FONTNAME", (0, 1), (-1, -2), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -2), 10),
            ("ALIGN", (0, 1), (0, -1), "CENTER"),
            ("ALIGN", (3, 1), (-1, -1), "RIGHT"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.HexColor("#f0f4ff")]),
            ("GRID", (0, 0), (-1, -2), 0.5, colors.HexColor("#cccccc")),
            ("BOTTOMPADDING", (0, 1), (-1, -2), 8),
            ("TOPPADDING", (0, 1), (-1, -2), 8),
            # Fila de totales
            ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#e8ecff")),
            ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, -1), (-1, -1), 10),
            ("ALIGN", (1, -1), (1, -1), "RIGHT"),
            ("TOPPADDING", (0, -1), (-1, -1), 10),
            ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
            ("LINEABOVE", (0, -1), (-1, -1), 1.5, colors.HexColor("#1a1a2e")),
        ])
    )
    elementos.append(tabla)
    elementos.append(Spacer(1, 0.6 * cm))

    # --- Resumen de impuestos ---
    porcentaje_total = sum(tasas_impuestos) * 100
    estilo_nota = ParagraphStyle(
        "Nota",
        parent=estilos["Normal"],
        fontSize=8,
        textColor=colors.HexColor("#777777"),
    )
    elementos.append(
        Paragraph(
            f"* Precios con IVA incluyen un {porcentaje_total:.0f}% de impuestos "
            f"({', '.join([f'{t*100:.0f}%' for t in tasas_impuestos])}).",
            estilo_nota,
        )
    )

    doc.build(elementos)
    return ruta_salida
# 