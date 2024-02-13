import sqlite3

def crear_bd():
    # Conectar a la base de datos (o crearla si no existe)
    conn = sqlite3.connect('usuarios.db')

    # Crear un cursor
    c = conn.cursor()

    # Crear la tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            email TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            imagen TEXT,
            realname TEXT,
            es_desarrollador BOOLEAN,
            nombreDistri TEXT,
            paisDistribuidor TEXT
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def registrar_usuario(email, username, password, imagen, realname, es_desarrollador, nombreDistribuidor, paisDistribuidor):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (email, username, password, imagen, realname, es_desarrollador, nombreDistribuidor, paisDistribuidor))
    conn.commit()
    conn.close()
    

def verificar_credenciales(username, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        SELECT * FROM usuarios WHERE username = ? AND password = ?
    ''', (username, password))
    usuario = c.fetchone()
    conn.close()
    return usuario is not None