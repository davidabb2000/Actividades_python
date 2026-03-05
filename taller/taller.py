# Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener: id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).

# Funciones principales: o agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900. o mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]" o buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales. o prestar_libro(id): Cambia el estado de disponibilidad a False si el libro existe y está disponible. o devolver_libro(id): Cambia el estado de disponibilidad a True.
# o eliminar_libro(id): Elimina un libro solo si no está prestado actualmente. o menu_principal(): Implementa un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.

# Funciones adicionales desafiantes: o libros_por_autor(autor): Lista todos los libros de un autor específico. o estadisticas(): Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados. o exportar_a_txt(): Guarda todos los libros en un archivo de texto llamado "biblioteca.txt".

# Lista global que almacena todos los libros como diccionarios
biblioteca = []

# Contador global para generar IDs autoincrementales
contador_id = 1


# =============================================================================
# FUNCIONES PRINCIPALES
# =============================================================================

def agregar_libro():
    """
    Registra un nuevo libro en la biblioteca.
    Solicita título, autor y año, validando que el año sea numérico
    y mayor a 1900. Asigna un ID autoincremental y disponibilidad True.
    """
    global contador_id  # Accedemos al contador global para asignar el ID

    print("\n📚 AGREGAR NUEVO LIBRO")
    print("-" * 40)

    # Solicitar y validar el título (no puede estar vacío)
    titulo = input("Título del libro: ").strip()
    if not titulo:
        print("⚠️  El título no puede estar vacío.")
        return

    # Solicitar y validar el autor (no puede estar vacío)
    autor = input("Autor del libro: ").strip()
    if not autor:
        print("⚠️  El autor no puede estar vacío.")
        return

    # Solicitar y validar el año de publicación
    año_input = input("Año de publicación: ").strip()

    # Verificar que el año sea numérico
    if not año_input.isdigit():
        print("⚠️  El año debe ser un valor numérico.")
        return

    año = int(año_input)

    # Verificar que el año sea mayor a 1900
    if año <= 1900:
        print("⚠️  El año debe ser mayor a 1900.")
        return

    # Crear el diccionario del nuevo libro
    nuevo_libro = {
        "id": contador_id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "disponible": True  # Todo libro nuevo se registra como disponible
    }

    # Agregar el libro a la lista de la biblioteca
    biblioteca.append(nuevo_libro)

    # Incrementar el contador para el próximo ID
    contador_id += 1

    print(f"\n✅ Libro '{titulo}' agregado correctamente con ID {nuevo_libro['id']}.")


def mostrar_libros():
    """
    Muestra todos los libros registrados en la biblioteca en formato legible.
    Formato: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]"
    Si no hay libros, informa al usuario.
    """
    print("\n📖 CATÁLOGO DE LIBROS")
    print("-" * 60)

    # Verificar si la biblioteca tiene libros
    if not biblioteca:
        print("⚠️  No hay libros registrados en la biblioteca.")
        return

    # Recorrer cada libro y mostrarlo con el formato requerido
    for libro in biblioteca:
        # Determinar el estado de disponibilidad como texto
        estado = "Disponible" if libro["disponible"] else "Prestado"

        # Imprimir la información del libro en el formato especificado
        print(f"ID: {libro['id']} - '{libro['titulo']}' "
              f"({libro['autor']}, {libro['año']}) [{estado}]")

    print(f"\nTotal de libros en catálogo: {len(biblioteca)}")


