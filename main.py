import socket
import sys
import fcm

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Start listening on socket
s.listen()
print('Socket now listening')

# now keep talking with the client
while True:
    try:
        # wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        while True:
            # Receiving from client
            data = conn.recv(1024)
            print(data)
            fcm.push_event(str(data))
            if not data:
                break
    except Exception:
        break

s.close()
