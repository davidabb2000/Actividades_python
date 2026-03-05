# 🐍 Ejercicios de Python – Fundamentos de Programación

Colección de ejercicios prácticos en Python organizados por unidades temáticas, cubriendo desde estructuras condicionales básicas hasta funciones, recursión y un proyecto integrador de biblioteca.

---

## 📁 Estructura del Proyecto

```
📦 python-ejercicios
├── 📄 index.py              # Playground general / ejemplos de listas, tuplas, sets y diccionarios
│
├── 🔹 Unidad 1 – Condicionales y Validaciones
│   ├── act.py               # 1.1 – Datos del usuario con validación de edad
│   ├── act1_2.py            # 1.2 – Calculadora básica
│   ├── act1_3.py            # 1.3 – Validación de correo electrónico
│   ├── act1_4.py            # 1.4 – Validador de contraseña segura
│   └── act1_5.py            # 1.5 – Convertidor de unidades con menú
│
├── 🔸 Unidad 2 – Estructuras Condicionales Avanzadas
│   ├── act2_1.py            # 2.1 – Clasificador de edad por categoría
│   ├── act2_2.py            # 2.2 – Menú interactivo con bucle
│   ├── act2_3.py            # 2.3 – Calculadora con menú y múltiples operaciones
│   ├── act2_4.py            # 2.4 – Conversor de calificación numérica a letra
│   └── act2_5.py            # 2.5 – Simulador de descuentos por categoría
│
├── 🔶 Unidad 3 – Ciclos y Listas
│   ├── act3_1.py            # 3.1 – Números pares con ciclo for
│   ├── act3_2.py            # 3.2 – Suma acumulada con ciclo while
│   ├── act3_3.py            # 3.3 – Buscador de nombres en lista
│   ├── act3_4.py            # 3.4 – Generador de tabla de multiplicar
│   └── act3_5.py            # 3.5 – Eliminación de duplicados (en progreso)
│
├── 🟣 Unidad 4 – Estructuras de Datos
│   ├── act4_1.py            # 4.1 – Lista de compras dinámica
│   ├── act4_2.py            # 4.2 – Directorio de contactos con diccionarios
│   ├── act4_3.py            # 4.3 – Gestión de productos con diccionarios
│   ├── act4_4.py            # 4.4 – Estadísticas de una lista de números
│   └── act4_5.py            # 4.5 – Comparación de listas (comunes y únicos)
│
├── 🟢 Unidad 5 – Funciones
│   ├── act5_1.py            # 5.1 – Función de saludo según hora del día
│   ├── act5_2.py            # 5.2 – Función para calcular promedio con validación
│   ├── act5_3.py            # 5.3 – Calculadora refactorizada con funciones
│   ├── act5_4.py            # 5.4 – Detector de palíndromos
│   └── act5_5.py            # 5.5 – Factorial recursivo
│
└── 🏛️ Proyecto Integrador
    └── taller.py            # Sistema completo de gestión de biblioteca
```

---

## 📚 Descripción de Ejercicios

### 🔹 Unidad 1 – Condicionales y Validaciones

| Archivo | Descripción |
|---|---|
| `act.py` | Solicita nombre, edad y ciudad. Valida que la edad sea un número positivo. |
| `act1_2.py` | Calculadora simple con soporte para `+`, `-`, `*`, `/`. Maneja división por cero. |
| `act1_3.py` | Verifica si un correo electrónico tiene formato válido (`@` y `.` en posición correcta). |
| `act1_4.py` | Valida que una contraseña tenga mínimo 8 caracteres, un número y un carácter especial. |
| `act1_5.py` | Convierte unidades: Celsius→Fahrenheit, Kilómetros→Millas, Kilogramos→Libras. |

### 🔸 Unidad 2 – Estructuras Condicionales Avanzadas

| Archivo | Descripción |
|---|---|
| `act2_1.py` | Clasifica una edad en: niño, adolescente, adulto o adulto mayor. |
| `act2_2.py` | Menú interactivo con opciones de saludo, despedida y salida. |
| `act2_3.py` | Calculadora mejorada con menú continuo y las cuatro operaciones básicas. |
| `act2_4.py` | Convierte una nota numérica (0-100) a su equivalente en letra (A, B, C, D, F). |
| `act2_5.py` | Aplica descuentos según categoría del cliente (A=20%, B=15%, C=10%). |

