from flask import Flask
from flask import send_file
import config


app = Flask(__name__)


def run():
    # start http server
    app.run(host=config.HTTP_HOST, port=config.HTTP_PORT)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/audio/<file>')
def send_audio(file):
    full_path = 'audio/' + file
    return send_file(
        full_path,
        mimetype="audio/mp3",
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


@app.route('/text/<file>')
def send_text(file):
    full_path = 'text/' + file
    return send_file(
        full_path,
        mimetype="text/txt",
        as_attachment=True,
        attachment_filename=file)


if __name__ == '__main__':
    run()
