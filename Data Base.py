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
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()
    print("Usuario agregado")

def ver_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)

def actualizar_usuario(id, nombre, edad):
    cursor.execute("UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, id))
    conexion.commit()
    print("Usuario actualizado")

def eliminar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit()
    print("Usuario eliminado")

# -------- PRUEBA --------

agregar_usuario("Juan", 25)
agregar_usuario("Maria", 30)

print("\nUsuarios:")
ver_usuarios()

actualizar_usuario(1, "Juan Perez", 26)

print("\nUsuarios actualizados:")
ver_usuarios()

eliminar_usuario(2)

print("\nUsuarios finales:")
ver_usuarios()

# Cerrar conexión
conexion.close()