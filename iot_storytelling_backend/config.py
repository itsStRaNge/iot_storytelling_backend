import socket

IPv4 = str(socket.gethostbyname(socket.gethostname()))

# TCP Server
TCP_HOST = ''  # Symbolic name, meaning all available interfaces
TCP_PORT = 8888  # Arbitrary non-privileged port
TCP_CHUNK_SIZE = 1024

# HTTP Server
HTTP_HOST = '0.0.0.0'  # all interfaces
HTTP_PORT = 8080