### 🔶 Unidad 3 – Ciclos y Listas

| Archivo | Descripción |
|---|---|
| `act3_1.py` | Imprime todos los números pares del 1 hasta N usando `for`. |
| `act3_2.py` | Suma números ingresados por el usuario hasta que ingrese 0. |
| `act3_3.py` | Busca un nombre en una lista predefinida y muestra su posición. |
| `act3_4.py` | Genera la tabla de multiplicar de un número del 1 al 10. |
| `act3_5.py` | *(En desarrollo)* Elimina duplicados de una lista sin usar sets. |

### 🟣 Unidad 4 – Estructuras de Datos

| Archivo | Descripción |
|---|---|
| `act4_1.py` | Lista de compras con menú para agregar, eliminar y mostrar productos. |
| `act4_2.py` | Directorio de contactos usando diccionarios con búsqueda, agregar y eliminar. |
| `act4_3.py` | Gestión de productos (nombre, precio, stock) con actualización de precios. |
| `act4_4.py` | Recibe una lista de números y calcula máximo, mínimo, promedio y suma total. |
| `act4_5.py` | Compara dos listas e identifica elementos comunes y únicos de cada una. |

### 🟢 Unidad 5 – Funciones

| Archivo | Descripción |
|---|---|
| `act5_1.py` | Función `saludar(nombre, hora)` que retorna saludo según franja horaria. |
| `act5_2.py` | Función `calcular_promedio(lista)` con validación para listas vacías. |
| `act5_3.py` | Calculadora refactorizada con funciones independientes por operación. |
| `act5_4.py` | Función `es_palindromo(texto)` que ignora espacios, puntuación y mayúsculas. |
| `act5_5.py` | Función `factorial(n)` implementada con recursión y validación de negativos. |

### 🏛️ Proyecto Integrador – Sistema de Biblioteca

`taller.py` es un sistema completo de gestión de biblioteca que integra los conceptos de todas las unidades anteriores.

**Funciones principales:**

| Función | Descripción |
|---|---|
| `agregar_libro()` | Registra un nuevo libro con ID autoincremental y validación de año (> 1900). |
| `mostrar_libros()` | Muestra el catálogo completo con estado de disponibilidad. |
| `buscar_libro()` | Búsqueda parcial por título o autor (sin distinción de mayúsculas). |
| `prestar_libro(id)` | Cambia el estado del libro a *Prestado* si está disponible. |
| `devolver_libro(id)` | Registra la devolución y cambia el estado a *Disponible*. |
| `eliminar_libro(id)` | Elimina un libro solo si no está prestado actualmente. |

**Funciones adicionales:**

| Función | Descripción |
|---|---|
| `libros_por_autor(autor)` | Lista todos los libros de un autor específico. |
| `estadisticas()` | Muestra total, disponibles, prestados y porcentaje de disponibilidad. |
| `exportar_a_txt()` | Guarda el catálogo completo en un archivo `biblioteca.txt`. |

---

## 🚀 Cómo ejecutar

### Requisitos

- Python 3.10 o superior → [Descargar Python](https://www.python.org/downloads/)

> ⚠️ La versión 3.10+ es necesaria para los ejercicios que usan `match/case` (Unidades 4 y 5).

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/davidabb2000/Actividades_python.git

# 2. Entra a la carpeta
cd tu-repositorio

# 3. Ejecuta cualquier ejercicio
python act.py
python act4_2.py
python taller.py
```

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-En%20progreso-yellow)

---

## 📌 Estado del Proyecto

| Unidad | Tema | Estado |
|---|---|---|
| Unidad 1 | Condicionales y Validaciones | ✅ Completa |
| Unidad 2 | Estructuras Condicionales Avanzadas | ✅ Completa |
| Unidad 3 | Ciclos y Listas | 🔄 En progreso (`act3_5.py` pendiente) |
| Unidad 4 | Estructuras de Datos | ✅ Completa |
| Unidad 5 | Funciones | ✅ Completa |
| Taller | Sistema de Gestión de Biblioteca | ✅ Completo |

---

## 📄 Licencia

Este proyecto es de uso educativo y está bajo la licencia [MIT](LICENSE).
