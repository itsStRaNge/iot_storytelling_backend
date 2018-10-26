import socket
import sys
import threading
import json
from datetime import datetime
import fcm
import http_server
import config
import decision

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def log(msg):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + msg)
    sys.stdout.flush()

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

    log('SERVER received: %s' % data)
    data_str = data.decode('utf8').replace("'", '"')
    d = json.loads(data_str)

    # TODO adjust decision fct call ok
    # call decision function
    decision.make(d['position'], d['qr_code'])
    log("SERVER Decision %s %s" % (song, picture))

    # Send action to other devices
    # fcm.update_actuator("0", audio=song, image=picture, text="none.txt")


def server_loop():
    while True:
        try:
            # wait to accept a connection - blocking call
            conn, addr = s.accept()
            log('SERVER Connected with ' + addr[0] + ':' + str(addr[1]))
            handle_connection(conn)
        except KeyboardInterrupt:
            break
        except Exception as e:
            log("Connection Error: %s" % e)


def start():
    # start http server
    t1 = threading.Thread(target=http_server.run)
    t1.start()

    # Bind socket to local host and port
    try:
        s.bind((config.TCP_HOST, config.TCP_PORT))
    except socket.error as e:
        log('SERVER Bind failed. Error Code : %s' % e)
        sys.exit()

    # Start listening on socket
    s.listen()

    # update tcp and http host address for devices
    log("SERVER Update Database")
    fcm.update_host()

    # update available data for actuators
    fcm.update_available_data()

    log('SERVER is running')
    # enter the server loop
    server_loop()

    # should never be reached
    s.close()


if __name__ == '__main__':
    start()
