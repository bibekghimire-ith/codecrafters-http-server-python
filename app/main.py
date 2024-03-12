# Uncomment this to pass the first stage
import socket
import threading
import os
import sys

# BUFFER_SIZE = 4096
BUFFER_SIZE = 65536

ResponseString = str
ResponseData = str
ContentType = str

def read_from_socket(sock: socket.socket) -> str:
    data = sock.recv(BUFFER_SIZE)
    # print(data.decode())
    
    return data.decode()
    
    
def send_to_socet(sock: socket.socket, data: str) -> None:
    encoded_data = data.encode()
    sock.send(encoded_data)


def parse_method(data: str) -> str:
    lines = data.split("\r\n")
    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == "GET":
            return "GET"
        elif tokens[0] == "POST":
            return "POST"
        
def parse_path(data: str, method: str) -> str:
    lines = data.split("\r\n")
    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == method:
            return tokens[1]
        
def parse_user_agent(data: str) -> str:
    lines = data.split("\r\n")
    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == "User-Agent:":
            return " ".join(tokens[1:])
        
class HttpHandler:
    def __init__(self, file_folder_path: str) -> None:
        self._file_folder_path = file_folder_path
        
        
    def handle_connection(self, sock: socket.socket) -> None:
        data = read_from_socket(sock)
        response_string, response_data, content_type = self.get_resposne(data)
        if content_type:
            content_type += "\r\n"
        response = f"HTTP/1.1 {response_string}\r\n{content_type}Content-Length: {len(response_data)}\r\n\r\n{response_data}"
        send_to_socet(sock, response)
        
        
    def get_resposne(
        self, data: str
        ) -> tuple[ResponseString, ResponseData, ContentType]:

        method = parse_method(data)
        path = parse_path(data, method)
        
        content_type = ""
        response_data = ""
        
        if method == "GET":
            if path == "/":
                return "200 OK", response_data, content_type
            if path.startswith("/echo/"):
                content_type = "Content-Type: text/plain"
                response_data = path.replace("/echo/", "")
                return "200 OK", response_data, content_type
            if path.startswith("/user-agent"):
                user_agent = parse_user_agent(data)
                response_data = user_agent
                content_type = "Content-Type: text/plain"
                return "200 OK", response_data, content_type
            if path.startswith("/files/") and self._file_folder_path:
                file_name = path.replace("/files/", "")
                file_path = os.path.join(self._file_folder_path, file_name)
                
                
                if not os.path.exists(file_path) or not os.path.isfile(file_path):
                    return "404 Not Found", response_data, content_type
                
                
                with open(file_path, "r") as file:
                    file_data = file.read()
                    response_data = file_data
                    content_type = "Content-Type: application/octet-stream"
                return "200 OK", response_data, content_type
            else:
                return "404 Not Found", response_data, content_type
        elif method == "POST":
            if path.startswith("/files/") and self._file_folder_path:
                file_name = path.replace("/files/", "")
                file_path = os.path.join(self._file_folder_path, file_name)
                if os.path.exists(file_path):
                    return "404 Not Found", response_data, content_type
                file_content = "Test Data Here"
                
                with open(file_path, "w+") as file:
                    file_data = file.write(file_content)
                return "201 Created", response_data, content_type
            else:
                return "404 Not Found", response_data, content_type



def main():
    directory = None
    
    if len(sys.argv) == 3 and sys.argv[1] == "--directory":
        directory = sys.argv[2]
    handler = HttpHandler(directory)
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        client_socket, client_address = server_socket.accept()
        
        threading.Thread(
            target=lambda: handler.handle_connection(client_socket)
        ).start()


if __name__ == "__main__":
    main()
