IoT Storytelling - Backend
==========================
This project is meant to explore the field of Internet of Things combined with digital storytelling to show 
the interaction between user and devices over multiple communication channels.

The project was supervised by Andrew Perkis and Asim Hameed at the NTNU and implemented by Øyvind Klungre and Lukas Bernhard.

Project Description
--------------------------
The project contains two layers, an interactive and technological one. The backend implements most parts of the technological
layer. If you want to read more about the interactive part of the project, please visit [frontend](https://github.com/itsStRaNge/iot_storytelling_frontend.git).

The technological layer is based on IoT concepts and connects all devices over a cloud service.
The cloud service is divided into a logical and storage unit. The logical unit creates, based on the user interaction, 
a reaction event that is forwarded to all devices to show the reaction. The storage unit holds the current state of the 
whole system and logs all previous states in a timeline.

Project Overview
--------------------------
The backend basicly consists of four blocks:

The **TCP Server** is starting the whole application and will handle incoming actions from the user. At the startup 
the system updates all available media files in `audio/`, `image` and `text/` folders and updates the server's IPv4 address
and the selected ports (see `config.py`) on the firebase cloud service. All tablets will get a notification to adjust the server address and
to download all new media files.

The **HTTP Server** is used as access point for the devices to download all available media files at `audio/`, `image` and `text/`.

The **Firebase Cloud Service** is handling the connection and defines the structure of the firebase realtime database.

**Decision functions** is defining the actual story plot. The module creates an event depending on the user interaction
received from the tcp server. The event is pushed over the firebase cloud service to the realtime database which 
notifies all devices about a new state.

The **Firebase Realtime Database** is a service provided by Google to store data and make notifications on Android devices
more easy. To get an overview about the structure of the database please visit our [database](https://ntnu-iot-storytelling.firebaseio.com/)
and read the firebase [docs](https://firebase.google.com/docs/database/). The database is divided into a `Productive`
and `Develop` node to make the productive running system independent of future developments. You can set the mode at `config.py`.

![General System Overview](System%20Overview.jpg)

Installation and Setup
--------------------------
### General
Make sure to install **python 3.5** and run `pip3 install -r requirements.txt` to install all dependencies. To start 
the server execute `python ./iot_storytelling_backend/server.py`.

Always make sure that all devices and the backend are connected to the same WiFi network!

### Raspberry Pi

Usually just powering the raspberry pi will start the backend. At the desktop you can find different shell scripts:

* `show_server_output.sh` - executing this file in the terminal will show you the debug outputs of the server

* `restart_server.sh` - executing this file will restart the whole backend process

* `update_server.sh` - this will get the newest server version from the master branch and restart the server

You can get access to the raspberry pi with connection a screen to it or via ssh ([login credentials](https://ntnu-iot-storytelling.firebaseio.com/Productive/Host/login))

