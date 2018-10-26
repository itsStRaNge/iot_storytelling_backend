import socket
import os
import sys

# Productive mode will use the Productive node at firebase db otherwise Develop node is used
PRODUCTIVE = False

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

# Get IPv4
# approach differs from operating system
IPv4 = None
if sys.platform == "linux":
    from netifaces import ifaddresses, AF_INET
    IPv4 = ifaddresses('wlan0')[AF_INET][0]['addr']
else:
    # IPv4 = str(socket.gethostbyname(socket.gethostname()))
    IPv4 = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
print("IPv4 - " + IPv4)
