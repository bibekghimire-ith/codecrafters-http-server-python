# Uncomment this to pass the first stage
import socket


BUFFER_SIZE = 4096

def read_from_socket(sock: socket.socket) -> None:
    data = sock.recv(BUFFER_SIZE)
    print(data.decode())
    
    
def send_to_socet(sock: socket.socket, data: str) -> None:
    encoded_data = data.encode()
    sock.send(encoded_data)


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    client_socket, client_address = server_socket.accept()
    read_from_socket(client_socket)

    send_to_socet(client_socket, "HTTP/1.1 200 OK\r\n\r\n")


if __name__ == "__main__":
    main()
