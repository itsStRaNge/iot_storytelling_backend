from iot_storytelling_backend import fcm

previous_state = "state_1"
current_state = "state_1"
next_state = ""

previous_qrcode = "code0"

previous_pos = 0

def init_all():
    # update available data for actuators
    fcm.update_available_data()

    # update tcp and http host address for devices
    fcm.update_host()

    # TODO add black image to src files and set all states of actuator devices to black image in firebase


# TODO notify devices within decision function
# fcm.update_actuator("0", audio=song, image=picture, text="none.txt")
# fcm.update_sensor(image="none.png", audio="none.wav", text="none.txt")


def make(pos, qrcode):
    global previous_state
    global current_state
    global next_state
    global previous_qrcode
    global previous_pos

    print("previous qr code before: %s" % previous_qrcode)
    print("current qr code before: %s" % qrcode)
    print("current state before: %s" % current_state)

    if current_state == "state_1":
        next_state = process_state_1(qrcode, pos)

    if current_state == "state_2":
        next_state = process_state_2(qrcode, pos)

    if current_state == "state_3":
        next_state = process_state_3(qrcode, pos)

    if current_state == "state_4":
        next_state = process_state_4(qrcode, pos)

    if current_state == "state_5":
        next_state = process_state_5(qrcode, pos)

    previous_state = current_state
    current_state = next_state

    previous_qrcode = qrcode
    previous_pos = pos

    print("previous qr code after: %s" % previous_qrcode)
    print("current qr code after: %s" % qrcode)
    print("current state after: %s" % current_state)


def process_state_1(qrcode, pos):
    if qrcode == previous_qrcode:
        if pos == 0:
            return "state_1"
        elif pos == 1:
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    elif qrcode == "code1":
        if pos == 0:
            fcm.update_actuator("0", audio="lighthouse-1.mp3", image="lighthouse_single.gif", text="lighthouse-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("0", audio="lighthouse-2.mp3", image="lighthouse_single.gif", text="lighthouse-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="lighthouse-3.mp3", image="lighthouse_single.gif", text="lighthouse-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_2"

    elif qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="blank.gif", text="blank-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="blank.gif", text="blank-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.gif", text="blank-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    elif qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="tree.gif", text="tree-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="tree.gif", text="tree-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("2", image="tree.gif", text="tree-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    elif qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="moon-1.mp3", image="moon_single.gif", text="moon-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("3", audio="moon-2.mp3", image="moon_single.gif", text="moon-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_4"
        elif pos == 2:
            fcm.update_actuator("3", audio="moon-3.mp3", image="moon_single.gif", text="moon-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

def process_state_2(qrcode, pos):
    if qrcode == previous_qrcode:
        if pos == 0:
            return "state_2"
        elif pos == 1:
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_2"
        elif pos == 2:
            fcm.update_actuator("0", audio="piano2.mp3", image="lighthouse_couple", text="lighthouse-4.txt")
            fcm.update_sensor(bird="invisible", text="return_piano.txt")
            return "state_3"

    if qrcode == "code1":
        if pos == 0:
            return "state_2"
        elif pos == 1:
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_2"
        elif pos == 2:
            fcm.update_actuator("0", audio="piano2.mp3", image="lighthouse_couple", text="lighthouse-4.txt")
            fcm.update_sensor(bird="invisible", text="return_piano.txt")
            return "state_3"

    if qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="blank.gif", text="blank-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="blank.gif", text="blank-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.gif", text="blank-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    if qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="tree.gif", text="tree-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="tree.gif", text="tree-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("2", image="tree.gif", text="tree-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    if qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="moon-1.mp3", image="moon_single.gif", text="moon-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("3", audio="moon-2.mp3", image="moon_single.gif", text="moon-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_4"
        elif pos == 2:
            fcm.update_actuator("3", audio="moon-3.mp3", image="moon_single.gif", text="moon-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

def process_state_3(qrcode, pos):
    if pos == 2:
        fcm.update_actuator("0", image="lighthouse_single.gif", text="lighthouse-5.txt")
        fcm.update_sensor(bird="visible", text="start.txt")
        return "state_2"
    else:
        return "state_3"

def process_state_4(qrcode, pos):
    if qrcode == previous_qrcode:
        if pos == 0:
            return "state_4"
        elif pos == 1:
            fcm.update_actuator("3", audio="guitar-2.mp3", image="moon_couple_gif", text="moon-4.txt")
            fcm.update_sensor(bird="invisible", text="return_guitar.txt")
            return "state_5"
        elif pos == 2:
            fcm.update_sensor(audio="piano.mp3")
            return "state_4"

    if qrcode == "code1":
        if pos == 0:
            fcm.update_actuator("0", audio="lighthouse-1.mp3", image="lighthouse_single.gif", text="lighthouse-1.txt")
            return "state_2"
        elif pos == 1:
            fcm.update_actuator("0", audio="lighthouse-2.mp3", image="lighthouse_single.gif", text="lighthouse-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="lighthouse-3.mp3", image="lighthouse_single.gif", text="lighthouse-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    if qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="blank.gif", text="blank-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="blank.gif", text="blank-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.gif", text="blank-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    if qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="tree.gif", text="tree-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="tree.gif", text="tree-2.txt")
            fcm.update_sensor(audio="guitar1.mp3")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("2", image="tree.gif", text="tree-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

    if qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="moon-1.mp3", image="moon_single.gif", text="moon-1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("3", audio="guitar-2.mp3", image="moon_couple_gif", text="moon-4.txt")
            fcm.update_sensor(bird="invisible", text="return_guitar.txt")
            return "state_5"
        elif pos == 2:
            fcm.update_actuator("3", audio="moon-3.mp3", image="moon_single.gif", text="moon-3.txt")
            fcm.update_sensor(audio="piano1.mp3")
            return "state_1"

def process_state_5(qrcode, pos):
    if pos == 1:
        fcm.update_actuator("3", image="moon_single.gif", text="moon-5.txt")
        fcm.update_sensor(bird="visible", text="start.txt")
        return "state_4"
    else:
        return "state_5"



if __name__ == "__main__":
    make(2, "code0")
    make(1, "code0")
    make(2, "code0")
    make(0, "code0")
    make(1, "code1")

