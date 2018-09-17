import socket
import json

JSON_FILE = 'test_data.json'

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_test_data():
    with open(JSON_FILE) as f:
        loaded_json = json.load(f)
        send_msg(str(loaded_json))


def send_msg(msg):
    s.connect((TCP_IP, TCP_PORT))
    print("CLIENT sending %s" % msg)
    s.send(msg.encode('utf-8'))
    s.close()