def buscar_libro():
    """
    Busca libros por título o autor usando coincidencias parciales (no sensible
    a mayúsculas/minúsculas). Muestra todos los resultados encontrados.
    """
    print("\n🔍 BUSCAR LIBRO")
    print("-" * 40)

    # Solicitar el término de búsqueda
    termino = input("Ingresa título o autor a buscar: ").strip().lower()

    if not termino:
        print("⚠️  Debes ingresar un término de búsqueda.")
        return

    # Filtrar libros donde el término coincida parcialmente con título o autor
    resultados = [
        libro for libro in biblioteca
        if termino in libro["titulo"].lower() or termino in libro["autor"].lower()
    ]

    # Mostrar resultados o informar que no se encontró nada
    if not resultados:
        print(f"⚠️  No se encontraron libros que coincidan con '{termino}'.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):\n")
        for libro in resultados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ID: {libro['id']} - '{libro['titulo']}' "
                  f"({libro['autor']}, {libro['año']}) [{estado}]")


def prestar_libro(id_libro):
    """
    Cambia el estado de disponibilidad de un libro a False (prestado).
    Solo funciona si el libro existe y está disponible actualmente.

    Parámetro:
        id_libro (int): ID numérico del libro a prestar.
    """
    # Buscar el libro por su ID usando next() con valor por defecto None
    libro = next((l for l in biblioteca if l["id"] == id_libro), None)

    # Verificar si el libro existe
    if libro is None:
        print(f"⚠️  No existe ningún libro con ID {id_libro}.")
        return

    # Verificar si el libro está disponible para préstamo
    if not libro["disponible"]:
        print(f"⚠️  El libro '{libro['titulo']}' ya está prestado.")
        return

    # Cambiar el estado a no disponible (prestado)
    libro["disponible"] = False
    print(f"✅ El libro '{libro['titulo']}' ha sido prestado exitosamente.")


def devolver_libro(id_libro):
    """
    Cambia el estado de disponibilidad de un libro a True (disponible).
    Registra la devolución de un libro previamente prestado.

    Parámetro:
        id_libro (int): ID numérico del libro a devolver.
    """
    # Buscar el libro por su ID
    libro = next((l for l in biblioteca if l["id"] == id_libro), None)

    # Verificar si el libro existe
    if libro is None:
        print(f"⚠️  No existe ningún libro con ID {id_libro}.")
        return

    # Verificar si el libro realmente estaba prestado
    if libro["disponible"]:
        print(f"⚠️  El libro '{libro['titulo']}' no estaba prestado.")
        return

    # Cambiar el estado a disponible
    libro["disponible"] = True
    print(f"✅ El libro '{libro['titulo']}' ha sido devuelto exitosamente.")


def eliminar_libro(id_libro):
    """
    Elimina un libro del catálogo solo si no está actualmente prestado.
    Si el libro está prestado, debe ser devuelto antes de eliminarse.

    Parámetro:
        id_libro (int): ID numérico del libro a eliminar.
    """
    # Buscar el libro por su ID
    libro = next((l for l in biblioteca if l["id"] == id_libro), None)

    # Verificar si el libro existe
    if libro is None:
        print(f"⚠️  No existe ningún libro con ID {id_libro}.")
        return

    # Verificar si el libro está prestado (no se puede eliminar si está prestado)
    if not libro["disponible"]:
        print(f"⚠️  No se puede eliminar '{libro['titulo']}' porque está prestado.")
        print("    Primero debe registrarse su devolución.")
        return

    # Confirmar la eliminación con el usuario
    confirmacion = input(f"¿Estás seguro de eliminar '{libro['titulo']}'? (s/n): ").strip().lower()

    if confirmacion == "s":
        biblioteca.remove(libro)
        print(f"✅ El libro '{libro['titulo']}' ha sido eliminado del catálogo.")
    else:
        print("❌ Eliminación cancelada.")


# =============================================================================
# FUNCIONES ADICIONALES
# =============================================================================

