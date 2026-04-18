import socket

HOST = '127.0.0.1'
PORT = 5000

print("Iniciando cliente...")

def iniciar_cliente():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("Conectado al servidor")

        while True:
            mensaje = input("Escribí un mensaje (o 'éxito' para salir): ")

            if mensaje.lower() == "éxito":
                break

            client_socket.send(mensaje.encode())

            respuesta = client_socket.recv(1024).decode()
            print(f"Servidor: {respuesta}")

        client_socket.close()

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor.")
    except Exception as e:
        print(f"Error en el cliente: {e}")


if __name__ == "__main__":
    iniciar_cliente()