import socket
import sys

from iot_storytelling_backend import fcm

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port
CHUNK_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def ping_host_ip():
    ip_str = str(socket.gethostbyname(socket.gethostname()))
    fcm.push_event(ip_str, event="host", silent=True)


def handle_connection(conn):

    # Receiving from client
    data = b''
    while True:
        chunk = conn.recv(CHUNK_SIZE)
        if chunk:
            data += chunk
            if len(chunk) < CHUNK_SIZE:
                break
        else:
            break

    # TODO: Some Processing of the data
    print('SERVER %s' % data)

    # Send action to other devices
    # fcm.push_event(str(data))


def start():
    # notify sensor app that server is running
    ping_host_ip()

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('SERVER Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    # Start listening on socket
    s.listen()
    print('SERVER Socket now listening')

    # now keep talking with the client
    while True:
        try:
            # wait to accept a connection - blocking call
            conn, addr = s.accept()
            print('SERVER Connected with ' + addr[0] + ':' + str(addr[1]))
            handle_connection(conn)
        except Exception as e:
            print(e)
            break

    s.close()


if __name__ == '__main__':
    start()