def libros_por_autor(autor):
    """
    Lista todos los libros de un autor específico usando coincidencia parcial.
    Útil para ver todas las obras de un mismo autor en la biblioteca.

    Parámetro:
        autor (str): Nombre o parte del nombre del autor a buscar.
    """
    print(f"\n👤 LIBROS DEL AUTOR: '{autor}'")
    print("-" * 40)

    # Filtrar libros cuyo autor contenga el texto buscado (sin distinción de mayúsculas)
    resultados = [
        libro for libro in biblioteca
        if autor.lower() in libro["autor"].lower()
    ]

    # Mostrar los libros encontrados o un mensaje informativo
    if not resultados:
        print(f"⚠️  No se encontraron libros del autor '{autor}'.")
    else:
        print(f"Se encontraron {len(resultados)} libro(s):\n")
        for libro in resultados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['año']}) [{estado}]")


def estadisticas():
    """
    Muestra un resumen estadístico del sistema de biblioteca:
    - Cantidad total de libros en el catálogo
    - Cantidad de libros disponibles para préstamo
    - Cantidad de libros actualmente prestados
    """
    print("\n📊 ESTADÍSTICAS DEL SISTEMA")
    print("-" * 40)

    # Calcular el total de libros
    total = len(biblioteca)

    # Contar libros disponibles (disponible == True)
    disponibles = sum(1 for libro in biblioteca if libro["disponible"])

    # Contar libros prestados (disponible == False)
    prestados = total - disponibles

    # Mostrar las estadísticas
    print(f"📚 Total de libros en catálogo : {total}")
    print(f"✅ Libros disponibles          : {disponibles}")
    print(f"📤 Libros prestados            : {prestados}")

    # Mostrar porcentaje de disponibilidad si hay libros
    if total > 0:
        porcentaje = (disponibles / total) * 100
        print(f"📈 Porcentaje de disponibilidad: {porcentaje:.1f}%")


def exportar_a_txt():
    """
    Guarda toda la información del catálogo en un archivo de texto
    llamado 'biblioteca.txt'. Incluye encabezado, listado de libros
    y estadísticas al final del archivo.
    """
    # Nombre del archivo de exportación
    nombre_archivo = "biblioteca.txt"

    try:
        # Abrir el archivo en modo escritura con codificación UTF-8
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:

            # Escribir encabezado del archivo
            archivo.write("=" * 60 + "\n")
            archivo.write("        CATÁLOGO DE LA BIBLIOTECA\n")
            archivo.write("=" * 60 + "\n\n")

            # Verificar si hay libros para exportar
            if not biblioteca:
                archivo.write("No hay libros registrados en la biblioteca.\n")
            else:
                # Escribir cada libro en el formato requerido
                for libro in biblioteca:
                    estado = "Disponible" if libro["disponible"] else "Prestado"
                    linea = (f"ID: {libro['id']} - '{libro['titulo']}' "
                             f"({libro['autor']}, {libro['año']}) [{estado}]\n")
                    archivo.write(linea)

                # Escribir sección de estadísticas al final del archivo
                archivo.write("\n" + "=" * 60 + "\n")
                archivo.write("ESTADÍSTICAS\n")
                archivo.write("=" * 60 + "\n")

                total = len(biblioteca)
                disponibles = sum(1 for l in biblioteca if l["disponible"])
                prestados = total - disponibles

                archivo.write(f"Total de libros    : {total}\n")
                archivo.write(f"Libros disponibles : {disponibles}\n")
                archivo.write(f"Libros prestados   : {prestados}\n")

        print(f"✅ Catálogo exportado exitosamente a '{nombre_archivo}'.")

    except IOError as e:
        # Manejar errores de escritura del archivo
        print(f"⚠️  Error al exportar el archivo: {e}")


# =============================================================================
# FUNCIÓN AUXILIAR PARA OBTENER UN ID VÁLIDO
# =============================================================================

def obtener_id(mensaje):
    """
    Solicita y valida que el usuario ingrese un ID numérico.
    Retorna el ID como entero o None si la entrada no es válida.

    Parámetro:
        mensaje (str): Texto del prompt que se muestra al usuario.
    """
    id_input = input(mensaje).strip()

    # Verificar que el valor ingresado sea un número positivo
    if not id_input.isdigit() or int(id_input) <= 0:
        print("⚠️  El ID debe ser un número entero positivo.")
        return None

    return int(id_input)


# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def menu_principal():
    """
    Implementa el menú interactivo del sistema de biblioteca.
    Utiliza un bucle while para repetir el menú hasta que el usuario
    seleccione la opción de salir (opción 0).
    """
    print("\n" + "=" * 60)
    print("     🏛️  SISTEMA DE GESTIÓN DE BIBLIOTECA  🏛️")
    print("=" * 60)

    # Bucle principal: se repite hasta que el usuario elija salir
    while True:
        # Mostrar las opciones del menú
        print("\n📋 MENÚ PRINCIPAL")
        print("-" * 40)
        print("  1. Agregar libro")
        print("  2. Mostrar todos los libros")
        print("  3. Buscar libro por título o autor")
        print("  4. Prestar libro")
        print("  5. Devolver libro")
        print("  6. Eliminar libro")
        print("  7. Libros por autor")
        print("  8. Ver estadísticas")
        print("  9. Exportar catálogo a TXT")
        print("  0. Salir")
        print("-" * 40)

        # Solicitar la opción del usuario
        opcion = input("Selecciona una opción: ").strip()

        # Procesar la opción seleccionada con estructura if-elif
        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            mostrar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            mostrar_libros()  # Mostrar libros para facilitar la selección
            id_libro = obtener_id("Ingresa el ID del libro a prestar: ")
            if id_libro is not None:
                prestar_libro(id_libro)

        elif opcion == "5":
            mostrar_libros()  # Mostrar libros para facilitar la selección
            id_libro = obtener_id("Ingresa el ID del libro a devolver: ")
            if id_libro is not None:
                devolver_libro(id_libro)

        elif opcion == "6":
            mostrar_libros()  # Mostrar libros para facilitar la selección
            id_libro = obtener_id("Ingresa el ID del libro a eliminar: ")
            if id_libro is not None:
                eliminar_libro(id_libro)

        elif opcion == "7":
            autor_buscar = input("\nIngresa el nombre del autor: ").strip()
            if autor_buscar:
                libros_por_autor(autor_buscar)
            else:
                print("⚠️  Debes ingresar el nombre de un autor.")

        elif opcion == "8":
            estadisticas()

        elif opcion == "9":
            exportar_a_txt()

        elif opcion == "0":
            # Despedida y salida del sistema
            print("\n👋 ¡Hasta pronto! Gracias por usar el Sistema de Biblioteca.")
            print("=" * 60)
            break  # Salir del bucle while y terminar el programa

        else:
            # Opción no válida
            print("⚠️  Opción no válida. Por favor selecciona una opción del menú.")


# =============================================================================
# DATOS DE EJEMPLO (opcionales, para facilitar las pruebas)
# =============================================================================

def cargar_datos_ejemplo():
    """
    Carga una serie de libros de ejemplo en la biblioteca para
    facilitar las pruebas del sistema sin necesidad de ingresar
    datos manualmente desde cero.
    """
    global contador_id

    libros_ejemplo = [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año": 1605},
        {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "año": 1985},
        {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "año": 2001},
        {"titulo": "Rayuela", "autor": "Julio Cortázar", "año": 1963},
    ]

    for datos in libros_ejemplo:
        libro = {
            "id": contador_id,
            "titulo": datos["titulo"],
            "autor": datos["autor"],
            "año": datos["año"],
            "disponible": True
        }
        biblioteca.append(libro)
        contador_id += 1

    print("✅ Se cargaron 5 libros de ejemplo en el sistema.")


# =============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Preguntar si se desean cargar datos de ejemplo al iniciar
    respuesta = input("¿Deseas cargar libros de ejemplo para pruebas? (s/n): ").strip().lower()
    if respuesta == "s":
        cargar_datos_ejemplo()

    # Iniciar el menú principal
    menu_principal()