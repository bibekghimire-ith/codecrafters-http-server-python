# Uncomment this to pass the first stage
import socket


# BUFFER_SIZE = 4096
BUFFER_SIZE = 65536

def read_from_socket(sock: socket.socket) -> str:
    data = sock.recv(BUFFER_SIZE)
    # print(data.decode())
    
    return data.decode()
    
    
def send_to_socet(sock: socket.socket, data: str) -> None:
    encoded_data = data.encode()
    sock.send(encoded_data)


def parse_path(data: str) -> str:
    lines = data.split("\r\n")
    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == "GET":
            return tokens[1]
        
        
def get_resposne_string(path: str) -> str:
    if path == "/":
        return "200 OK"
    else:
        return "404 Not Found"


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    client_socket, client_address = server_socket.accept()
    
    # read_from_socket(client_socket)
    data = read_from_socket(client_socket)
    path = parse_path(data)
    response_string = get_resposne_string(path)

    # send_to_socet(client_socket, "HTTP/1.1 200 OK\r\n\r\n")
    send_to_socet(client_socket, f"HTTP/1.1 {response_string}\r\n\r\n")


if __name__ == "__main__":
    main()
