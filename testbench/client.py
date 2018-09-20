import socket
import json
import time
from datetime import datetime
from iot_storytelling_backend.config import TCP_PORT


JSON_FILE = 'test_data.json'
TCP_IP = 'localhost'  # socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_test_data():
    with open(JSON_FILE) as f:
        loaded_json = json.load(f)
        send_msg(str(loaded_json))


def send_msg(msg):
    s.connect((TCP_IP, TCP_PORT))
    time.sleep(2)
    print(datetime.now())
    print("CLIENT sending %s" % msg)
    s.send(msg.encode('utf-8'))
    s.close()
