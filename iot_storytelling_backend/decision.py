from iot_storytelling_backend import fcm

previous_state = "state_1"
current_state = "state_1"
next_state = ""


previous_qrcode = "code0"
print("previous qr code before: %s" % previous_qrcode)
previous_pos = 0

def init_all():
    # update available data for actuators
    fcm.update_available_data()

    # update tcp and http host address for devices
    fcm.update_host()

    fcm.update_actuator("0", image="background_black.png")
    # TODO add black image to src files and set all states of actuator devices to black image in firebase


# TODO notify devices within decision function
# fcm.update_actuator("0", audio="song.mp3", image="picture.png", text="none.txt")
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

    if qrcode == "code0":
        if pos == 0:
            return "state_1"
        elif pos == 1:
            fcm.update_sensor(audio="guitar_1.mp3", image="background.png", text="start.txt")
            return "state_1"
        elif pos == 2:
            fcm.update_sensor(audio="piano_1.mp3", image="background.png", text="start.txt")
            return "state_1"

    elif qrcode == "code1":
        if pos == 0:
            fcm.update_sensor(image="background.png", text="start.txt")
            fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_1.txt")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
            fcm.update_actuator("3", image="background_black.gif")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
            fcm.update_actuator("3", image="background_black.gif")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_3.txt")
            fcm.update_sensor(audio="piano_1.mp3")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
            fcm.update_actuator("3", image="background_black.gif")
            return "state_2"

    elif qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt", audio="none.wav")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.boy_bird_2_tree", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"

    elif qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_1.txt")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="girl_bird_1_crash.mp3", image="girl_bird_1_mountain.gif", text="girl_bird_1_3.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"

    elif qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_1_1.txt")
            return "state_1"
            fcm.update_actuator("0", image="background_black.gif")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
        elif pos == 1:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_1_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
            return "state_4"
        elif pos == 2:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_1_3.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("0", image="background_black.gif")
            fcm.update_actuator("1", image="background_black.gif")
            fcm.update_actuator("2", image="background_black.gif")
            return "state_1"



def process_state_2(qrcode, pos):
    if qrcode == "code0":
        if pos == 0:
            return "state_2"
        elif pos == 1:
            fcm.update_sensor(audio="guitar_1.mp3")
            return "state_2"
        elif pos == 2:
            fcm.update_actuator("0", audio="piano_2.mp3", image="couple_lighthouse.gif", text="boy_bird_1_4.txt")
            fcm.update_sensor(bird="invisible", text="return.txt")
            return "state_3"

    if qrcode == "code1":
        if pos == 0:
            return "state_2"
        elif pos == 1:
            fcm.update_sensor(audio="guitar_1.mp3")
            return "state_2"
        elif pos == 2:
            fcm.update_actuator("0", audio="piano_2.mp3", image="couple_lighthouse.gif", text="boy_bird_1_4.txt")
            fcm.update_sensor(bird="invisible", text="return.txt")
            return "state_3"

    if qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.boy_bird_2_tree", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"

    if qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_1.txt")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="girl_bird_1_crash.mp3", image="girl_bird_1_mountain.gif", text="girl_bird_1_3.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"

    if qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_2_1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_2_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            return "state_4"
        elif pos == 2:
            fcm.update_actuator("3", audio="girl_bird_2_1.mp3", image="girl_bird_2_moon.gif", text="girl_bird_2_3.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            return "state_1"

def process_state_3(qrcode, pos):
    if pos == 0:
        fcm.update_actuator("0", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_5.txt")
        fcm.update_sensor(bird="visible", text="start.txt")
        return "state_2"
    else:
        return "state_3"

def process_state_4(qrcode, pos):
    if qrcode == "code0":
        if pos == 0:
            return "state_4"
        elif pos == 1:
            fcm.update_actuator("3", audio="girl_bird_2_2.mp3", image="couple_moon.gif", text="girl_bird_2_4.txt")
            fcm.update_sensor(bird="invisible", text="return.txt")
            return "state_5"
        elif pos == 2:
            fcm.update_sensor(audio="piano_1.mp3")
            return "state_4"

    if pos == 0:
        fcm.update_sensor(image="background.png", text="start.txt")
        fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_1.txt")
        fcm.update_actuator("1", image="background_black.gif")
        fcm.update_actuator("2", image="background_black.gif")
        fcm.update_actuator("3", image="background_black.gif")
        return "state_1"
    elif pos == 1:
        fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_2.txt")
        fcm.update_sensor(audio="guitar_2.mp3")
        fcm.update_actuator("1", image="background_black.gif")
        fcm.update_actuator("2", image="background_black.gif")
        fcm.update_actuator("3", image="background_black.gif")
        return "state_1"
    elif pos == 2:
        fcm.update_actuator("0", audio="piano_2.mp3", image="boy_bird_1_lighthouse.gif", text="boy_bird_1_3.txt")
        fcm.update_sensor(audio="piano_1.mp3")
        fcm.update_actuator("1", image="background_black.gif")
        fcm.update_actuator("2", image="background_black.gif")
        fcm.update_actuator("3", image="background_black.gif")
        return "state_2"

    if qrcode == "code2":
        if pos == 0:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("1", image="boy_bird_2_tree.gif", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"
        elif pos == 2:
            fcm.update_actuator("1", image="blank.boy_bird_2_tree", text="boy_bird_2_1.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")

            return "state_1"

    if qrcode == "code3":
        if pos == 0:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_1.txt")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("2", image="girl_bird_1_mountain.gif", text="girl_bird_1_2.txt")
            fcm.update_sensor(audio="guitar_2.mp3")
            fcm.update_actuator("0", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"
        elif pos == 2:
            fcm.update_actuator("0", audio="girl_bird_1_crash.mp3", image="girl_bird_1_mountain.gif", text="girl_bird_1_3.txt")
            fcm.update_sensor(audio="piano_2.mp3")
            fcm.update_actuator("2", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("1", image="background_black.gif", audio="none.wav")
            fcm.update_actuator("3", image="background_black.gif", audio="none.wav")
            return "state_1"

    if qrcode == "code4":
        if pos == 0:
            fcm.update_actuator("3", audio="moon_1.mp3", image="moon_single.gif", text="moon_1.txt")
            return "state_1"
        elif pos == 1:
            fcm.update_actuator("3", audio="guitar-2.mp3", image="moon_couple_gif", text="moon_4.txt")
            fcm.update_sensor(bird="invisible", text="return_guitar.txt")
            return "state_5"
        elif pos == 2:
            fcm.update_actuator("3", audio="moon-3.mp3", image="moon_single.gif", text="moon_3.txt")
            fcm.update_sensor(audio="piano_1.mp3")
            return "state_1"

def process_state_5(qrcode, pos):
    if pos == 0:
        fcm.update_actuator("3", image="single_moon.gif", text="girl_bird_2_5.txt")
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

