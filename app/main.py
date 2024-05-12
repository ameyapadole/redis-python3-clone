import socket
"""
        The server_socket.accept(), gives us two things, connection and address
        + = simple string
        \r
        \n
"""

def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept()
    with connection:
        connection.recv(1024) #1024 number of bytes we can recieve
        connection.send(pong.encode()) #Send accepts a utf string to be send

    pong = "+PONG\r\n"


if __name__ == "__main__":
    main()
