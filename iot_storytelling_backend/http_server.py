from flask import Flask
from flask import send_file

HOST = '0.0.0.0'  # all interfaces
PORT = 8080
app = Flask(__name__)


def run():
    app.run(host=HOST, port=PORT)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/audio/<file>')
def send_audio(file):
    full_path = 'audio/' + file
    return send_file(
        full_path,
        mimetype="audio/wav",
        as_attachment=True,
        attachment_filename=file)


@app.route('/image/<file>')
def send_image(file):
    full_path = 'image/' + file
    return send_file(
        full_path,
        mimetype="image/png",
        as_attachment=True,
        attachment_filename=file)


if __name__ == '__main__':
    run()
