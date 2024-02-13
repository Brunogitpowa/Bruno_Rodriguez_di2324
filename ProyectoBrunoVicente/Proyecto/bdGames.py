import sqlite3 
import subprocess 
import zipfile #para el manejo de ficheros .zip
import shutil #biblioteca para el manejo de ficheros mover, copiar etc
import glob #biblioteca para detectar rutas y encontrar ficheros
import os

# Conéctate a la base de datos (esto creará el archivo si no existe)
conn = sqlite3.connect('games.db')

# Crea un cursor
cursor = conn.cursor()

# Crea una tabla para los juegos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        imagen TEXT NOT NULL,
        description TEXT
    )
""")


def play_game(game_id):
    # Conéctate a la base de datos
    conn = sqlite3.connect('games.db')

    # Crea un cursor
    cursor = conn.cursor()

    # Busca el juego en la base de datos
    cursor.execute("SELECT path FROM games WHERE id = ?", (game_id,))

    # Obtiene la ruta al archivo del juego
    game_path = cursor.fetchone()[0]

    # Cierra la conexión a la base de datos
    conn.close()

    # Ejecuta el juego
    subprocess.run(["python", game_path])

def add_game(name, zip_path, image, description):
    try:
        print("Iniciando la adición del juego...")

        # Crea una nueva carpeta para el juego en la carpeta Games
        new_folder_path = os.path.join('Games', name)
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Carpeta creada: {new_folder_path}")

        # Copia el archivo zip a la nueva carpeta
        new_zip_path = os.path.join(new_folder_path, os.path.basename(zip_path))
        shutil.copy(zip_path, new_zip_path)
        print(f"Archivo zip copiado a: {new_zip_path}")

        # Descomprime el archivo zip en la nueva carpeta
        with zipfile.ZipFile(new_zip_path, 'r') as zip_ref:
            zip_ref.extractall(new_folder_path)
        print(f"Archivo zip descomprimido en: {new_folder_path}")

        # Busca el archivo .py principal en la carpeta descomprimida
        py_files = glob.glob(os.path.join(new_folder_path, "*.py"))
        main_script_path = py_files[0]  # Asume que el primer archivo .py es el principal
        print(f"Script principal encontrado: {main_script_path}")

        # Conéctate a la base de datos
        conn = sqlite3.connect('games.db')
        print("Conexión a la base de datos establecida")

        # Crea un cursor
        cursor = conn.cursor()

        # Inserta el nuevo juego en la base de datos
        cursor.execute("INSERT INTO games (name, path, imagen, description) VALUES (?, ?, ?, ?)", (name, main_script_path, image, description))
        print("Juego insertado en la base de datos")

        # Confirma los cambios
        conn.commit()
        print("Cambios confirmados")

    except Exception as e:
        print(f"Error al añadir el juego: {e}")

    finally:
        # Cierra la conexión a la base de datos
        if conn:
            conn.close()
        print("Conexión a la base de datos cerrada")


def get_game_count():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM games")
    game_count = cursor.fetchone()[0]
    conn.close()
    return game_count


def get_game_details(game_id):
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    cursor.execute("SELECT imagen, description FROM games WHERE id = ?", (game_id,))
    game_details = cursor.fetchone()
    conn.close()
    print(game_details)
    return game_details

def get_game_script(game_id):
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    cursor.execute("SELECT path FROM games WHERE id = ?", (game_id,))
    result = cursor.fetchone()

    conn.close()

    if result is not None:
        return result[0]
    else:
        return None