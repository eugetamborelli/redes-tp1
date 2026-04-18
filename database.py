import sqlite3

DB_NAME = "chat.db"

# Crear base de datos y tabla
def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT,
                fecha_envio TEXT,
                ip_cliente TEXT
            )
        """)

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")


# Guardar mensaje
def save_message(contenido, fecha_envio, ip_cliente):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, fecha_envio, ip_cliente))

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error al guardar mensaje: {e}")