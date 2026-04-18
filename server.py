import socket
from datetime import datetime
from database import init_db, save_message

HOST = '127.0.0.1'
PORT = 5000

# Configuración del socket TCP/IP
def iniciar_servidor():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Servidor escuchando en {HOST}:{PORT}")
        return server_socket
    except OSError:
        print("Error: el puerto está ocupado o no disponible.")
        return None


# Manejo de clientes
def manejar_cliente(client_socket, client_address):
    print(f"Conexión establecida con {client_address}")

    while True:
        try:
            mensaje = client_socket.recv(1024).decode()

            if not mensaje:
                break

            # Guardar mensaje en DB
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_message(mensaje, timestamp, client_address[0])

            # Respuesta al cliente
            respuesta = f"Mensaje recibido: {timestamp}"
            client_socket.send(respuesta.encode())

        except Exception as e:
            print(f"Error al manejar cliente: {e}")
            break

    client_socket.close()
    print(f"Conexión cerrada con {client_address}")


def aceptar_conexiones(server_socket):
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            manejar_cliente(client_socket, client_address)
        except KeyboardInterrupt:
            print("\nServidor detenido.")
            break
        except Exception as e:
            print(f"Error aceptando conexiones: {e}")


if __name__ == "__main__":
    init_db()  # Inicializa la base de datos

    server = iniciar_servidor()
    if server:
        aceptar_conexiones(server)