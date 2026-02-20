# TechStore Chile - Sistema de Gestión de Inventario

Un proyecto educativo de nivel ingenieril que demuestra **modularización profesional** en Python siguiendo los principios de **Separación de Responsabilidades (SoC)** y el **Principio de Responsabilidad Única**.

## Estructura del Proyecto

```
techstore_project/
│
├── main.py                 # Punto de entrada (Invocación)
├── core/                   # Lógica de negocio (Funciones)
│   ├── __init__.py
│   ├── inventory_manager.py
│   └── calculations.py
└── data/                   # Definición de estructuras y constantes
    ├── __init__.py
    └── storage.py
```

## 🎯 Características Implementadas

### Estructuras de Datos Python
- **Lista** (`list`): Almacenamiento ordenado del inventario
- **Set** (`set`): Categorías únicas sin duplicados
- **Tupla** (`tuple`): Tasas de impuestos inmutables
- **Diccionario** (`dict`): Representación de cada producto

### Arquitectura por Capas

#### 1️⃣ Capa de Datos (`data/storage.py`)
Define las estructuras de datos globales:
- Inventario de productos
- Categorías únicas
- Constantes del sistema (nombre tienda, tasas de impuestos)

#### 2️⃣ Capa de Lógica de Negocio (`core/`)
- **`calculations.py`**: Funciones puras de cálculo (precio final con impuestos)
- **`inventory_manager.py`**: Operaciones CRUD sobre el inventario

#### 3️⃣ Punto de Entrada (`main.py`)
Orquestador que demuestra el uso del sistema con un flujo completo.

## 🚀 Ejecución

```bash
cd techstore_project
python main.py
```

## Mejores Prácticas Aplicadas

✅ **Type Hinting**: Uso de anotaciones de tipo para mejor legibilidad  
✅ **F-strings**: Formato moderno de cadenas  
✅ **Docstrings**: Documentación en cada función  
✅ **Modularización**: Separación clara de responsabilidades  
✅ **Gestión de Scope**: Uso correcto de variables globales y locales  
✅ **PEP 8**: Convenciones de estilo de Python  

## Conceptos Demostrados

- Importación de módulos personalizados
- Uso de `__init__.py` para paquetes
- Manipulación de estructuras de datos mutables/inmutables
- List comprehension para filtrado
- Iteración con `enumerate()`
- Logging básico con prefijos `[LOG]` y `[ERR]`

## Nivel de Complejidad

**Ingeniero en Informática** - Arquitectura escalable y mantenible para proyectos profesionales.

---

**Autor**: MIGUEL RAMOS 
**Fecha**: 2026  
**Tecnología**: Python 3.x
