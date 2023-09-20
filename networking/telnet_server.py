# Inside networking/__init__.py

import socket
import select

# Initialize socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5555))
server_socket.listen(5)

# List of sockets to monitor
sockets_list = [server_socket]

while True:
    # Wait for at least one of the sockets to be ready for processing
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for s in read_sockets:
        if s is server_socket:
            # Accept new connection
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
        else:
            # Read data from client
            data = s.recv(1024)
            if data:
                # Handle data (send to game logic)
                pass
            else:
                # Remove disconnected client
                sockets_list.remove(s)
