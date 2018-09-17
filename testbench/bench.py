import threading
from iot_storytelling_backend import server
from testbench import client


server_thread = threading.Thread(target=server.start)
server_thread.start()

client.send_test_data()

