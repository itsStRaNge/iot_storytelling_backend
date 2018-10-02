import socket
import os
import sys


def ip4_addresses():
    from netifaces import interfaces, ifaddresses, AF_INET
    return ifaddresses('wlan0')[AF_INET][0]['addr']

IPv4 = None
if sys.platform == "linux":
    IPv4 = ip4_addresses()
else:
    IPv4 = str(socket.gethostbyname(socket.gethostname()))
print("IPv4 - " + IPv4)

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
