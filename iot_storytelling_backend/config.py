import socket
import os


IPv4 = str(socket.gethostbyname(socket.gethostname()))

# TCP Server
TCP_HOST = '0.0.0.0'  # Symbolic name, meaning all available interfaces
TCP_PORT = 8888  # Arbitrary non-privileged port
TCP_CHUNK_SIZE = 1024

# HTTP Server
HTTP_HOST = '0.0.0.0'  # all interfaces
HTTP_PORT = 8080

# locations of sources
AUDIO_DIR = os.path.dirname(os.path.abspath(__file__)) + "/audio"
IMAGE_DIR = os.path.dirname(os.path.abspath(__file__)) + "/image"
TEXT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/text"
