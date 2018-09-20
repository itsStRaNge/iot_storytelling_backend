import socket
import json
from iot_storytelling_backend.server import PORT
JSON_FILE = 'test_data.json'

TCP_IP = 'localhost'  # socket.gethostbyname(socket.gethostname())
TCP_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_test_data():
    with open(JSON_FILE) as f:
        loaded_json = json.load(f)
        send_msg(str(loaded_json))


def send_msg(msg):
    s.connect((TCP_IP, PORT))
    print("CLIENT sending %s" % msg)
    s.send(msg.encode('utf-8'))
    s.close()
