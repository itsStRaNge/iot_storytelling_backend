import socket
import sys
import threading
import json
from iot_storytelling_backend import fcm
from iot_storytelling_backend import http_server
from iot_storytelling_backend import config


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handle_connection(conn):

    # Receiving data from client
    data = b''
    while True:
        chunk = conn.recv(config.TCP_CHUNK_SIZE)
        if chunk:
            data += chunk
            if len(chunk) < config.TCP_CHUNK_SIZE:
                break
        else:
            break

    print('SERVER received: %s' % data)

    data_str = data.decode('utf8').replace("'", '"')
    d = json.loads(data_str)

    # TODO: Do Processing of the data

    # Send action to other devices
    fcm.update_actuator("0", audio="sound.wav", image="image.png", text="first.txt")


def server_loop():
    while True:
        try:
            # wait to accept a connection - blocking call
            conn, addr = s.accept()
            print('SERVER Connected with ' + addr[0] + ':' + str(addr[1]))
            handle_connection(conn)
        except Exception as e:
            print(e)
            break


def start():
    # start http server
    t1 = threading.Thread(target=http_server.run)
    t1.start()

    # Bind socket to local host and port
    try:
        s.bind((config.TCP_HOST, config.TCP_PORT))
    except socket.error as e:
        print('SERVER Bind failed. Error Code : %s' % e)
        sys.exit()

    # Start listening on socket
    s.listen()
    print('SERVER started')

    # update tcp and http host address for devices
    fcm.update_host()

    # update available data for actuators
    fcm.update_available_data()

    # enter the server loop
    server_loop()

    # should never be reached
    s.close()


if __name__ == '__main__':
    start()
