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
#Se crearon tres tablas: Id, nombres y edad
conexion.commit() #guarda la info en la base de datos

# -------- FUNCIONES --------

def agregar_usuario(nombre, edad):
    if not nombre.strip():
        print("Error: el nombre no puede estar vacío")
        return
    if edad < 0:
        print("Error: la edad no puede ser negativa")
        return

    
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad)) # (?, ?) sirve para que SQL no introduzca valores ignorando los valores ya dados.
    conexion.commit()
    print("Usuario agregado")

def ver_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall() #Devuelve una lista de  tuplas con los valores.
    for u in usuarios:
        print(u)

def buscar_usuario_por_nombre(nombre):
    cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    for r in resultados:
        print(r)

def actualizar_usuario(id, nombre, edad):
    cursor.execute("UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, id))
    conexion.commit()
    print("Usuario actualizado")

def eliminar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit() #Permite crear comandos
    print("Usuario eliminado")

# -------- PRUEBA --------

agregar_usuario("Juan", 25)
agregar_usuario("Maria", 30)

print("\nUsuarios:")
ver_usuarios()

buscar_usuario_por_nombre("Juan")

actualizar_usuario(1, "Juan Perez", 26)

print("\nUsuarios actualizados:")
ver_usuarios()

eliminar_usuario(2)

print("\nUsuarios finales:")
ver_usuarios()

# Cerrar conexión
conexion.close()
