import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config

cred = credentials.Certificate(os.path.dirname(os.path.abspath(__file__)) + '/firebase_db_cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ntnu-iot-storytelling.firebaseio.com/'
})

if config.PRODUCTIVE:
    fdb = db.reference("Productive")
else:
    fdb = db.reference("Develop")


def update_host():
    # update data about host at database
    host_ref = fdb.child('Host')
    host_ref.update({
        'ip': config.IPv4,
        'tcp_port': config.TCP_PORT,
        'http_port': config.HTTP_PORT,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def update_available_data():
    # get all audio files
    audio_files = [f for f in listdir(config.AUDIO_DIR) if isfile(join(config.AUDIO_DIR, f))]
    update_data("audio", audio_files)

    # get all image files
    image_files = [f for f in listdir(config.IMAGE_DIR) if isfile(join(config.IMAGE_DIR, f))]
    update_data("images", image_files)

    # get all text files
    text_files = [f for f in listdir(config.TEXT_DIR) if isfile(join(config.TEXT_DIR, f))]
    update_data("text", text_files)


def update_data(key, data):
    # if data has changed, then push new data to database
    data_ref = fdb.child('Host').child(key)
    old_data = data_ref.get()

    try:
        if old_data != data:
            print("FCM Update Data for " + key)
            data_ref.delete()
            data_ref.set(data)
    except AttributeError:
        data_ref.set(data)


def update_actuator(device, image="none.png", audio="none.wav", text="none.txt"):
    # update state of actuator app in database
    ref = fdb.child("Actuator").child(device)
    ref.set({
        'image': image,
        'audio': audio,
        'text': text,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def update_sensor(image="none.png", audio="none.wav", text="none.txt"):
    # update state of sensor app in database
    ref = fdb.child("Sensor")
    ref.set({
        'image': image,
        'audio': audio,
        'text': text,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == '__main__':
    update_available_data()
