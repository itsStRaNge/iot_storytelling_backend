import socket
import sys
import threading
from iot_storytelling_backend import fcm
from iot_storytelling_backend import http_server

IPv4 = str(socket.gethostbyname(socket.gethostname()))
HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port
CHUNK_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def ping_host_ip():
    fcm.push_event(IPv4, event="host")


def handle_connection(conn):

    # Receiving data from client
    data = b''
    while True:
        chunk = conn.recv(CHUNK_SIZE)
        if chunk:
            data += chunk
            if len(chunk) < CHUNK_SIZE:
                break
        else:
            break

    # TODO: Do Processing of the data
    print('SERVER received: %s' % data)

    # Send action to other devices
    fcm.push_event(str(data))


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
        s.bind((HOST, PORT))
    except socket.error as e:
        print('SERVER Bind failed. Error Code : %s' % e)
        sys.exit()

    # Start listening on socket
    s.listen()
    print('SERVER Socket now listening')

    # notify sensor app that server is running
    ping_host_ip()

    # enter the server loop
    server_loop()

    # should never be reached
    s.close()


if __name__ == '__main__':
    start()
