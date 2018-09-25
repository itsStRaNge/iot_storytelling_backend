import socket
import os
from os import listdir
from os.path import isfile, join

# Number of event receiving Devices
NUMBER_ACTUATORS = 2

# TCP Server
TCP_HOST = ''  # Symbolic name, meaning all available interfaces
TCP_PORT = 8888  # Arbitrary non-privileged port
TCP_CHUNK_SIZE = 1024

# HTTP Server
HTTP_HOST = '0.0.0.0'  # all interfaces
HTTP_PORT = 8080

IPv4 = str(socket.gethostbyname(socket.gethostname()))

# locations of sources
AUDIO_DIR = os.path.dirname(os.path.abspath(__file__)) + "/audio"
IMAGE_DIR = os.path.dirname(os.path.abspath(__file__)) + "/image"
TEXT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/text"

# list of files
audio_files = [f for f in listdir(AUDIO_DIR) if isfile(join(AUDIO_DIR, f))]
image_files = [f for f in listdir(IMAGE_DIR) if isfile(join(IMAGE_DIR, f))]
text_files = [f for f in listdir(TEXT_DIR) if isfile(join(TEXT_DIR, f))]
