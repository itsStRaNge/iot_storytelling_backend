import os
from os import listdir
from os.path import isfile, join
import firebase_admin
from datetime import datetime
from iot_storytelling_backend import config
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(os.path.dirname(os.path.abspath(__file__)) + '/firebase_db_cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ntnu-iot-storytelling.firebaseio.com/'
})


def update_host():
    host_ref = db.reference('Host')
    host_ref.update({
        'ip': config.IPv4,
        'tcp_port': config.TCP_PORT,
        'http_port': config.HTTP_PORT,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def update_available_data():
    audio_files = [f for f in listdir(config.AUDIO_DIR) if isfile(join(config.AUDIO_DIR, f))]
    update_data("Audio", audio_files)

    image_files = [f for f in listdir(config.IMAGE_DIR) if isfile(join(config.IMAGE_DIR, f))]
    update_data("Images", image_files)

    text_files = [f for f in listdir(config.TEXT_DIR) if isfile(join(config.TEXT_DIR, f))]
    update_data("Text", text_files)


def update_data(key, data):
    data_ref = db.reference('Host').child(key)
    old_data = data_ref.get()

    try:
        if old_data != data:
            print("FCM Update Data for " + key)
            data_ref.delete()
            data_ref.set(data)
    except AttributeError:
        data_ref.set(data)


def update_actuator(device, image="none.png", audio="none.wav", text="none.txt"):
    ref = db.reference("Actuator").child(device)
    ref.set({
        'image': image,
        'audio': audio,
        'text': text,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def update_sensor(image="none.png", audio="none.wav", text="none.txt"):
    ref = db.reference("Sensor")
    ref.set({
        'image': image,
        'audio': audio,
        'text': text,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == '__main__':
    update_available_data()
