import sqlite3

# Conectar (o crear) la base de datos
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")
conexion.commit()

# -------- FUNCIONES --------

def agregar_usuario(nombre, edad):
    if not nombre.strip():
        print("Error: el nombre no puede estar vacío")
        return
    if edad < 0:
        print("Error: la edad no puede ser negativa")
        return

    cursor.execute(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
        (nombre, edad)
    )
    conexion.commit()
    print("Usuario agregado")

def ver_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("No hay usuarios")
        return

    for id, nombre, edad in usuarios:
        print(f"ID: {id} | Nombre: {nombre} | Edad: {edad}")

def buscar_usuario_por_nombre(nombre):
    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre LIKE ?",
        ('%' + nombre + '%',)
    )
    resultados = cursor.fetchall()

    if not resultados:
        print("No se encontraron resultados")
        return

    for r in resultados:
        print(r)

def actualizar_usuario(id, nombre, edad):
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    if cursor.fetchone() is None:
        print("Usuario no encontrado")
        return

    cursor.execute(
        "UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?",
        (nombre, edad, id)
    )
    conexion.commit()
    print("Usuario actualizado")

def eliminar_usuario(id):
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    if cursor.fetchone() is None:
        print("Usuario no encontrado")
        return

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit()
    print("Usuario eliminado")

# -------- MENÚ INTERACTIVO --------

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Salir")

        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                agregar_usuario(nombre, edad)

            elif opcion == "2":
                ver_usuarios()

            elif opcion == "3":
                nombre = input("Buscar nombre: ")
                buscar_usuario_por_nombre(nombre)

            elif opcion == "4":
                id = int(input("ID: "))
                nombre = input("Nuevo nombre: ")
                edad = int(input("Nueva edad: "))
                actualizar_usuario(id, nombre, edad)

            elif opcion == "5":
                id = int(input("ID a eliminar: "))
                eliminar_usuario(id)

            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción inválida")

        except ValueError:
            print("Error: ingresá valores válidos (por ejemplo, números en edad o ID)")

# -------- EJECUCIÓN --------

menu()

# Cerrar conexión al salir
conexion.close()

