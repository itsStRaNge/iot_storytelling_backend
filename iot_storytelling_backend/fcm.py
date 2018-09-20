import os
import firebase_admin
from datetime import datetime
from iot_storytelling_backend import config
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(os.path.dirname(os.path.abspath(__file__)) + '/firebase_db_cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://ntnu-iot-storytelling.firebaseio.com/'
})


def update_host():
    host_ref = db.reference('Host')
    host_ref.update({
        'ip': config.IPv4,
        'tcp_port': config.TCP_PORT,
        'http_port': config.HTTP_PORT
    })


def update_actuator(device, image, audio):
    ref = db.reference(device)
    ref.set({
        'image': image,
        'audio': audio,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
